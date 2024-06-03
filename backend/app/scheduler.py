from datetime import datetime, timedelta

def schedule_daily_task(time_of_day):
    now = datetime.now()
    next_run = datetime.combine(now.date(), time_of_day)
    if next_run < now:
        next_run += timedelta(days=1)
    return next_run

def schedule_weekly_task(day_of_week, time_of_day):
    now = datetime.now()
    next_run = now + timedelta((day_of_week - now.weekday() + 7) % 7)
    next_run = datetime.combine(next_run.date(), time_of_day)
    if next_run < now:
        next_run += timedelta(weeks=1)
    return next_run
