import os
import sys
import glob
import toml


def cli():
    ws_env = os.environ.get("GITHUB_WORKSPACE")
    print(os.getcwd())
    print(glob.glob("*"))
    os.chdir(ws_env)

    # Shell script argument passing conventions upset me
    wants_latest = sys.argv[-1] == "true"

    print(wants_latest)
