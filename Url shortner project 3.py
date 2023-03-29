pip install pyshorteners
import pyshorteners

url=input("Hey please enter the URL:")

def shortenurl(url):
    s=pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shortenurl(url)
