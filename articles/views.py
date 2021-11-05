from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Article
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    model = Article


class NewsListView(ListView):
    template_name = "article_list.html"
    model = Article


class ArticleView(DetailView):
    template_name = "article_detail.html"
    model = Article


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "news_new.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "news_update.html"
    fields = ["title", "body", "picture"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "news_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
