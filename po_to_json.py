#!/usr/bin/env python3

import argparse
from pathlib import Path
from collections import Counter
import json

import polib


def parse_args():
    parser = argparse.ArgumentParser(description="Find and merge po files by lang")
    parser.add_argument("directory", help="Root directory to search for", type=Path)
    return parser.parse_args()


def main():
    args = parse_args()
    translations = {}
    for po_path in args.directory.glob("**/*.po"):
        try:
            po_file = polib.pofile(po_path)
        except (OSError, UnicodeDecodeError) as err:
            print(err)
            continue
        language = po_file.metadata.get("Language", po_path.stem)
        for entry in po_file:
            if not entry.msgstr:
                continue
            translation = translations.setdefault(entry.msgid, {}).setdefault(
                language, {}
            )
            msgstr = translation.setdefault(
                entry.msgstr, {"sources": Counter(), "seen": 0}
            )
            msgstr["sources"][str(po_path)] += 1
            msgstr["seen"] += 1
    with open("translations.json", "w") as translations_file:
        json.dump(translations, translations_file, indent=4)


if __name__ == "__main__":
    main()
