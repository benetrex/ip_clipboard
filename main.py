#!/usr/bin/env python
import requests
import pyperclip

resp = requests.get('https://ifconfig.me/ip')
if resp.status_code == 200:
    pyperclip.copy(resp.content.decode('utf-8'))
