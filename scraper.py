
import scraperwiki
import lxml.html
html = scraperwiki.scrape("https://www.whatdotheyknow.com/body/decc")
root = lxml.html.fromstring(html)
tds = root.cssselect("td")
for td in tds:
  indexno = indexno + 1
  record = {'td' : td.text, "index" :indexno}
  scraperwiki.sqlite.save(["index"], record)
