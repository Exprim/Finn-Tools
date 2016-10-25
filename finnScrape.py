from lxml import html
import requests
import time
import datetime
import urllib2
import sys

# TODO:
# - Build C# Application. PYTHON = BACKEND C# UI = FRONTEND (PYTHON MUCH MORE FLEXIBLE)
#
#
#

print "Checking internet connection..."
def internet_on():
    try:
        response = urllib2.urlopen('http://google.com',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False
if internet_on() == False:
    print "You don't have internet available. Can't run this application w/out internet. Connect and retry."
    sys.exit("Terminating... ")
else:
    print "Internet: Good"

print("Starter med a scrape finn.no...")

today = datetime.date.today()

page = requests.get('http://m.finn.no/bap/forsale/search.html?search_type=SEARCH_ID_BAP_ALL&q=server')
tree = html.fromstring(page.content)

# Lager en liste av priser
# HUSK: Vi angriper classen, intet annet!Trenger ikke full xpath, bare class/text()
tittel = tree.xpath('//*[@class="t4 word-break mhn result-item-heading"]/text()')

# Åpner, skriver inn info, stenger - GAMMEL INFO VIL ALLTID BLI SKREVET OVER...!!!! (Dette må fikses)
text_file = open("Output.txt", "w",)
text_file.write("TIME: %s" % today)
text_file.write("\n")
text_file.write("Navn: %s" % tittel)
text_file.close()

print("Finished..")

## Prosesserer informasjonen vi har hentet

text_file = open("Output.txt", "r")
testRead = text_file.readlines()
print "Printing return info"
print testRead
