from datetime import datetime, time
from home.models import DailyOpertingHours

def is_restaurant_open():
    now = datetime.now()
    current_day = now.strftime("%A") 
    current_time = now.time()

    # Example opening hours (you can customize these)
    # Each day maps to (opening_time, closing_time)
    opening_hours = {
        "Monday": (time(9, 0), time(22, 0)),     # 9 AM - 10 PM
        "Tuesday": (time(9, 0), time(22, 0)),
        "Wednesday": (time(9, 0), time(22, 0)),
        "Thursday": (time(9, 0), time(22, 0)),
        "Friday": (time(9, 0), time(23, 0)),     # Open till 11 PM on Fridays
        "Saturday": (time(10, 0), time(23, 0)),  # Open 10 AM - 11 PM
        "Sunday": (time(10, 0), time(21, 0)),    # Open 10 AM - 9 PM
    }

    if current_day not in opening_hours:
        return False  # closed if no data available

    open_time, close_time = opening_hours[current_day]

    return open_time <= current_time <= close_time

def get_today_operating_hours():
    today = datetime.now().strftime('%A')

    try:
        hours = DailyOpertingHours.objects.get(day_of_week=today)
        return(hours.open_time, hours.close_time)
    except:
        return (None , None)

def is_valid_phone_number(phone_number: str) -> bool:
    pattern = re.compile(r"^\+?\d{1,3}?[-\s]?\d{3,5}[-\s]?\d{4,7}$")
    return bool(pattern.match(phone_number))                     