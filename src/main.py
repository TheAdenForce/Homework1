from src.masks import get_mask_card_number
from src.utils import transaction_amount

print(get_mask_card_number("1234567890123456"))
print(
    transaction_amount({"operationAmount": {"amount": 25, "currency": {"code": "RUB"}}})
)
