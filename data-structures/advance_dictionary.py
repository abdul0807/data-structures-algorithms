# *****************************
# Created by Mohammed Abdul Qavi on 17/06/22
# *****************************

from typing import Any, Dict


class AdvanceDictionary(object):
    """
    Create and Update the dictionary data structure in python with advance features like nested keys and list of values
    """

    def __init__(self):
        pass

    def create_dict(self,
                    keys: Any,
                    value: Any) -> Dict[Any, list]:
        """

        :param keys: the keys to create a new dictionary. This can be a single key or a list of keys. In case of a list, a dictionary with nested key is created.
        :param value: the value to be assigned to the given key
        :return: the newly created dictionary with the given keys and value
        """
        new_dict = dict()
        if isinstance(keys, list):
            if len(keys) == 1:
                new_dict[keys[0]] = [value]
            else:
                new_dict[keys[0]] = self.create_dict(keys[1:], value)  # calling the function recursively
        else:
            new_dict[keys] = [value]

        return new_dict

    def update_dict(self,
                    given_dict: Dict[Any, list],
                    keys: Any,
                    value: Any):
        """

        :param given_dict: the given dictionary to be updated
        :param keys: the keys to update the given dictionary. This can be a single key or a list of keys. In case of a list, a dictionary with nested key is added.
        :param value: the value to be assigned to the given key
        :return:
        """
        if not isinstance(keys, list):
            keys = [keys]

        known_keys = []
        for k in keys:
            if isinstance(given_dict, dict) and k in given_dict.keys():
                known_keys.append(k)
                given_dict = given_dict[k]
            else:
                break

        if isinstance(given_dict, dict):
            unknown_keys = [k for k in keys if k not in known_keys]
            new_dict = self.create_dict(unknown_keys, value)
            given_dict.update(new_dict)
        elif isinstance(given_dict, list):
            given_dict.append(value)
        else:
            given_dict = [value]


if __name__ == "__main__":
    dict_obj = AdvanceDictionary()
    locations = dict_obj.create_dict(keys=['North America', 'USA'], value='Mountain View')
    print(locations)

    dict_obj.update_dict(locations, keys=['Asia', 'India'], value='Bangalore')
    dict_obj.update_dict(locations, keys=['North America', 'USA'], value='Atlanta')
    dict_obj.update_dict(locations, keys=['Africa', 'Egypt'], value='Cairo')
    dict_obj.update_dict(locations, keys=['Asia', 'China'], value='Shanghai')
    print(locations)

"""
Output:

{'North America': {'USA': ['Mountain View']}}
{'North America': {'USA': ['Mountain View', 'Atlanta']}, 'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']}, 'Africa': {'Egypt': ['Cairo']}}

"""
