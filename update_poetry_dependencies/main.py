import os
import sys
from glob import glob

from use_dir import use_dir

ws_env = os.environ.get("GITHUB_WORKSPACE")

print(ws_env)

with use_dir(ws_env):
    print(glob("*"))

print(sys.argv)
