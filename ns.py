#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
import json

headers = {
  'Content-Type': 'application/json'
}

url_ns = "https://your_url.herokuapp.com/api/v1/entries.json?find[date][$gt]=20210210&count=1"

response = requests.request("GET", url_ns, headers=headers)

glucose = response.json()[0]['sgv']

url = "http://192.168.1.110:7000/api/v3/notify"

if glucose > 160:
	payload='{{"name":"CGMNotification", "force":true, "scrollSpeed": 80, "icon":"CGM", "moveIcon":true, "repeatIcon":true, "repeat":2, "multiColorText":[{{
"text":"Current glucose ","color":[80,110,255]}},{{"text":"{glucose} ","color":[255,0,0]}}, {{"text":"[{delta:.1f}] {direction}","color":[80,110,255]}}], "color
":[80,110,255]}}'

if glucose < 70:
        payload='{{"name":"CGMNotification", "force":true, "scrollSpeed": 80, "icon":"CGM", "moveIcon":true, "repeatIcon":true, "repeat":2, "multiColorText":[{{
"text":"Current glucose ","color":[80,110,255]}},{{"text":"{glucose} ","color":[247, 133, 31]}}, {{"text":"[{delta:.1f}] {direction}","color":[80,110,255]}}], "
color":[80,110,255]}}'

if glucose >= 70 and glucose <= 160:
        payload='{{"name":"CGMNotification", "force":true, "scrollSpeed": 80, "icon":"CGM", "moveIcon":true, "repeatIcon":true, "repeat":2, "multiColorText":[{{
"text":"Current glucose ","color":[80,110,255]}},{{"text":"{glucose} ","color":[0,255,0]}}, {{"text":"[{delta:.1f}] {direction}","color":[80,110,255]}}], "color
":[80,110,255]}}'

payload = payload.format(glucose=glucose, delta=round(response.json()[0]['delta'],1), direction=response.json()[0]['direction'])

response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))
