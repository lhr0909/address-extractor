# address-extractor
A service that extracts addresses. It first tries to find and parse the address from a blob of text and then uses libpostal to expand the address.

# Install & Run

## Prerequisites

- [pyenv](https://github.com/pyenv/pyenv-installer)
- poetry `pip install poetry`

## Local Run / Develop

To run / develop locally, first follow the instruction to [install libpostal](https://github.com/openvenues/libpostal#installation-maclinux).

[Alternative instruction from pypostal](https://github.com/openvenues/pypostal#installation)

Once libpostal is installed, run the following command to install dependencies:

```shell
poetry install
```

Run the following command to run the service:

```shell
make serve
```

visit https://localhost:7000/docs to check the API documentation in a Swagger UI.

## Docker Run

We have a Dockerfile included, which you could build yourself. There also will be a Docker Hub version available. A docker-compose sample will also be provided to see how it runs

# License

[MIT](./LICENSE)
