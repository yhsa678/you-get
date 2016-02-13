#!/usr/bin/env python

__all__ = ['gogoup_download']

import json
import random
import xml.etree.ElementTree as ET
import base64, hashlib, urllib, time, re
import requests
import pyCookieCheat
from .letv import letvcloud_download_by_vu

from ..common import *

def gogoup_download(url, output_dir='.', merge=True, info_only=False ,**kwargs):
    if re.match(r'http:\/\/www\.gogoup\.com\/play\?festId=\d+', url):
        cookies = pyCookieCheat.chrome_cookies(url)
        sess = requests.Session()
        video_page = str(sess.get(url, cookies = cookies).content)
        # Get uu, vu
        uu = re.search('\"uu\":"[a-f0-9]+"', video_page).group().split('"')[-2]
        vu = re.search('\"vu\":"[a-f0-9]+"', video_page).group().split('"')[-2]
        print('Got vu: %s, uu: %s' % (vu, uu))
        title = "gogoup-%s" % vu
        letvcloud_download_by_vu(vu, uu, title=title, output_dir=output_dir, merge=merge, info_only=info_only)
    else:
        print('The page url is not supported. URL: %s' % url)

site_info = "gogoup.com"
download = gogoup_download
download_playlist = playlist_not_supported('gogoup')
