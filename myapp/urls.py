from django.urls import path
from .views import (
    create_article,
    list_topics,
    articles_by_topic,
    subscribe_to_topic,
    unsubscribe_from_topic,
    user_profile,
    register,
    set_password,
    login_view,
    logout_view,
)

urlpatterns = [
    path('create/', create_article, name='create_article'),
    path('topics/', list_topics, name='list_topics'),
    path('topics/<int:topic_id>/', articles_by_topic, name='articles_by_topic'),
    path('topics/<int:topic_id>/subscribe/', subscribe_to_topic, name='subscribe_to_topic'),
    path('topics/<int:topic_id>/unsubscribe/', unsubscribe_from_topic, name='unsubscribe_from_topic'),
    path('profile/', user_profile, name='user_profile'),
    path('register/', register, name='register'),
    path('set-password/', set_password, name='set_password'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]