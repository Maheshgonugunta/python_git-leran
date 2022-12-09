from django.contrib import admin
from django.urls import path
from.import views
from.views import loginDetailAPI
urlpatterns=[

    path('api/login-detail/',loginDetailAPI.as_view()),
]