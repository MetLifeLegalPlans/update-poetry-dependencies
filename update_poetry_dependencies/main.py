import os
import sys
import toml


def cli():
    ws_env = os.environ.get("GITHUB_WORKSPACE")
    os.chdir(ws_env)

    # Shell script argument passing conventions upset me
    wants_latest = sys.argv[-1] == "true"

    print(wants_latest)
