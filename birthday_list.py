from datetime import datetime,  timedelta
from collections import defaultdict

weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_birthdays_per_week(users):
    current_date = datetime.now().date()
    end_date = current_date + timedelta(days=7)
    dict = defaultdict(list)
    for user in users: 
        for name, birthday in user.items(): #замена года рождения на текущий год
            b = birthday.strftime("%y %m %d").split()
            b[0] = str(current_date.year)
            b = " ".join(b)
            birthday = datetime.strptime(b, "%Y %m %d")
            birthday = birthday.date()

            if current_date <= birthday < end_date: #проверяем приходится ли др на эту неделю
                day = birthday.weekday()
                if day not in (5, 6):
                    dict[birthday].append(name)
                #если выпал на выходные:
                elif day == 5: #суббота
                    dict[birthday+timedelta(days = 2)].append(name)
                elif day == 6:#воскресенье
                    dict[birthday+timedelta(days = 1)].append(name)
            else: 
                continue

    l = sorted(dict)
    for d in l:
        l = ", ".join(dict[d])
        print(f"{weekdays[d.weekday()]}: {l}")
    if len(dict) == 0:
         print("No birthdays this week")

if __name__ == "__main__":
        
    users = [
        {"Oleg": datetime(1994, 2, 1)},
        {"Olga": datetime(2000, 2, 4)},
        {"Nikita": datetime(1988, 1, 31)},
        {"Daria": datetime(1999, 2, 14)}, 
        {"Tanya": datetime( 2003, 2, 1)},
        {"Alex": datetime(1988, 2, 5)},
        {"Svitlana": datetime(1994, 2,2)}
    ]
    get_birthdays_per_week(users)

