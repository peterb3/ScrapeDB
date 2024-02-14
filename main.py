from scrape import Scrape
import json

elements_to_scrape = {}

f = open("scrape.json")
data = f.read()
f.close()
elements_to_scrape = json.loads(data)

stock_list = ["AAPL", "TSLA", "GOOGL", "NFLX", "NVDA"]
compiled_dict = {}

for stock in stock_list:
    stock_info = Scrape(stock, elements_to_scrape)
    compiled_dict[stock] = stock_info.summary()

with open("test.json", "w") as outfile:
    json.dump(compiled_dict, outfile)
