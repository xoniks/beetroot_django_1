from django.urls import path
from .views import HomePageView, AboutPageview


urlpatterns =[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageview.as_view(),name = 'about')
]