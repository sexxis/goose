# goose
Dank chatbot interface for Waterloo's Open Data API!

Uses the textblob package for python 2.7, so make sure to have that installed :D
Also uses stringscore package to rate input string similarity to key phrases

# Developer setup

### Linux

Install virtualenv
```bash
$ sudo pip install virtualenv # make sure to install the one for python2
```
In project root, run the following to start virtualenv
```bash
$ virtualenv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt # Install the dependencies
$ python -m textblob.download_corpora
```
To start the interactive chat console, run the following in project root
```bash
$ ./scripts/start.sh
```
When you finish, run `deactivate` to exit virtualenv

#### PyCharm IDE is recomended (makes life better)
Download: https://www.jetbrains.com/pycharm/specials/pycharm/pycharm.html?&gclid=Cj0KEQjwouW9BRCN0ozIifTI6_cBEiQAD9gNsUWQ_sGy6IZ9sHIfGD53jGgCCD6fDgySWi100dK-ew0aAmw08P8HAQ&gclsrc=aw.ds.ds&dclid=CK-2oPyV1M4CFY1xAQodsSgJbg
