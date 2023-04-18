from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path('register/', views.registerUserApi),
    path('register/', views.RegisterUserApiView.as_view() ),
    path('fetch-bets/', views.FetchBettDetailsApiView.as_view() ),

]


