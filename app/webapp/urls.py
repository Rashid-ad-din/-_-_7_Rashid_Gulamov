from django.urls import path

from webapp.views.notes import main_view, search_view, add_view, edit_view, delete_view, confirm_delete_view

urlpatterns = [
    path('', main_view, name='main'),
    path('search/', search_view, name='search'),
    path('add/', add_view, name='add'),
    path('edit/<pk>/', edit_view, name='edit'),
    path('delete/<pk>/', delete_view, name='delete'),
    path('confirm-delete/<pk>/', confirm_delete_view, name='confirm_delete')
]
