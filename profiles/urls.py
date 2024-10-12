from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles import views

# router = DefaultRouter()
# router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]
