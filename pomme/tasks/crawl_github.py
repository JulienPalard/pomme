from datetime import datetime

import polib
from github import Github

from pomme import celery
from pomme.models.entry import Entry
from pomme.static import GH_TOKEN


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        60, index_python_docs_fr.s(), name="Update online users every minute"
    )


@celery.task
def index_python_docs_fr():
    g = Github(GH_TOKEN)
    repo = g.get_repo("python/python-docs-fr")
    root_files = repo.get_contents("/")  # Get root files

    po_files = []
    for file in root_files:
        if file.name.endswith(".po"):
            po_files.append(file)
    for file in po_files:

        pofile = polib.pofile(file.decoded_content.decode("utf-8"))

        for entry in pofile:
            Entry(
                msgid=entry.msgid,
                msgstr=entry.msgstr,
                id_lang="en",
                str_lang="fr",
                crawl_timestamp=datetime.utcnow().timestamp(),
                source_url=file.html_url,
                license="CC0",
            ).save()
