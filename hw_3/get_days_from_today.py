from datetime import datetime

def get_days_from_today(date: str):
    today = datetime.today().date()

    try:
        day_given = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "The format of the date have to be YYYY-MM-DD!"

    return (day_given - today).days

test = get_days_from_today("2026-06-17")
print(test)