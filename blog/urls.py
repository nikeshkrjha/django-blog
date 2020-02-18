from django.urls import path
from . import views
from .views import PostDetailView,PostCreateView,PostUpdateView

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('portfolio/', views.portfolio, name='blog-portfolio'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/new/', PostCreateView.as_view(), name='post-create')
]
