from typing import Tuple

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .logic import validate_numeric_entity


@api_view(['POST'])
def validate(request):
    if request.method == 'POST':
        values_to_be_validated = request.data.get("values")
        supported_values = request.data.get("supported_values", None)
        invalid_trigger = request.data.get("invalid_trigger", None)
        key = request.data.get("key", None)
        support_multiple = request.data.get("support_multiple", True)
        pick_first = request.data.get("pick_first", False)
        constraint = request.data.get("constraint", None)
        var_name = request.data.get("var_name", None)
        numeric_slot_validation_result: Tuple[bool, bool, str, dict] = validate_numeric_entity(values_to_be_validated,invalid_trigger,key,
                                                                                               support_multiple,pick_first,constraint,var_name)
        filled = numeric_slot_validation_result[0]
        partially_filled = numeric_slot_validation_result[1]
        trigger = numeric_slot_validation_result[2]
        parameters = numeric_slot_validation_result[3]
        return Response({"filled": filled, "partially_filled": partially_filled, "trigger": trigger
                            , "parameters": parameters})
