# coding=utf-8
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
