from masks import get_mask_card_number, get_mask_account

card_or_account_request = input('Введите номер карты или счета: ')

def mask_account_card(nums: str) -> str:
    """ Функция принимает название платёжной системы и номер карты или номер счета и выводит их маскировку"""
    if 'Счет' not in nums:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums.replace(nums[-16:], cards)
        return new_card
    else:
        account = get_mask_account(nums[-20:])
        new_account = nums.replace(nums[-20:], account)
        return new_account


print(mask_account_card(card_or_account_request))