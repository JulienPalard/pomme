from datetime import datetime

import polib
from github import Github
from peewee import DoesNotExist

from pomme import celery
from pomme.models.entry import Entry
from pomme.static import GH_TOKEN


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        3600, index_python_docs_fr.s(), name="crawl_github_python-docs-fr"
    )


@celery.task
def index_python_docs_fr():
    g = Github(GH_TOKEN)
    repo = g.get_repo("python/python-docs-fr")

    po_files = []
    contents = repo.get_contents("/")  # Get root content
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            if file_content.type == "file" and file_content.name.endswith(".po"):
                po_files.append(file_content)

    count = 0
    for file in po_files:
        pofile = polib.pofile(file.decoded_content.decode("utf-8"))
        for entry in pofile:
            # If the entry is not fuzzy, or isn't the same as the untranslated entry
            if entry.translated() and entry.msgid != entry.msgstr:
                try:
                    Entry.get(msgid=entry.msgid, msgstr=entry.msgstr)
                except DoesNotExist:
                    Entry(
                        msgid=entry.msgid,
                        msgstr=entry.msgstr,
                        id_lang="en",
                        str_lang="fr",
                        crawl_timestamp=datetime.utcnow().timestamp(),
                        source_url=file.html_url,
                        license="CC0",
                    ).save()
                    count += 1
    return f"Successfully added/updated {count} entries."
