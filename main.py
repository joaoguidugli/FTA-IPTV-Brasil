#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from utils.tools import Tools
from datetime import datetime


obj = Tools()
numChannels = 0

entries = os.listdir('./channels')
for entry in entries:

    test = open('./channels/' + entry,)
    data = json.load(test) 
    connection = data['DATA']['url']
    name = data['INFO']['channel-name']

    print('[VERIFICANDO CANAL] ' + name)

    if not connection:
        obj.addChannelListOffline(
            data['INFO']['channel-name'],
            entry
        )
        print('Canal Offline')
    else:
        state = obj.checkChannel(connection)
        if state == "State.Ended" or state == "State.Error":
            obj.addChannelListOffline(
                data['INFO']['channel-name'],
                entry
            )
            print('Canal Offline')
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
            print('Canal Online')
            numChannels += 1




now = datetime.now()
data = (str(now.day) + "/" + str(now.month) + "/" + str(now.year))
obj.createReadMe(str(numChannels), data)