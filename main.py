# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:30:24 2020

@author: abhinav.mahapatra
"""

from record import record
from play import get_query, play_link

try:
    # initializing the recognition
    recorder = record()
    usr_inp = recorder.recog_speech()

    # Getting the query for the song
    if play_link(get_query(usr_inp)):
        print('Enjoy the karaoke')
    else:
        print('Some error has occurred.')

except Exception as e:
    print(e)