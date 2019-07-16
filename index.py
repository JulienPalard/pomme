import json

with open("translations.json") as translations_files:
    translations = json.load(translations_files)

index = {}
for msgid in translations.keys():
    for word in msgid.split():
        index.setdefault(word.lower(), []).append(msgid)

with open("index.json", "w") as index_file:
    json.dump(index, index_file)
