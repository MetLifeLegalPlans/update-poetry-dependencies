import os
import sys
from glob import glob

ws_env = os.environ.get("GITHUB_WORKSPACE")

print(ws_env)

os.chdir(ws_env)
print(glob("*"))

print(sys.argv)
