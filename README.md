# Test framework (UI) | Playwright

## Install Poetry

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

## Install requirements

```shell
poetry install --no-root
poetry run playwright install --with-deps
```

## Create `.env` file

To get started with the project, you need to create a `.env` file in the root of the project directory. This file will
store sensitive environment variables such as test framework's settings.

### Step-by-Step Guide:

#### 1. Create a .env File:

In your project root directory, create a file named .env.

```shell
touch .env
```

#### 2. Add the Required Variables:

Copy and paste the following environment variables into the `.env` file:

```shell
TEST_USER.EMAIL=user@example.ru
TEST_USER.USERNAME=username
TEST_USER.PASSWORD=password

TEST_DATA.IMAGE_PNG_FILE=./testdata/image.png

HEADLESS=True

BROWSERS="webkit,chromium"
```

## Run UI-tests

```shell
# --numprocesses launchs tests in parallel in 2 processes
poetry run pytest --numprocesses 2
```
