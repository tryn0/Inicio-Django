from django.views.generic import DetailView, ListView, DeleteView
from myblog.models import Post
from django.urls import reverse_lazy

class PostListView(ListView):
    template_name = "post_list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
