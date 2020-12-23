#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import vlc
import time
import os
from utils.toools import Toools

entries = os.listdir('./channels')
ChannelsOnline = {}
ChannelsOffline = {}

obj = Toools()

#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--no-xlib', '--vout=dummy')

#Define VLC player
player=instance.media_player_new()

for entry in entries:

    test = open('./channels/' + entry,)
    data = json.load(test) 
    connection = data['DATA']['url']

    print(data['DATA']['url'])
    # thisdict[entry] = data['DATA']['url']

    #Define VLC media
    media=instance.media_new(connection)

    #Set player media
    player.set_media(media)

    #Play the media
    player.play()

    #Sleep for 10 sec for VLC to complete retries.
    time.sleep(5)
    #Get current state.
    state = str(player.get_state())

    #Find out if stream is working.
    if state == "State.Ended" or state == "State.Error":
        ChannelsOffline[entry] = connection
        obj.addChannelListOffline(
            data['INFO']['channel-name'],
            entry
        )
        player.stop()
    else:
        ChannelsOnline[entry] = connection
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
        player.stop()
    
