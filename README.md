# CodingLoveSlackBot

_The-must-install chat bot for Slack._

![Slack](https://a.slack-edge.com/272a/img/slack_growl_icon.png)

http://thecodinglove.com/

### >_ Version
0.0.1

### >_ Requirements
Python 2.7.10+

### >_ Create Slack bot user
Creating a new bot user is easy as a butterfly.
Just log in to your slack team in this browser, and [click here](https://my.slack.com/services/new/bot) to create a new bot user.

After you figured out the perfect name of your bot (mine is _codinglovebot_), you will see some useful info about this bot. The most important is the token. You have to add this token, and the name of your bot to the system environment variables, so let's do it:

```sh
export SLACK_BOT_TOKEN={your_slack_bot_token}
export SLACK_BOT_NAME={your_slack_name}
```

### >_ Installation
After You clone this repo:

(OPTIONAL)
You can run this in [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
Just type the followings:
```sh
$ virtualenv venv
$ . venv/bin/activate
```

Install requirements by running this command:
```sh
pip install -r requirements.txt
```

Find out the _user_id_ of your bot:
```sh
python get_bot_id.py
```

Add this ID to the system environment:
```sh
export SLACK_BOT_ID={your_slack_bot_id}
```

### >_ Usage
All set, let run it!!
```sh
python codinglovebot.py
```
If you can not see any error, and printed out something like this: 'codinglove connected and running!' you are done.

***Now You can try this on Your Slack by sending a private message to the bot, something like this:***

--> @codinglovebot: send me a random post


If there is any issue, error, typo or anything, pls let me know, and I will fix it as soon as possible. 


License
----

MIT


**Free Software, Hell Yeah!**

_szilagyiabo_
