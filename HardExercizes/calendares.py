import calendar
from datetime import date

currentYear = date.today().year
for lerp in range(currentYear, currentYear+10):
    if calendar.isleap(lerp) : 
        print(lerp)
        break

print(calendar.leapdays(2001, 2050))

print(calendar.weekday(2016,7,29))
print(calendar.day_name[calendar.weekday(2016,7,29)])