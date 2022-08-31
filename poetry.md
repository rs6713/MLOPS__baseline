poetry is a packaging and dependency manager. It resolves your library dependencies, and can build and publish your project to be distributed on your private pypi repository

The main file of your poetry project is the pyproject.toml file. Define the requirements, the dev-requirements and project metadata in this file. poetry uses the .toml file to resolve the dependencies of your defined requirements, and creates the poetry.lock file. Then poetry creates a virtual environment and installs everything from the .lock file.

Some alternatives to poetry for virtual environments are virtualenv, conda, venv

# Install poetry via curl
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# Add poetry to your shell
export PATH="$HOME/.poetry/bin:$PATH"

# For tab completion in your shell, see the documentation
poetry help completions

# by default poetry virtual environment create, stored outside of project
# Configure poetry to create virtual environments inside the project's root directory
poetry creates an environment on a global system path (.cache/ by default). This separation of concerns allows keeping your project away from dependency source code.
poetry config virtualenvs.in-project true

# Create a new project, and directory
poetry new hugos-ds-poetry-demo
poetry add pandas
# Specify some dev libraries
poetry add --dev black flake8

With the above commands, I have created a pyproject.toml file as well as a poetry.lock file. poetry has installed the virtual environment for this project in hugos-ds-poetry-demo/.venv. 

# Run the script within your virtual environment, using the 'run'-command.
poetry run python hugos_ds_poetry_demo/example.py

# Spawn a shell within your virtual environment.
poetry shell

# Try running the script again, after having spawned the shell within your virtual environment.
python hugos_ds_poetry_demo/example.py

# In pre-existing project with no virtualenv
poetry init

[tool.poetry.dependencies] The version of Python we want the project to use is defined here as well. In our case python = "^3.8" specifies the minimum version required to run our app. Here this is Python 3.8 and this has been based on the version of our local version defined with pyenv.

if a poetry.lock file is already present, the version numbers defined in it take precedence over what is defined in the pyproject.toml.  you should commit the poetry.lock file to your project repository so that all collaborators working on the project use the same versions of dependencies.

poetry shell
activate the environment
command creates a child process that inherits from the parent Shell but will not alter its environment. It encapsulates and restrict any modifications you will perform to your project environment.

source $HOME/.poetry/env
poetry env use 3.8.6


# Handling changing python versions
Whenever you change dependencies by hand in your pyproject.toml you have to take care of these points:

Run poetry lock afterwards or remove the poetry.lock file to force recreation of it. The reasons for this is, that poetry install takes the poetry.lock as input if can find one and not the pyproject.toml.

If you change the python version and uses in-project virtualenv, remove the .venv before running poetry install. poetry doesn't change the python version of a venv once it is created, because it uses the python version itself to create the virtualenv.