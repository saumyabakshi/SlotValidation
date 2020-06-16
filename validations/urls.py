from django.urls import path

from .views import posting

app_name = "validations"

urlpatterns = [
    path('validations/', posting,name='post'),

]