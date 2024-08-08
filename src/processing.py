from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате

    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


filtered_data_default = filter_by_state(data)
filtered_data_canceled = filter_by_state(data, 'CANCELED')

sorted_data_default = sort_by_date(data)
sorted_data_ascending = sort_by_date(data, reverse=False)

print("Filtered data (default):", filtered_data_default)
print("Filtered data (CANCELED):", filtered_data_canceled)
print("Sorted data (default):", sorted_data_default)
print("Sorted data (ascending):", sorted_data_ascending)