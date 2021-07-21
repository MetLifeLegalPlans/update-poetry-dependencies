import os
import sys
import subprocess
import toml
import shlex

IGNORED_PACKAGES = [
    # Ideally we should support the minimum version the package can
    "python",
    # These just do not play nice with dependency resolution on
    # modern versions of python
    "importlib-metadata",
    "importlib_metadata",
]


def latest_string(key, val):
    if isinstance(val, str):
        return f"{key}@latest"

    extras_str = ",".join(val["extras"])
    return f"{key}[{extras_str}]@latest"


def dep_str(coll):
    res = []

    for k, v in coll.items():
        if k in IGNORED_PACKAGES:
            continue

        res += [latest_string(k, v)]

    return shlex.join(res)


def cli():
    ws_env = os.environ.get("GITHUB_WORKSPACE")
    os.chdir(ws_env)

    # Shell script argument passing conventions upset me
    wants_latest = sys.argv[-1] == "true"

    subprocess.run("poetry update")

    if wants_latest:
        with open("pyproject.toml") as f:
            pyproject = toml.load(f)

        dependencies = pyproject["tool"]["poetry"]["dependencies"]
        dev_dependencies = pyproject["tool"]["poetry"]["dev_dependencies"]

        subprocess.run(f"poetry add {dep_str(dependencies)}")
        subprocess.run(f"poetry add --dev {dep_str(dev_dependencies)}")
