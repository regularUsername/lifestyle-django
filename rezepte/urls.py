from django.urls import path

from . import views

app_name = 'rezepte'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    # path('kat<int:kat_id>', views.filter_by_cat, name='filter_by_cat'),
    # path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>', views.detail_view, name='detail_view'),
    path('favorite', views.favorite, name='favorite'),
]
