import json, urllib.request, urllib.parse, urllib.error

def loadEmbedCode(url):
    serviceUrl = "http://noembed.com/embed"
    response = urllib.request.urlopen(serviceUrl, urllib.parse.urlencode({'url': url}))
    data = json.load(response)
    if "error" in data:
        return None
    return data.get("html")
