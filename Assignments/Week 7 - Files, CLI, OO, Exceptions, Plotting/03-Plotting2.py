import matplotlib.pyplot as plt

persons = {'Holger':25,'Helga':54,'Hasse':76,'Halvor':12,'Hassan':43,'Hulda':31,'Hansi':102}

names = list(persons.keys())
age = list(persons.values())
plt.ylabel("Age", fontsize=10)
plt.xlabel("Person", fontsize=10)


plt.bar(names, age, width=0.7, align='center')
plt.show()