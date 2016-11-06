from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from bs4 import BeautifulSoup
from django.conf import settings
import urllib
import re
import wget

class RootUrl(models.Model):
    name = models.CharField(max_length=200)
    root_url = models.CharField(max_length=2000)
    start_date = models.DateTimeField(timezone.now())
    stop_date = models.DateTimeField(timezone.now())
    last_update_date = models.DateTimeField(timezone.now())
    
    def __str__(self):
        return self.name
        
    def fileExtract(self):
        urls = [self.root_url]
        visited = set()
        tags = ['track', 'audio', 'video', 'html', 'figure', 'object', 'img']
        while len(urls) > 0:
            try: 
                htmltext = urllib.urlopen(urls[0]).read()
            except:
                print urls[0]
            soup = BeautifulSoup(htmltext, "html.parser")
            urls.pop(0)
            for tag in tags:
                files = soup.findAll(tag)
                for file in files:
                    fileaddr = re.findall('.*src="(.*?)".*', str(file))[0]
                    visited.add(fileaddr)
        return visited
    
    def download(self, url):
        path = settings.STATIC_URL
        wget.download(url, out=path)

class ItemUrl(models.Model):
    item_url = models.ForeignKey(RootUrl, on_delete=models.CASCADE)
    item_content = models.CharField(max_length=2000)
    acquired_date = models.DateTimeField(editable=False)

    
    def __str__(self):
        return self.item_content
