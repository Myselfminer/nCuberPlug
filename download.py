import urllib2
def download(url):
    max_tries=11
    min_tries=1
    for i in range(min_tries ,max_tries):
        a=max_tries-i
        print("Downloading "+url+" with %s tries remaining"%a)
        #for i in [""]:
        try:
            urlobj=urllib2.urlopen(url)
            a=urlobj.read()
            print("Finished downloading of %s"%url)
            return a
        except:
            continue
