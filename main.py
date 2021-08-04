# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd  
from utils.tools import Tools
from datetime import datetime
# odfpy is required

obj = Tools()
numChannels = 0

planilha = pd.read_csv("channels.csv", encoding="utf-8")
planilha = planilha.fillna('')

for index, row in planilha.iterrows():

    connection = row['url']
    print('[VERIFICANDO CANAL] ' + row['channel-name'])

    if not connection:
        obj.addChannelListMissing(
            row['channel-name']
        )
        print('Canal Offline')
    else:
        state = obj.checkChannel(connection)
        if state == "State.Ended" or state == "State.Error":
            obj.addChannelListOffline(
                row['channel-name']
            )
            print('Canal Offline')
        else:
            obj.addChannelPlaylist(
                row['group-title'],
                row['tvg-id'],
                row['tvg-name'],
                row['tvg-logo'],
                row['url-tvg'],
                str(row['shift']),
                row['tvg-language'],
                row['tvg-country'],
                row['channel-name'],
                row['url']
            )
            print('Canal Online')
            numChannels += 1

now = datetime.now()
data = (str(now.day) + "/" + str(now.month) + "/" + str(now.year))
obj.createReadMe(str(numChannels), data)