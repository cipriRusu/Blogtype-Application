from functools import wraps
from services.services import Services

def inject(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for element in func.__annotations__.items():
            kwargs[element[0]] = Services.get_service(element[1])
        return func(*args, **kwargs)
    return wrapper
