from datetime import datetime
from exceptions import InvalidNumberError


def to_number(value: str) -> float: #str to flt

    try:
        return float(value)
    except ValueError:
        raise InvalidNumberError(f"Invalid numeric value: {value}")


def current_timestamp() -> str: #return date
    
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
