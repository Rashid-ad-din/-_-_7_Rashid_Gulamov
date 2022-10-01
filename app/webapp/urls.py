from django.urls import path

from webapp.views.notes import main_view, search_view

urlpatterns = [
    path('', main_view, name='main'),
    path('/search/', search_view, name='search')
]
