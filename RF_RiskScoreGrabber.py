import urllib.request
import json

token = '' #INSERT YOUR TOKEN HERE
CVE_Collection = [line.rstrip('\n') for line in open('cve')]
length = len(CVE_Collection)

for i in range (0, length):
    cve = CVE_Collection[i]
    url = "https://api.recordedfuture.com/v2/vulnerability/"+cve+"?fields=risk&metadata=false"
    req = urllib.request.Request(url, None, {'X-RFToken': token})   
    with urllib.request.urlopen(req) as res:
        raw = (res.read())
        parse = json.loads(raw)
        score = int((parse['data']['risk']['score']))
                   
        if (score >= 90):
            with open('very_critical.txt','a') as dfile:
                dfile.write(cve +',')
        elif (80<=score<=89):
            with open('critical.txt','a') as zfile:
                zfile.write(cve +',')
        elif (65<=score<= 79):   
            with open('high.txt','a') as afile:
                afile.write(cve + ',')
        elif (25<=score<=64):
                        with open('medium.txt','a') as bfile:
                                bfile.write(cve + ',')
        elif (5<=score<=24):
                        with open('low.txt','a') as cfile:
                                cfile.write(cve + ',')
        else:
                        with open('informational.txt','a') as afile:
                                afile.write(cve + ',')
