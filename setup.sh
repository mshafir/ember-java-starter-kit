
## This script sets up the dev environment for this toolkit. 
## It assumes an ubuntu environment and that java8 jdk is already set up.

# set up python dependencies
curl https://bootstrap.pypa.io/get-pip.py -o .tmp/get-pip.py
sudo python .tmp/get-pip.py
sudo pip install urwid

# set up ember dependencies
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
nvm install node
source /home/user/.bashrc
npm install -g ember-cli
npm install -g bower

# set up postgres
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start

# if you need to you can clear the existing db for a fresh environment
# sudo -u postgres psql --command 'DROP DATABASE IF EXISTS "APP-DEV"'
sudo -u postgres psql --command 'CREATE DATABASE "APP-DEV"'
sudo -u postgres psql -d APP-DEV --command "CREATE USER admin WITH PASSWORD 'admin' SUPERUSER"

