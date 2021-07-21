# Update poetry dependencies

This action takes the `pyproject.toml` file in the root of the repository and updates all dependencies within their semver constraints.

If the `latest` flag is specified, it also updates the semver constraints.

## Inputs

## `latest`

Whether the semver constraints should be pushed to the latest stable release. Default `false`.
