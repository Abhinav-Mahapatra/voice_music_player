# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:03:07 2020

@author: abhinav.mahapatra
"""
import urllib.request
import urllib.parse
import re
import pafy
import webbrowser

def play_link(url):
    video = pafy.new(url)
    best = video.getbest()
    if webbrowser.open(best.url):
        return 1
    else:
        return 0

def get_query(inp_str):
    inp_str = inp_str.replace(' ','+')
    query_string = urllib.parse.urlencode({"search_query" : inp_str})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string )
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    output = "http://www.youtube.com/watch?v=" + search_results[0]
    return output
