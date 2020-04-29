import os.path
import pandas as pd
import requests
import zipfile
import matplotlib.pyplot as plt

filename = 'FOLK1A.csv'

if os.path.isfile(filename):
    print("File exist")
else:
    print("File not exist")
    print("Fetching csv from api.statbank.dk")
    url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F%2CTOT&Tid=*'
    response = requests.get(url)  # , params={'downloadformat': 'csv'}

    print("Headers:", response.headers)

    # get the filename
    fname = response.headers['content-disposition'].split('=')[1]
    filename = fname
    print("Filename:", fname)

    # write content to file (zip file writing bytes)
    if response.ok:  # status_code == 200:
        with open(fname, 'wb') as f:
            f.write(response.content)
    print('-----------------')
    print('Downloaded {}'.format(fname))


try:
    # Read CSV
    data = pd.read_csv(
        filename, sep=";")
    print("__________________\nInside Try Statement:\n")
    # print("Type:", type(data))
    print("Columns:", data.columns)
    # print("Iloc[0]:", data.iloc[3, :])
    fraskilt = data.loc[data.CIVILSTAND ==
                        "Fraskilt"]["INDHOLD"].values.tolist()
    print("Fraskilte\n", fraskilt)
    total = data.loc[data.CIVILSTAND == "I alt"]["INDHOLD"].values.tolist()
    print("I alt\n", total)
    tid = data.loc[data.CIVILSTAND == "I alt"]["TID"].values.tolist()
    print("\nTid:\n", tid)
    # samlet = pd.merge(fraskilt, total, how="inner", on="TID",
    #                   suffixes=('_fraskilt', '_total'))
    # print("samlet:\n", samlet)
    percentages = [skilt/tot*100 for skilt, tot in zip(fraskilt, total)]
    print("percentages\n", percentages)

    # Time to plot
    plt.figure()

    x = tid
    y = percentages
    plt.plot(x, y, linewidth=5)

    # Set chart title and label axes.
    plt.title("Skilte over tid i Danmark", fontsize=24)
    plt.xlabel("Tid", fontsize=14)
    plt.ylabel("% af totalbefolkningen er der skilte", fontsize=14)
    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)
    # Save plot as .png and show it
    plt.savefig('skilte.png', bbox_inches='tight')
    plt.show()

except:
    print("File not found")
