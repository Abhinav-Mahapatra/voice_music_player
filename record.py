# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:14:47 2020

@author: abhinav.mahapatra
"""

import speech_recognition as sr

class record():
    def __init__(self):
        # Initializing
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def recog_speech(self):
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print('Say something')
            self.audio = self.r.listen(source)
            self.output = self.r.recognize_google(self.audio)
            print(self.output)
        return self.output
