from django.urls import path
from .views import NewsListView, NewsUpdateView, NewsDeleteView, NewsCreateView, ArticleView, HomePageView
urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('', NewsListView.as_view(), name='article_list'),
    path('new/', NewsCreateView.as_view(), name='news_new'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('<int:pk>/', ArticleView.as_view(), name='article_detail'),
]
