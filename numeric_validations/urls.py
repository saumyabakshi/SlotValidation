from django.urls import path

from .views import validate

app_name = "numeric_validations"

urlpatterns = [
    path('numeric_validations/', validate,name='post'),

]