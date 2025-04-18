# Introduction

## Project Setup

- This project is using [uv](https://docs.astral.sh/uv/pip/environments/)

```sh
# Activate the source
source .venv/bin/activate

# install packages
uv pip install -r requirements.txt
```

## About torch with cuda

I have a cuda 12 installed in my machine so this project is generated using

```sh
uv pip install torch --index-url https://download.pytorch.org/whl/cu121
```

**Check your cuda version** and update torch accordingly

```sh
nvcc --version
```
