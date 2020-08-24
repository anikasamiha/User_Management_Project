from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_url'), #home-view- choice between parent/child user

    #Parent urls
    path('parent-form/', views.parent_form, name='parent_form_url'), #parents create 
    path('parent/<int:id>/', views.parent_form, name='parent_edit_url'), #and update
    path('parent-delete/<int:id>/', views.parent_delete, name='parent_delete_url'), #delete
    path('parent-list/', views.parent_list, name='parent_list_url'), #list of parents

    #Child urls
    path('child-form/', views.child_form, name='child_form_url'), #child create 
    path('child/<int:id>/', views.child_form, name='child_edit_url'), #and update
    path('child-delete/<int:id>/', views.child_delete, name='child_delete_url'), #delete
    path('child-list/', views.child_list, name='child_list_url'), #list of children
]

