#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import vlc

class Tools ():

    def __init__(self):
        file = open("playlist.m3u8", "w")
        file.write("#EXTM3U\n\n")
        file.close()

        file = open("./log/channelsoff.md", "w")
        file.write("# Canais Offline\n\n")
        file.write("| Canal | Motivo |\n")
        file.write("| ----- | ------ |\n")
        file.close()
        
        #define VLC instance
        self.instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--no-xlib', '--vout=dummy', '--verbose=-1')

        #Define VLC player
        self.player = self.instance.media_player_new()
        self.list_player =  self.instance.media_list_player_new()
        

    def checkChannel ( self, connection ):
        #Define VLC media
        media = self.instance.media_new(connection)
        media_list = self.instance.media_list_new([connection])

        #Set player media
        self.player.set_media(media)
        
        self.list_player.set_media_player(self.player)
        self.list_player.set_media_list(media_list)

        #Play the media
        self.list_player.play()

        #Sleep for 10 sec for VLC to complete retries.
        time.sleep(7)
        #Get current state.
        state = str(self.list_player.get_state())

        self.list_player.stop()
        return state

    def addChannelPlaylist( self, groupTitle, tvgId, tvgName, tvgLogo, urlTvg, shift, tvgLanguage, tvgCountry, channelName, url ):
        file = open("playlist.m3u8", "a")
        file.write('''#EXTINF:0 group-title="''' + groupTitle + '''" tvg-id="''' + tvgId + '''" tvg-name="''' + tvgName + '''" tvg-logo="''' + tvgLogo + '''" url-tvg="''' + urlTvg + '''" shift="''' + shift + '''" tvg-language="''' + tvgLanguage + '''" audio-track="por" shift="-3" aspect-ratio="16:9" subtitles="por" tvg-country="''' + tvgCountry + '''" size="Medium" background="#000000", ''' + channelName)
        file.write("\n")
        file.write(url)
        file.write("\n")
        file.close()

    def addChannelListOffline( self, channelName ):
        file = open("./log/channelsoff.md", "a")
        file.write("| ")
        file.write(channelName + " | ")
        file.write("Link desatualizado |")
        file.write("\n")
        file.close()

    def addChannelListMissing( self, channelName ):
        file = open("./log/channelsoff.md", "a")
        file.write("| ")
        file.write(channelName + " | ")
        file.write("Link faltando |")
        file.write("\n")
        file.close()

    def createReadMe( self, numChannels, data ):
        file = open("README.md", "w", encoding="utf-8")
        file.write('''<h1 align="center">FTA-IPTV-Brasil 📺</h1>\n''')
        file.write('''<p align="center">\n''')
        file.write('''<img alt="Última atualização" src="https://img.shields.io/badge/%C3%9Altima_atualiza%C3%A7%C3%A3o-'''+ data + '''-blue.svg" target="_blank" />\n''')
        file.write('''<img alt="Canais" src="https://img.shields.io/badge/Canais-'''+ numChannels +'''-success" target="_blank" />\n''')
        file.write('''<img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-yellow.svg" target="_blank" />\n''')
        file.write('''</p>\n''')
        file.write('''\n''')
        file.write('''> Somente serão adicionadas emissoras gratuitas de sinal aberto. Caso encontre alguma emissora que não se enquadre nesse quesito dentro do banco de dados, comunique o autor.\n''')
        file.write('''\n''')
        file.write('''Este projeto tem em vista montar um banco de dados com os canais disponíveis no Brasil de forma gratuita, via FTA (free-to-air), que se encontram na internet, com o objetivo de dinfundir o conhecimento sobre IPTV e o acesso a informação.\n''')
        file.write('''\n''')
        file.write('''Além disso possui um sistema de verificação da validade do link cadastrado,  através do VLC, que pode ser visto em `main.py`, que gera a lista `playlist.m3u8`, contendo apenas canais em funcionamento.\n''')
        file.write('''\n''')
        file.write('''```sh\n''')
        file.write('''https://raw.githubusercontent.com/joaoguidugli/FTA-IPTV-Brasil/master/playlist.m3u8\n''')
        file.write('''```\n''')
        file.write('''\n''')
        file.write('''## ✅ Funcionalidades\n''')
        file.write('''\n''')
        file.write('''- [x] Cadastro de sistema de log\n''')
        file.write('''- [x] Geração automática do README com número de canais disponíveis\n''')
        file.write('''- [x] Alteração no main.py para melhor codificação\n''')
        file.write('''- [ ] Cadastro dos canais disponíveis por via terrestre, descritos no [Portal BSD](https://www.portalbsd.com.br/)\n''')
        file.write('''- [ ] Configuração do EPG e das logos\n''')
        file.write('''- [ ] ...\n''')
        file.write('''- [ ] Cadastrar todos os canais disponíveis em FTA\n''')
        file.write('''\n''')
        file.write('''## 📝 Licença\n''')
        file.write('''\n''')
        file.write('''Copyright © 2020 [João Guidugli](https://github.com/joaoguidugli).<br/>\n''')
        file.write('''This project is [MIT](https://github.com/joaoguidugli/FTA-IPTV-Brasil/blob/master/LICENSE) licensed.<br/>\n''')
        file.write('''\n''')
        file.write('''<sub>Os logotipos, marcas, símbolos, nomes e URLs citadas neste projeto pertencem ao indivíduo que o produziu ou a empresa que o publicou.</sub><br/>\n''')
        file.write('''<sub>A utilização e citações para fins ilustrativos, informativos e educativos, não constitui ofensa aos direitos autorais.</sub><br/>\n''')
        file.write('''<sub>[LEI Nº 9.610 DE 1998](http://www.planalto.gov.br/ccivil_03/Leis/L9610.htm) • [Inciso XIV do Artigo 5 da Constituição Federal](https://presrepublica.jusbrasil.com.br/legislacao/91972/constituicao-da-republica-federativa-do-brasil-1988#art-5--inc-XIV)</sub>\n''')
        file.write('''\n''')
        file.close()