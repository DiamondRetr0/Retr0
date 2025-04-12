import logging

# Настройка логгера
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
    """
    Вычисляет факториал числа n рекурсивным методом.
    """
    logging.debug(f"Вычисление factorial({n})")  # Логирование начала вычисления

    if n == 0:
        logging.debug("Базовый случай: n == 0, возвращаем 1")
        return 1
    elif n < 0:
        logging.warning("Введенное число отрицательное. Факториал не определен.")
        return None
    else:
        result = n * factorial(n - 1)
        logging.debug(f"Промежуточный результат: factorial({n}) = {n} * factorial({n - 1}) = {result}") # Логирование промежуточного результата
        return result

# Пример использования
number = 5
result = factorial(number)

if result is not None:
    logging.info(f"Факториал числа {number} равен {result}")
else:
    logging.error("Не удалось вычислить факториал.")

