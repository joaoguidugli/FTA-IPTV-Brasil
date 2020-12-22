#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class Toools ():

    def __init__(self):
        file = open("playlist.m3u8", "w")
        file.write("#EXTM3U\n\n")
        file.close()

    def addChannelPlaylist( self, groupTitle, tvgId, tvgName, tvgLogo, urlTvg, shift, tvgLanguage, tvgCountry, channelName, url ):
        file = open("playlist.m3u8", "a")
        file.write('''#EXTINF:0 group-title="''' + groupTitle + '''" tvg-id="''' + tvgId + '''" tvg-name="''' + tvgName + '''" tvg-logo="''' + tvgLogo + '''" url-tvg="''' + urlTvg + '''" shift="''' + shift + '''" tvg-language="''' + tvgLanguage + '''" audio-track="por" shift="-3" aspect-ratio="16:9" subtitles="por" tvg-country="''' + tvgCountry + '''" size="Medium" background="#000000", ''' + channelName)
        file.write("\n")
        file.write(url)
        file.write("\n")
        file.close()
