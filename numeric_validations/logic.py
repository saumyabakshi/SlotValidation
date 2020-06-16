from typing import List, Dict, Callable, Tuple
import ast

SlotValidationResult = Tuple[bool, bool, str, Dict]


def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                            support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None,
                            **kwargs) -> SlotValidationResult:
    """
    Validate an entity on the basis of its value extracted.
    The method will check if that value satisfies the numeric constraints put on it.
    If there are no numeric constraints, it will simply assume the value is valid.

    If there are numeric constraints, then it will only consider a value valid if it satisfies the numeric constraints.
    In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
    will be filtered so that only those values are used to fill the slot which satisfy the numeric constraint.

    If multiple values are supported and even 1 value does not satisfy the numeric constraint, the slot is assumed to be
    partially filled.

    :param pick_first: Set to true if the first value is to be picked up
    :param support_multiple: Set to true if multiple utterances of an entity are supported
    :param values: Values extracted by NLU
    :param invalid_trigger: Trigger to use if the extracted value is not supported
    :param key: Dict key to use in the params returned
    :param constraint: Conditional expression for constraints on the numeric values extracted
    :param var_name: Name of the var used to express the numeric constraint
    :return: a tuple of (filled, partially_filled, trigger, params)
    """
    if not values:
        return (False, False,invalid_trigger,{})

    list_of_values = [value_dict['value'] for value_dict in values]

    if not constraint:
        if pick_first == True:
            param = list_of_values[0]
            param_dict = {key : param}
        else:
            param_dict = {key: list_of_values}
        return (True,False,'',param_dict)

    validated_values = list(filter(lambda y:eval(constraint,{},{var_name:y}) == True,list_of_values))

    if not validated_values:
        filled = False
        partially_filled = True
        return (filled, partially_filled, invalid_trigger, {})

    if len(list_of_values) == len(validated_values):
        filled = True
        partially_filled = False
    else:
        filled = False
        partially_filled = True

    if support_multiple == False and pick_first == True:
        if list_of_values[0] in validated_values:
            param_value = validated_values[0]
            param_dict = {key: param_value}
            if filled:
                return (filled, partially_filled, '', param_dict)
            else:
                return (filled, partially_filled, invalid_trigger, param_dict)
        else:
            return(filled,partially_filled,invalid_trigger,{})

    # if support_multiple is True and pick_first is False:
    param_dict = {key: validated_values}
    if filled:
        return (filled,partially_filled,'',param_dict)
    else:
        return (filled,partially_filled,invalid_trigger,param_dict)



