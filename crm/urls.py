from django.contrib import admin
from django.urls import path, include
from .views import CrmCreateView

urlpatterns = [
    path('', CrmCreateView.as_view(), name="crm_form"),
]
