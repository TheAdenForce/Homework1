import json
import logging
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion

utils_logger = logging.getLogger('utils')
# создаем обработчик, который будет писать в файл, режим w
file_handler = logging.FileHandler("../logs/utils_log.log", 'w')
# создаём форматтер, задаём нужный нам формат
file_formatter = logging.Formatter("%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s")
# соединяем. Форматтер к обработчику, обработчик к логгеру
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.INFO)


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        utils_logger.info("Открываю файл с транзакциями")
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                utils_logger.error("Ошибка файла с транзакциями")
                return []
        if not isinstance(transactions, list):
            utils_logger.error("Список транзакций пуст")
            return []
        utils_logger.info("Создан список словарей с данными о финансовых транзакциях")
        return transactions
    except FileNotFoundError:
        utils_logger.error("Файл с транзакциями не найден")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        utils_logger.info("Код валюты в транзакции RUB")
    else:
        amount = currency_conversion(trans)
        utils_logger.info("Код валюты транзакции не RUB, произведена конвертация")
    return amount
