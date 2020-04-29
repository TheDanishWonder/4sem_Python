import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

# Wait, how is this any different from 5c? Its barely a different task.

# KØN;ALDER;CIVILSTAND;OMRÅDE;TID;INDHOLD
# I alt;I alt;Ugift;Hele landet;2020K1;2844060
# I alt;I alt;Gift/separeret;Hele landet;2020K1;2146017

# Show a bar chart of 'Married' and 'Never Married'
# for all ages in DK (Hint: 2 bars of different color)

url = "https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&K%C3%98N=TOT&ALDER=IALT&CIVILSTAND=U%2CG&OMR%C3%85DE=000&Tid=2020K1"
data = pd.read_csv(url, sep=';')
print(data)
gift = data.loc[data.CIVILSTAND == "Gift/separeret"]["INDHOLD"].values.tolist()
ugift = data.loc[data.CIVILSTAND == "Ugift"]["INDHOLD"].values.tolist()
print("gift:", gift)
print("ugift:", ugift)
years = (2008, 2020)

indices = np.arange(len(gift))
width = 0.1

fig, ax = plt.subplots()
giftBar = ax.bar(indices, gift, width, color="r")
ugiftBar = ax.bar(indices+width, ugift, width, color="b")

ax.set_ylabel('People')
ax.set_title('Marital Status in Denmark, 2008, 2020')
ax.set_xticks(indices + width / 2)
ax.set_xticklabels(years)

ax.legend((giftBar[0], ugiftBar[0]),
          ('Gift', 'Ugift'))

plt.show()
