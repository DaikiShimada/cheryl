# Cheryl: easy slack posting direct message bot tool
## Requirements
- Python 2.x (checked Python 2.7.6)
- [slacker 0.9.0](https://github.com/os/slacker)
## How to use
Show a easy example.
```python
from cheryl import CherylAPI

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
bot = CherylAPI(token=token, configfile='cheryl.json')
bot.post_direct_message_by("username", "message", ["attachment files' path"])
```
Here, token parameter takes priority over configure file.
## Setting
You can make arrangements for nice bot.  
Setting cheryl, you can edit __cheryl.json__ file.  
```json
{
    "token": "xxxxx-xxxxxxxxx-xxxxxxxx-xxxxx",
    "name": "display name",
    "icon": "icon_image.jpg"
}
```
