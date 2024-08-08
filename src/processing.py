from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    """
    return [item for item in data if item.get('state') == state]