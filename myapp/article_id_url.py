from .views import article_id, update, delete, comment
from django.urls import path


urlpatterns = [
    path('<int:article_id>/', article_id, name='article_id'),
    path('<int:article_id>/comment/', comment, name='comment'),
    path('<int:article_id>/update/', update, name='update'),
    path('<int:article_id>/delete/', delete, name='delete'),
]