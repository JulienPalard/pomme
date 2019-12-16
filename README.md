# TUW: Traduit Un Word

To run it, use the following scripts, in that precise order:

- `fetch.py`: To crawl github for `po` files.
- `po_to_json.py github.com` to parse and aggregate po files.
- `index.py` to create an index from the previous aggregate.
- `FLASK_APP=search flask run` to run the service.

Then you can query the service like this:

```
$ curl -s http://localhost:8000/search/?q=socket | json_pp | head
{
   "\n%s: -w option cannot use a relative socket directory specification\n" : {
      "\n%s : l'option -w ne peut pas utiliser un chemin relatif vers le répertoire de\nla socket\n" : {
         "seen" : 1,
         "sources" : {
            "github.com/woonhak/postgresql-directio/src/bin/pg_ctl/po/fr.po" : 1
         }
      },
   ...
```
