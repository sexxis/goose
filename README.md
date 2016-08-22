# goose
Dank chatbot interface for Waterloo's Open Data API!

Uses the textblob package for python 2.7, so make sure to have that installed :D
Also uses stringscore package to rate input string similarity to key phrases

# Developer setup

### Linux
1. Install pip
2. Install virtualenv
```bash
$ sudo pip install virtualenv # make sure to install the one for python2
```
3. In project root, run the following to start virtualenv
```bash
$ virtualenv venv
$ . ./venv/bin/activate
```
4. To start the interactive chat console, run the following in project root
```bash
$ ./scripts/start.sh
```
5. When you finish, run `deactivate` to exit virtualenv
