
import csv
import numpy as np
import matplotlib.pyplot as plt

## 1. Open the file './befkbhalderstatkode.csv'
filename = './befkbhalderstatkode.csv'

## Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
data = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)

# print(data.size) # Test if file is read (OK)

dd = data

## Find out how many people lived in each of the 11 areas in 2015, using this data.

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

def number_of_people_in_each_neighborhood(n, mask):
    all_people_in_given_n = dd[mask & (dd[:,1] == n)]
    sum_of_people = all_people_in_given_n[:,4].sum() # 4 is idex of no of 'PERSONER'
    return sum_of_people
people_mask = (dd[:,0] == 2015)
sum = np.array([number_of_people_in_each_neighborhood(n, people_mask) for n in neighb.keys()])
cph_1 = sum[0] + sum[1] + sum[2] + sum[3] + sum[4] + sum[5] + sum[6] + sum[7] + sum[8] + sum[9] + sum[10]

#print(sum) (OK)
#print(cph) (OK)

## 4. Make a bar plot to show the size of each city area from the smallest to the largest

cities = list(neighb.values())
no_of_cities = list(neighb.keys())
no_of_people = list(sum)

plt.bar(cities, sum,  width=0.5, align='center')
plt.axis([0, len(cities), 0, max(no_of_people) + 1000]) 
plt.xlabel("cities", fontsize=10)
plt.xticks(rotation=80)
plt.ylabel("Number of People in each city", fontsize=10)
#plt.show() (OK)

## 5. Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015

cph = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest'}
above_65_mask = (dd[:,0] == 2015) & (dd[:,2] > 65)

above_65 = np.array([number_of_people_in_each_neighborhood(n, above_65_mask) for n in cph.keys()])
people_over_65 = above_65[0] + above_65[1] + above_65[2] + above_65[3] + above_65[4] + above_65[5] + above_65[6] + above_65[7] + above_65[8] + above_65[9]
# print(above_65) (OK)
# print(people_over_65) # amount of people over 65 in cph in 2015 (OK) result: 55700

## 6. How many of those were from the other nordic countries (not dk)

# Nordic countries 5104: 'Finland', 5110: 'Norge', 5120: 'Sverige'

over_65_from_finland_mask = (dd[:,0] == 2015) & (dd[:,2] > 65) & (dd[:,3] == 5104)
over_65_from_finland = np.array([number_of_people_in_each_neighborhood(n, over_65_from_finland_mask) for n in cph.keys()])
over_65_from_norway_mask = (dd[:,0] == 2015) & (dd[:,2] > 65) & (dd[:,3] == 5110)
over_65_from_norway = np.array([number_of_people_in_each_neighborhood(n, over_65_from_norway_mask) for n in cph.keys()])
over_65_from_sweden_mask = (dd[:,0] == 2015) & (dd[:,2] > 65) & (dd[:,3] == 5120)
over_65_from_sweden = np.array([number_of_people_in_each_neighborhood(n, over_65_from_sweden_mask) for n in cph.keys()])
over_65_from_scandinavia_ex_dk = over_65_from_finland[0] + over_65_from_finland[1] + over_65_from_finland[2] + over_65_from_finland[3] + over_65_from_finland[4] + over_65_from_finland[5] + over_65_from_finland[6] + over_65_from_finland[7] + over_65_from_finland[8] + over_65_from_finland[9] + over_65_from_norway[0] + over_65_from_norway[1] + over_65_from_norway[2] + over_65_from_norway[3] + over_65_from_norway[4] + over_65_from_norway[5] + over_65_from_norway[6] + over_65_from_norway[7] + over_65_from_norway[8] + over_65_from_norway[9] + over_65_from_sweden[0] + over_65_from_sweden[1] + over_65_from_sweden[2] + over_65_from_sweden[3] + over_65_from_sweden[4] + over_65_from_sweden[5] + over_65_from_sweden[6] + over_65_from_sweden[7] + over_65_from_sweden[8] + over_65_from_sweden[9]
# print(over_65_from_scandinavia_ex_dk) (ok) result: 573

## 7. Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015

unique_years = np.unique(dd[:,0])
print(unique_years)

def number_of_people_each_year(n, mask):
    all_people_in_given_n = dd[mask & (dd[:,1] == n)]
    sum_of_people = all_people_in_given_n[:,4].sum() # 4 is idex of no of 'PERSONER'
    return sum_of_people

vesterbro_1992_to_2015_mask = (dd[:,2] > 18)
vesterbro_1992_to_2015 = np.array([number_of_people_in_each_neighborhood(n, vesterbro_1992_to_2015_mask) for n in unique_years])
#print(vesterbro_1992_to_2015)
