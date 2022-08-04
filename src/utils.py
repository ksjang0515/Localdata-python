from datetime import datetime


def check_date_format(date: str) -> bool:
    try:
        datetime.strptime(date, '%Y%m%d')
    except ValueError:
        return False

    return True
