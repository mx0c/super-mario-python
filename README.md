# Super Mario Implementation in Python

This is inspired by Meth-Meth-Method's [super mario game](https://github.com/meth-meth-method/super-mario/)

## Development

### Running Locally

To run the application locally, use Poetry to install the dependencies and run the application.
This way we can ensure that everyone is using the same version python version and dependencies.

```bash
pip3 install poetry
poetry install
poetry run python main.py
```

### Linting

Linting is done using pre-commit hooks. Before committing your code, linting and formatting checks will run automatically. pre-commit will inform you of the problems that need to be fixed before you can commit your code.

You can also run the pre-commit checks manually using the following command:

Only first time:
```bash
pip3 install pre-commit
pre-commit install
```

Then:
```bash
pre-commit run --all-files
```

## Building

### Standalone windows build

* $ pip install py2exe
* $ python compile.py py2exe

### Controls

* Left: Move left
* Right: Move right
* Space: Jump
* Shift: Boost
* Left/Right Mouseclick: secret

## Current state:
![Alt text](img/pics.png "current state")

## Dependencies
* pygame
* scipy

## Contribution

If you have any Improvements/Ideas/Refactors feel free to contact me or make a Pull Request.
The code needs still alot of refactoring as it is right now, so I appreciate any kind of Contribution.

Ensure that all github actions are passing in your pull request before asking for a review.
