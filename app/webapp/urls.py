from django.urls import path

from webapp.views.notes import main_view

urlpatterns = [
    path('', main_view, name='main')
]