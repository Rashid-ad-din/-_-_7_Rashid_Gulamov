from django.urls import path

from webapp.views.notes import main_view, search_view, add_view

urlpatterns = [
    path('', main_view, name='main'),
    path('search/', search_view, name='search'),
    path('add/', add_view, name='add')
]
