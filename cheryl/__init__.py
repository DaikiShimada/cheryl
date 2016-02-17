#!/usr/bin/env python
# -*- coding: utf-8 -*-

from slacker import Slacker
import os.path
import json, codecs

from logging import getLogger,Formatter,StreamHandler,DEBUG
logger = getLogger()
formatter = Formatter(fmt='%(asctime)s %(message)s',datefmt='%Y/%m/%d %p %I:%M:%S,',)
handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.setLevel(DEBUG)
logger.addHandler(handler)

class SlackDMBot(object):
    _slack = None
    _users = None
    _channels = None

    def __init__(self, token):
        # init API object
        self._slack = Slacker(token)
        # get user:id dict
        response = self._slack.users.list()
        self._users = {usr['name']: usr['id'] for usr in response.body['members']}
        self._users_inv = {v:k for k, v in self._users.items()}
        # get channel:id dict
        response = self._slack.channels.list()
        self._channels = { channel['name']: channel['id'] for channel in response.body['channels'] if channel['is_member'] }
        self._channels_inv = {v:k for k, v in self._channels.items()}

    def post_direct_message(self, dst_usrname, text, attachments, **options):
        if dst_usrname not in self._users:
            logger.error('Error: dstination, ' + dst_usrname + ', is not in this team.')
            return

        dm = self._slack.im.open(self._users[dst_usrname]).body['channel']
        self._slack.chat.post_message(dm['id'], text, **options)
        logger.debug("[POST DM] [TO: " + dst_usrname + "] " + text + " (option=" + str(options) + ")")

        if attachments is not None:
            for att in attachments:
                self._slack.files.upload(att, channels=[dm['id']])
                logger.debug("[UPLOAD FILE] [TO: " + dst_usrname + "] " + att)

        self._slack.im.close(dm['id'])


class CherylAPI(SlackDMBot):
    _config = None

    def __init__(self, token=None, configfile="~/cheryl.config"):
        # reed config file
        with codecs.open(os.path.expanduser(configfile), 'r', 'utf-8') as f:
            self._config = json.load(f)
            
        tk = self._config['token'] if token is None else token
        super(CherylAPI, self).__init__(tk)

    def post_direct_message_by(self, dst_usrname, text, attachments=None):
        as_user = False
        username = self._config['name']
        icon_url = self._config['icon']
        self.post_direct_message(dst_usrname, text, attachments, as_user=as_user, username=username, icon_url=icon_url)
