# Auto remove CDK dev environment

//TODO

## Description

//TODO

## Requirements

* [Nodejs](https://nodejs.org/en/)

## Use

For use this project in your local machine, just install npm dependencies:

```bash
npm install
```

To manually create a virtualenv on MacOS and Linux:

```bash
python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```bash
source .env/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```bash
pip3 install -r requirements.txt
```

## Pre-commit

A pre-commit configuration file is provided in this repo to perform some linterns, validations and so on in order to avoid commit code to the repo that later will fail in validations step in the build pipeline.

The first execution can be slower because of installation of dependencies. Further executions will use the pre-commit cache.

### Pre-commit requirements

In order to use pre-commit with all the hooks declared you need to install the following:

* [Pre-commit](https://pre-commit.com/#install)
* [Markdownlint](https://github.com/markdownlint/markdownlint) (also requires ruby)
* [Shellcheck](https://github.com/koalaman/shellcheck)
* [pylint](https://www.pylint.org/#install)

### Use pre-commit

Once you have all the requirements achieved, you have to install pre-commit in the local repository:

```bash
pre-commit install
```

And you can test it's working with the following:

```bash
➜ pre-commit run --all-files
Check for added large files..............................................Passed
Check for case conflicts.................................................Passed
Check that executables have shebangs.................(no files to check)Skipped
Check JSON...........................................(no files to check)Skipped
Check for merge conflicts................................................Passed
Trim Trailing Whitespace.................................................Passed
Don't commit to branch...................................................Passed
Tabs remover.............................................................Passed
Check markdown files.....................................................Passed
Test shell scripts with shellcheck...................(no files to check)Skipped
Yaml lintern.............................................................Passed
Python lintern...........................................................Passed
Python unit tests........................................................Passed
```
