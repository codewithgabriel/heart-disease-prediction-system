from django.contrib import admin
from django.urls import path
from . import views

app_name = "predict_app"
urlpatterns = [
    path('/' , views.index , name="index"),
    path('system/' , views.predict_system , name="system"),
    path('result/' , views.predict_system_result , name="result"),
    path('about/' , views.about, name="about")


]
