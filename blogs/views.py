from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import CategoryModel, PostModel, PostTagModel, CommentModel
from .forms import CommentModelForm


class PostListView(ListView):
    template_name = 'blog.html'
    paginate_by = 3

    def get_queryset(self, **kwargs):
        qs = PostModel.objects.order_by('-id')
        tag = self.request.GET.get('tag')
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(title__icontains=search)
        if tag:
            qs = qs.filter(tag__name=tag)

        cat = self.request.GET.get('cat')
        if cat:
            qs = qs.filter(category_id=cat)
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['category'] = CategoryModel.objects.all()
        data['tags'] = PostTagModel.objects.all()
        data['comment'] = CommentModel.objects.all()
        data['post'] = PostModel.objects.all()
        return data


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['category'] = CategoryModel.objects.all()
        data['tags'] = PostTagModel.objects.all()
        data['comment'] = CommentModel.objects.all()
        data['post'] = PostModel.objects.all()
        return data


class CommentCreateView(CreateView):
    form_class = CommentModelForm
    template_name = 'blog-detail.html'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(PostModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.kwargs.get('pk')})
