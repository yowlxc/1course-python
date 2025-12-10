import functools
import sys
import logging
from datetime import datetime

def logger(func_non = None, *, handle = sys.stdout):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            start_msg = f"[{timestamp_1}] [INFO] Вызов функции {func.__name__}({signature})"
            if isinstance(handle, logging.Logger):
                handle.info(start_msg)
            elif hasattr(handle, 'write'):
                handle.write(start_msg + '\n')
            else:
                raise TypeError(f"Неизвестный тип handle: {type(handle)}.")

            try:
                result = func(*args, **kwargs)
                timestamp_end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                end_msg = f"[{timestamp_end}] [INFO] Функция {func.__name__} завершена успешно. Результат: {repr(result)}"
                if isinstance(handle, logging.Logger):
                    handle.info(end_msg)
                elif hasattr(handle, 'write'):
                    handle.write(end_msg + '\n')
                return result

            except Exception as e:
                timestamp_err = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                error_msg = f"[{timestamp_err}] [ERROR] {type(e).__name__}: {e}"
                if isinstance(handle, logging.Logger):
                    handle.error(error_msg)
                elif hasattr(handle, 'write'):
                    handle.write(error_msg + '\n')
                raise

        return wrapper
    return decorator

