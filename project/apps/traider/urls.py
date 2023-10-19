from django.urls import path
from . import views
## for autocomplete...
#from .views import *

app_name = "traider"

urlpatterns = [
    #path('screenshots/',
    #     SomethingAutocomplete.as_view(),
    #     name='something-autocomplete',
    #),

    path('statistic/', views.statistic, name="statistic"),
    path('balances/', views.balances, name="balances"),
    path('remove-candidates/', views.remove_candidates, name="remove_candidates"),
    path('add/', views.traid_add, name="traid_add"),
    path('<int:id>/edit/', views.traid_update, name="traid_update"),
    path('<int:id>/del/', views.traid_del, name="traid_del"),
    path('<int:id>/', views.traid, name='traid'),
	path('', views.index, name='index'),
]
