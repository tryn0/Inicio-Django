from django.urls import path
from myblog.views import PostListView, PostDetailView, PostDeleteView
urlpatterns = [
    path('blog/', PostListView.as_view(), name='post_list'),
    path('blog/<pk>', PostDetailView.as_view(), name='post_detail'),
    path('blog/<pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]
