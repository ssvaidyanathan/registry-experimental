[![Go Actions Status](https://github.com/apigee/registry-experimental/workflows/Go/badge.svg)](https://github.com/apigee/registry-experimental/actions)

# Registry Experiments

The [Apigee Registry API](https://github.com/apigee/registry) allows teams to
upload and share machine-readable descriptions of APIs that are in use and
development.

This repository holds experimental code that builds on the Registry API: new
projects, suspended projects, and work that might be useful in future projects.

### registry-experimental

[cmd/registry-experimental](cmd/registry-experimental) contains a command-line
tool that is structurally identical to the registry tool but containing
experimental capabilities, some of which might eventually be migrated to the
registry tool.

### Running the registry-graphql proxy

[cmd/registry-graphql](cmd/registry-graphql) contains a simple proxy that
provides a read-only GraphQL interface to the Registry API. It can be run with
a local or remote `registry-server`.

## License

This software is licensed under the Apache License, Version 2.0. See
[LICENSE](LICENSE) for the full license text.

## Disclaimer

This is not an official Google product. Issues filed on Github are not subject
to service level agreements (SLAs) and responses should be assumed to be on an
ad-hoc volunteer basis.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING](CONTRIBUTING.md) for notes
on how to contribute to this project.
