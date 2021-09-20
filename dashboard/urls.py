from django.urls import path
from . import views
import dashboard

app_name = "dashboard"

urlpatterns = [
    path('',views.DashboardView.as_view(),name="index")
]
