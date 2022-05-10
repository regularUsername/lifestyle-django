from django.urls import path
from . import views

app_name = 'videos'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>',views.detail_view, name='detail_view')
]
