**Random betterlockscreen**

Quick hack to set random image for the lock screen with a helper script and crontab.
In order to make this a bit more useful I'd need to add a YAML config parser.

**Installation**

I've set it up with a crontab for my local user:

```
*/30 * * * * /usr/bin/python3 ~/bin/betterlockscreen_random.py
```

Systemd timers could also be an appropriate setup.
