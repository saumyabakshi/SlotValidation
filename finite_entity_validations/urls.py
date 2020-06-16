from django.urls import path

from .views import validate

app_name = "finite_entity_validations"

urlpatterns = [
    path('finite_entity_validations/', validate, name='post'),

]