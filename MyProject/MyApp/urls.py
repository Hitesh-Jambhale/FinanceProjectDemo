from django.urls import path
from .views import homeView,eligibility_view

urlpatterns = [
    path('home/',homeView),
    path('el',eligibility_view)
]