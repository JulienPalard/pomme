import os
import re
from time import sleep
from base64 import b64decode
from github import Github


path_blacklist = {"/venv/", "/.venv/", "/site-packages/"}
seen = set()

while True:
    try:
        g = Github(os.environ["GH_KEY"])
        for code in g.search_code(
            query='language:"Gettext Catalog" french fork:false', sort="indexed"
        ):
            if code.html_url in seen:
                break
            sleep(6)
            seen.add(code.html_url)
            local_path = re.sub(
                "/blob/[a-f0-9]*/", "/", code.html_url[len("https://") :]
            )
            if any(blacklist in local_path for blacklist in path_blacklist):
                print("- SKIPPING ", code.html_url)
                continue
            print("-", local_path)
            local_dir = os.path.dirname(local_path)
            os.makedirs(local_dir, exist_ok=True)
            with open(local_path, "wb") as codefile:
                codefile.write(b64decode(code.content.encode("ASCII")))
        print("zzzZZZ")
        sleep(60)
    except Exception as err:
        print(err)
        print("zzzZZZ" * 2)
        sleep(3600)
