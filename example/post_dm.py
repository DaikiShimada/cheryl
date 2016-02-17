#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheryl import CherylAPI

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
bot = CherylAPI(token=token, configfile='cheryl.json')
bot.post_direct_message_by("username", "message", ["attachment files' path"])
