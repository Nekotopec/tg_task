import json


def flatten(dictionary: dict) -> dict:
    """Return flattened dictionary."""

    # Избегаем неявного изменения словаря.
    dictionary = dict(dictionary)

    new_dict = dict()
    while dictionary:
        key, value = dictionary.popitem()
        if type(value) == dict:
            for sub_key, sub_value in value.items():
                dictionary[f'{key}.{sub_key}'] = sub_value
        else:
            new_dict[key] = value
    return new_dict


if __name__ == '__main__':

    dictionary = {
        "a": 5,
        "b": 6,
        "c": {
            "f": 9,
            "g": {
                "m": 17,
                "n": 3
            }
        }
    }
    d = flatten(dictionary)
    try:
        assert d == {
            'a': 5,
            'b': 6,
            'c.f': 9,
            'c.g.m': 17,
            'c.g.n': 3
        }
        print('Test has been PASSED.')
    except AssertionError:
        print('Test has been FAILED')
    print(json.dumps(d, indent=2, sort_keys=True))
