from django.urls import path
from tweet import views

urlpatterns = [
    path('',views.tweet_List, name='TweetList'),
    path('create/',views.tweet_Create, name='TweetCreate'),
    path('<int:tweet_id>/edit/',views.tweet_Edit,name='TweetEdit'),
    path('<int:tweet_id>/delete/',views.tweet_Delete,name='TweetDelete'),
    path('register/',views.register, name='register'),
]