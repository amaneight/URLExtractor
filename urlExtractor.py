#
# Title: URL extractor from Firefox broswser
#
# Author: Aman Sehgal
# Date: 19/8/2017
#

import json

# Open recovery.js
f = open(r"C:\Users\<user_name>\AppData\Roaming\Mozilla\Firefox\Profiles\<default - file>\sessionstore-backups\recovery.js", "r")
jdata = json.loads(f.read())
f.close()

#Open file to paste URL's of all tabs
f = open(r"C:\URLs.txt","w")
for win in jdata.get("windows"):
        for tab in win.get("tabs"):
            i = tab.get("index") - 1
            f.write(tab.get("entries")[i].get("url")+"\n")

f.close()
