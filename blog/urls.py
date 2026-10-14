from django.urls import path
from .views import (
	BlockListView,
  BlogDetailView,
	BlogCreateView,
	BlogUpdateView,
	BlogDeleteView
	)

urlpatterns = [
	path('', BlockListView.as_view(), name='home'),
	path('posts/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
	path('posts/new', BlogCreateView.as_view(), name='post-new'),
	path('posts/<int:pk>/edit', BlogUpdateView.as_view(), name='post-edit'),
	path('posts/<int:pk>/delete', BlogDeleteView.as_view(), name='post-delete')
]