from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType
from django.core.paginator import Paginator
# Create your views here.


def blog_list(request):
    context = {}
    # 查询全部
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 4)
    # 获取传入的页面参数
    page_num = request.GET.get('page')
    blogs_of_page = paginator.get_page(page_num)
    blog_types = BlogType.objects.all()
    # 过滤,保留blog_type=2的博客（2为博客类型的id）
    # blogs = Blog.objects.filter(blog_type=2)
    context['blogs'] = blogs_of_page
    context['blog_types'] = blog_types
    return render_to_response('blog/blog_list.html', context)


def blog_detail(request, blog_id):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_id)
    context['blog_detail'] = blog
    return render_to_response('blog/blog_detail.html', context)


def blog_with_type(request, blog_type):
    context = {}
    types = Blog.objects.filter(blog_type=blog_type)
    context['blog_types'] = types
    all_types = BlogType.objects.all()
    context['all_types'] = all_types
    return render_to_response('blog/blog_with_type.html', context)



