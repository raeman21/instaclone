from django.conf.urls import url
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    url('home/', PostListView.as_view(), name='blog-home'),
    url('post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url('about/', views.about, name='blog-about'),
]
