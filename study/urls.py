from django.urls import path
from . import views
from .views import IndexView
app_name = 'study'
urlpatterns = [
    path('', views.index,name='index'),
    path('', IndexView.as_view(),name='index'),
]