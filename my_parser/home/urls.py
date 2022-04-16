from msilib.schema import ListView
from django.urls import path
from . import views
from .views import Parse, Show_tablet, Sorting_by_create_data, Sorting_by_update_data, Sorting_by_country, Sorting_by_url, Sorting_by_dead


urlpatterns = [
    path('', views.show, name="home_form"),
   
    path('test', views.test, name="test"),
    path('test_two', views.test_two, name="test_two"),

  
    path('send', Parse.as_view(), name='result'),

    
    path('result', Show_tablet.as_view(), name="table"),

    # Сортировка.
    path('result/search by create data', Sorting_by_create_data.as_view(), name='search_create_data'),
    path('result/search by update data', Sorting_by_update_data.as_view(), name='search_update_data'),
    path('result/search by country', Sorting_by_country.as_view(), name='search_country'),
    path('result/search by url', Sorting_by_url.as_view(), name='search_url'),
    path('result/search by dead', Sorting_by_dead.as_view(), name='search_dead')
]
