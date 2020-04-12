# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:04:10 2020

@author: Ayush
"""

from youtube_transcript_api import YouTubeTranscriptApi

text = YouTubeTranscriptApi.get_transcript('jNQXAC9IVRw')
for x in range(len(text)):
  print(text[x]['text'], end='\n')