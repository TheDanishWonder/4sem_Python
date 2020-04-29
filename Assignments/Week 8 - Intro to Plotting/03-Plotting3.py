import matplotlib.pyplot as plt

data = {'apple': 10,'banana':2,'citrus':32,'dragon fruit':8}
explode = (0.1, 0.2, 0, 0) # offset second slice
fig1, ax1 = plt.subplots() # first returned is the containing figure (fig1), then the subplot Axe object(s) (ax1)
ax1.pie(data.values(), labels=data.keys(), explode=explode, autopct=lambda p:'{:.2f}%({:.0f})'.format(p,(p/100)*sum(data.values())), 
        #autopct=make_autopct(data.values()), 
        #autopct='%.1f', 
        # autopct= a format string like '%1.2f%%' for showing pct sign and 2 decimals
        shadow=True, startangle=90)
ax1.set_aspect('equal')
ax1.legend(data.keys(), loc='upper right') # use instead of labels in ax1.pie(...)
#ax1.axis('equal')  
#plt.tight_layout()
plt.show()