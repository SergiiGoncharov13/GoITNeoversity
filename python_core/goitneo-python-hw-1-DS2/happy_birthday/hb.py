from datetime import datetime, timedelta


users= [
        {'name' : 'Bill', 'birthday' : datetime(year=2000, month=12, day=4)},
        {'name' : 'John', 'birthday' : datetime(year=2000, month=12, day=5)},
        {'name' : 'Tim', 'birthday' : datetime(year=2000, month=12, day=6)},
        {'name' : 'Alisha', 'birthday' : datetime(year=2000, month=11, day=26)},
        {'name' : 'Julie', 'birthday' : datetime(year=2000, month=12, day=7)},
        {'name' : 'Sabina', 'birthday' : datetime(year=2000, month=12, day=11)},
        {'name' : 'Anna', 'birthday' : datetime(year=2000, month=12, day=6)},
        {'name' : 'Emma', 'birthday' : datetime(year=2000, month=12, day=8)},
        {'name' : 'Charles', 'birthday' : datetime(year=2000, month=12, day=10)},
        {'name' : 'Victoria', 'birthday' : datetime(year=2000, month=12, day=12)}
    ]


def get_birthdays_per_week(users):
    today_date = datetime.now()
    days_interval = define_days_interval(today_date)
    new_day = today_date + days_interval

    day_of_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    for user in users:
        new_date = datetime(
            year=today_date.year,
            month=user.get('birthday').month,
            day=user.get('birthday').day
        )

        if today_date < new_date <= new_day:
            weekday_string = new_date.strftime("%A")
            if weekday_string in ["Saturday", "Sunday"]:
                weekday_string = "Monday"
            day_of_week.get(weekday_string).append(user.get("name"))
    return print_result_list(day_of_week)


def define_days_interval(today_date):
    if today_date.weekday() == 5:
        days_interval = timedelta(days=6)
    elif today_date.weekday() == 6:
        days_interval = timedelta(days=5)
    else:
        days_interval = timedelta(days=7)
    return days_interval


def print_result_list(day_of_week):
    for k, v in day_of_week.items():
        if v:
            print(f'{k}: {", ".join(v)}')



if __name__ == "__main__":
    get_birthdays_per_week(users)