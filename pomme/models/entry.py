from playhouse.sqlite_ext import FTS5Model
from playhouse.sqlite_ext import SearchField

from pomme import pomme_db


class Entry(FTS5Model):
    msgid = SearchField()
    msgstr = SearchField()
    id_lang = SearchField()
    str_lang = SearchField()
    crawl_timestamp = SearchField(unindexed=True)
    source_url = SearchField(unindexed=True)
    license = SearchField(unindexed=True)

    class Meta:
        database = pomme_db


if not Entry.table_exists():
    Entry.create_table()
