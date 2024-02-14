import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json(open("test.json", "r"))

df.set_index("AAPL", inplace=True)

df.head()
