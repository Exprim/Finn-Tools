from lxml import html
import requests
import time
import datetime

print("Starter med a scrape finn.no...")

today = datetime.date.today()

page = requests.get('http://skse.silverlock.org/')
tree = html.fromstring(page.content)

# Lager en liste av priser
# Vi leser fra CSS stylesheetet / classen den er i

tittel = tree.xpath('//*[@class="t4 word-break mhn result-item-heading"]/text()')

print tittel.lower()

text_file = open("Output.txt", "w")
text_file.write("AN1: %s" % tittel.lower())

print("Finished..")
