import functools
import io
from datetime import datetime

error_stream = io.StringIO()

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        error_stream.write(f"[{timestamp}] [INFO] Вызов функции {func.__name__}({signature})\n")

        try:
            result = func(*args, **kwargs)
        except (ConnectionError, ValueError, KeyError, TypeError) as e:
            timestamp_err = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            error_stream.write(f"[{timestamp_err}] [ERROR] {type(e).__name__}: {e}\n")
            raise

        timestamp_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_stream.write(f"[{timestamp_end}] [INFO] Функция {func.__name__} завершена успешно. Результат: {repr(result)}\n")
        return result
    return wrapper
