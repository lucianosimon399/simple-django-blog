from blog.models import Post, Category
from django.views.generic import ListView
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

class PostListView(ListView):

    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories'] = \
            context['categories'] = \
            Post.objects.all().values(
                'category__name', 'category__slug'
            ).annotate(
                total=Count('category__name')
            ).order_by('total')
        return context

class CategoryListView(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            return Post.objects.filter(category=category)
        except Category.DoesNotExist:
            return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        try:
            context['category'] = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            context['category'] = None
        return context
