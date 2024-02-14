from scrape import Scrape
import json

elements_to_scrape = {}

f = open("scrape.json")
data = f.read()
f.close()
elements_to_scrape = json.loads(data)

s = Scrape("AAPL", elements_to_scrape)
print(s.summary())

# with open("test.json", "w") as outfile:
#     json.dump(elements_to_scrape, outfile)
