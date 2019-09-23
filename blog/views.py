from django.shortcuts import render_to_response, get_object_or_404
from .models import Blog, BlogType
from django.core.paginator import Paginator
from django.conf import settings
# Create your views here.


def page_of_common(request, blogs):
    context = {}
    paginator = Paginator(blogs, settings.EACH_PAGE_BLOGS_NUM)
    # 获取传入的页面参数
    page_num = request.GET.get('page')
    if page_num is None:
        page_num = 1
    # 获取当前页面
    blogs_of_page = paginator.get_page(page_num)
    # 过滤,保留blog_type=2的博客（2为博客类型的id）
    # blogs = Blog.objects.filter(blog_type=2)
    # 显示当前页的前两页和后两页
    page_range = list(range(max(1, int(page_num) - 2), int(page_num))) + \
                 list(range(int(page_num), min(int(page_num) + 2, paginator.num_pages) + 1))
    # 加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if 1 not in page_range:
        page_range.insert(0, 1)
    if paginator.num_pages not in page_range:
        page_range.append(paginator.num_pages)
    context['page_range'] = page_range
    context['blogs'] = blogs_of_page
    return context


def blog_list(request):
    # 查询全部
    blogs = Blog.objects.all()
    blog_types = BlogType.objects.all()
    context = page_of_common(request, blogs)
    context['blog_types'] = blog_types
    return render_to_response('blog/blog_list.html', context)


def blog_detail(request, blog_id):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_id)
    last_blog = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['last_blog'] = last_blog
    next_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['next_blog'] = next_blog
    context['blog_detail'] = blog
    return render_to_response('blog/blog_detail.html', context)


def blog_with_type(request, blog_type):
    types = Blog.objects.filter(blog_type=blog_type)
    context = page_of_common(request, types)
    all_types = BlogType.objects.all()
    context['all_types'] = all_types
    return render_to_response('blog/blog_with_type.html', context)



