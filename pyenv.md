### Pyenv Notes
* Lets you change global Python version on per-user basis
* Support for pyper-project Python versions
* Override Python version with environment variable
* Test across multiple python versions with Tox


To install pyenv you require some OS-specific dependencies. These are needed as pyenv installs Python by building from source. 
For ubuntu/debian:
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
To know required OS dependencies: https://github.com/pyenv/pyenv/wiki#suggested-build-environment
then can install pyenv
curl https://pyenv.run | bash

# See all available python installations.
pyenv install --list
# Install some python versions.
pyenv install  3.7.5
# See all python installations that you have installed.
pyenv versions

pyenv allows to manage python versions at global/local level
# Set the default/global from one of the python versions.
pyenv global 3.8.0
# In the current directory, set the python version. This creates the file .python-version.
pyenv local 2.7.17

pyenv captures Python commands using executables injected into your PATH. Then it determines which Python version you need to use, and passes the commands to the correct Python installation.

pyenv versions
  system
* 3.7.10 (set by /home/<username>/.pyenv/version)
  3.8.7
  3.9.2
Change the global version will not affect your system version. The system version corresponds to the version used by your OS to accomplish specific tasks or run background processes that depend on this specific Python version. Do not switch the system version to another one or you may face several issues with your OS! This version is usually updated along with your OS. The global version is just the version that pyenv will use to execute your Python commands / programs globally.

# Explicitly activate pyenv version
pyenv shell 3.8.6


Restart bash to get pyenv settings
pyenv versions
python -V
pyenv which python 
pyenv shell 3.8.6
pyenv virtualenv 3.6.8 .bayesian-venv --> create virtual enviro

# pyenv shell should activate pythonversion for terminal , but doesn't always work
[pth] = pyenv which python # after setting python version
poetry env use [pth]