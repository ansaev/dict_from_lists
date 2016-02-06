from dict_from_lists import dict_from_lists
from pytest import fixture

@fixture(params=[
    {
        "keys": ["key1", "key2"],
        "values": [1, 2],
        'dict': {"key1": 1, 'key2': 2}
     },
    {
        "keys": ["key1", "key2", "key3"],
        "values": [1, 2],
        'dict': {"key1": 1, 'key2': 2, 'key3': None}
    },
    {
        "keys": ["key1", "key2"],
        "values": [1, 2, 3, 4, 5],
        'dict': {"key1": 1, 'key2': 2}
    },
])
def test_data(request):
    return request.param

def test_dict_from_lists(test_data):
    assert dict_from_lists(test_data['keys'], test_data['values']) == test_data['dict']
