from django.conf.urls import url
from django.views.generic import DetailView
from blog.models import Post, Category
from blog.views import CategoryListView, PostListView

urlpatterns = [
    # Index
    url(r'^(?P<page>\d+)?/?$', PostListView.as_view(
        model=Post,
        paginate_by=5,
        ),
        name='index'
    ),

    # Individual post
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', DetailView.as_view(
        model=Post,
        ),
        name='post'
    ),

    # Categories
    url(r'^category/(?P<slug>[a-zA-Z0-9-]+)/?$', CategoryListView.as_view(
        paginate_by=5,
        model=Category,
        ),
        name='category'
    ),
]