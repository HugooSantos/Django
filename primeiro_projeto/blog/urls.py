from django.urls import path
from . import views
urlpatterns = [
    path('', views.BlogListView.as_view(),name = 'home'),
    path('Post/new/', views.BlogCreateView.as_view(), name='Post_new'),
    path('Post/teste/', views.hello, name='hello'),
    path('Post/<slug:slug>/', views.BlogDetailView.as_view(), name='Post_detail'),
    path('Post/<int:pk>/edit', views.BlogUpdateView.as_view(), name='Post_edit'),
    path('Post/<int:pk>/delete', views.BlogDeleteView.as_view(), name='Post_delete'),

]
