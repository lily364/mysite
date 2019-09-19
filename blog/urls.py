from django.urls import path
from .views import blog_list, blog_detail, blog_with_type
urlpatterns = [
    path('', blog_list, name='blogs'),
    path('<int:blog_id>', blog_detail, name='blog'),
    path('type/<int:blog_type>', blog_with_type, name='blog_type'),
]