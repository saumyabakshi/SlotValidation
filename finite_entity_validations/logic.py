from typing import List, Dict, Callable, Tuple

SlotValidationResult = Tuple[bool, bool, str, Dict]


def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                  invalid_trigger: str = None, key: str = None,
                                  support_multiple: bool = True, pick_first: bool = False,
                                  **kwargs) -> SlotValidationResult:
    """
    Validate an entity on the basis of its value extracted.
    The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param supported_values: List of supported values for the slot
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :return: a tuple of (filled, partially_filled, trigger, params)
    """
    if not values:
        return (False, False, invalid_trigger, {})

    list_of_values = [value_dict['value'] for value_dict in values]
    list_of_valid_values = [value for value in list_of_values if value in supported_values]

    if not list_of_valid_values:
        filled = False
        partially_filled = True
        return (filled, partially_filled, invalid_trigger, {})

    if len(list_of_valid_values) == len(list_of_values):
        filled = True
        partially_filled = False
    else:
        filled = False
        partially_filled = True

    if support_multiple == False and pick_first == True:
        if list_of_values[0] == list_of_valid_values[0]:
            param_values = list_of_valid_values[0]
            param_values_dict = {key: param_values.upper()}
            if filled:
                return (filled, partially_filled, '', param_values_dict)
            else:
                return (filled,partially_filled,invalid_trigger,param_values_dict)
        else:
            return (filled, partially_filled, invalid_trigger, {})

    if filled:
        param_values = list(map(lambda valid_value: valid_value.upper(), list_of_valid_values))
        param_values_dict = {key: param_values}
        return (filled, partially_filled, '', param_values_dict)
    else:
        return (filled, partially_filled,invalid_trigger, {})

