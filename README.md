# goose
Dank chatbot interface for Waterloo's Open Data API!

### How it works, simplified
User input is recieved by Mr. Goose, which is then compared to key phrases to check for phrase similarity. If an input phrase is considered similar enough to a key phrase, an applicable response phrase is triggered and sent back to the user. If the input cannot be classified as a key phrase category, then a new response will be generated. On the case of the user input triggering an api command, the bot will fetch the appropriate data from the waterloo api and send the user a formated response with the aquired data.

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

### IDE
You can omit the Developer setup if you want to use an IDE

#### PyCharm IDE is recomended (makes life better)
https://www.jetbrains.com/pycharm/
