from django.urls import path
from .views import blog_list, blog_detail, blog_with_type, blog_with_date
urlpatterns = [
    path('', blog_list, name='blogs'),
    path('<int:blog_id>', blog_detail, name='blog'),
    path('type/<int:blog_type>', blog_with_type, name='blog_type'),
    path('date/<int:year>/<int:month>', blog_with_date, name='blog_date')
]