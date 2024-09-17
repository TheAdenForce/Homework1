import logging


masks_logger = logging.getLogger('masks')
# создаем обработчик, который будет писать в файл, режим w
file_handler = logging.FileHandler("../logs/masks_log.log", 'w')
# создаём форматтер, задаём нужный нам формат
file_formatter = logging.Formatter("%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s")
# соединяем. Форматтер к обработчику, обработчик к логгеру
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.INFO)



def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску.
    7000 79** **** 6361"""
    masks_logger.info("Создаю маску номера карты")
    if len(str(card_number)) != 16:
        masks_logger.error("Неправильный номер карты")
        raise ValueError("Неправильный номер карты")
    masks_logger.info("Маска номера карты создана")
    return f"{int(str(card_number)[:4])} {int(str(card_number)[4:6])}** **** {int(str(card_number)[12:])}"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску.
    **4305"""
    masks_logger.info("Создаю маску номера счета")
    if len(str(account_number)) != 20:
        masks_logger.error("Неправильный номер счета")
        raise ValueError("Неправильный номер счета")
    masks_logger.info("Маска номера счета создана")
    return f"**{int(str(account_number)[-4:])}"
