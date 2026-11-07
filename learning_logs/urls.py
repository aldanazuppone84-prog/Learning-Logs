"""definite the URL mode of learning_logs"""
from django.urls import path

from . import views

app_name ='learning_logs'
urlpatterns = [
    # main page
    path('', views.index, name = 'index'),
    # page to display all the topics
    path('topics/', views.topics, name='topics'), 
    # specific page to show certain topic 
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page used for adding the new schame 
    path('new_topic/', views.new_topic, name='new_topic'),
    # page used for adding the new items 
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page used for editting the items
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]