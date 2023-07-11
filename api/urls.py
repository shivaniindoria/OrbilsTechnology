from django.urls import path
from .views import DumpItApi

urlpatterns = [
    path('',DumpItApi.as_view()),
    path('create/',DumpItApi.as_view())
]
