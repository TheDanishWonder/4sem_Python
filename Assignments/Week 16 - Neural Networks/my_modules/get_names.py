import pandas as pd
import os
base_path = os.path.dirname(__file__)
print(base_path)
names_series = pd.read_excel('/home/tha/ghub/4sem/python/2020s/unisex_navne.xls',header=None,names=['navne'])['navne']
names_list = list(names_series)
def get_names(ls):
    current = 0
    while(current < len(ls)):
        yield ls[current]
        current += 1

if __name__ == '__main__':
    for name in get_names(names_list):
        print(name)

