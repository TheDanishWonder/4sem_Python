import matplotlib.pyplot as plt

student_attendance = {'day1':33, 'day2':34,'day3':29,'day4':31,'day5':28,'day6':26,'day7':30}

days = list(student_attendance.keys())
att = list(student_attendance.values())
plt.ylabel("Days", fontsize=10)
plt.xlabel("Attendance", fontsize=10)


plt.plot(days, att)
plt.show()