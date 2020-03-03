from datetime import datetime


def date_in_the_past(d):
    d = datetime(*d.timetuple()[:6]).date()
    return datetime.utcnow().date() > d
