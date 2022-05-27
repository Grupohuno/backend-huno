import datetime


def get_time():
    now = datetime.datetime.now()
    year = f"{now.year:02d}"
    month = f"{now.month:02d}"
    day = f"{now.day:02d}"
    # hour = "{:02d}".format(now.hour)
    # minute = "{:02d}".format(now.minute)
    day_month_year = f"{year}-{month}-{day}"
    return day_month_year
