#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from utils.tools import Tools


obj = Tools()
numChannels = 0

entries = os.listdir('./channels')
for entry in entries:

    test = open('./channels/' + entry,)
    data = json.load(test) 
    connection = data['DATA']['url']

    state = obj.checkChannel(connection)
    if state == "State.Ended" or state == "State.Error":
        obj.addChannelListOffline(
            data['INFO']['channel-name'],
            entry
        )
    else:
        obj.addChannelPlaylist(
            data['EPG']['group-title'],
            data['EPG']['tvg-id'],
            data['EPG']['tvg-name'],
            data['EPG']['tvg-logo'],
            data['EPG']['url-tvg'],
            data['EPG']['shift'],
            data['EPG']['tvg-language'],
            data['EPG']['tvg-country'],
            data['INFO']['channel-name'],
            data['DATA']['url']
        )
        numChannels += 1

obj.createReadMe(str(numChannels))