def get_mask_card_number(card_number: str) -> str:
    """ Разбиваем номер карты на части """
    first_block = card_number[:4]
    second_block = card_number[4:6]
    fourth_block = card_number[12:] if len(card_number) > 12 else ""

    """ Формируем замаскированный номер карты """
    masked_card_number = f"{first_block} {second_block}** ****  {fourth_block}"

    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """ Берем последние 4 символа номера счета """
    last_four_digits = account_number[-4:]

    """ Формируем замаскированный номер счета """
    masked_account_number = f"**{last_four_digits}"

    return masked_account_number


