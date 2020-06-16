from typing import Tuple

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .logic import validate_finite_values_entity

@api_view(['POST'])
def validate(request):
    if request.method == 'POST':
        values_to_be_validated = request.data.get("values")
        invalid_trigger = request.data.get("invalid_trigger", None)
        key = request.data.get("key", None)
        supported_values = request.data.get("supported_values", None)
        support_multiple = request.data.get("support_multiple", True)
        pick_first = request.data.get("pick_first", False)
        slot_validation_result: Tuple[bool, bool, str, dict] = validate_finite_values_entity(values_to_be_validated,
                                                                                           supported_values,
                                                                                           invalid_trigger, key,
                                                                                           support_multiple, pick_first)
        filled = slot_validation_result[0]
        partially_filled = slot_validation_result[1]
        trigger = slot_validation_result[2]
        parameters = slot_validation_result[3]
        return Response({"filled": filled, "partially_filled": partially_filled, "trigger": trigger
                            , "parameters": parameters})

    return Response({"message": "Send POST request"})
