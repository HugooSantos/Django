from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView ,DetailView,UpdateView, DeleteView
from django.views.generic.edit import CreateView
from . models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
@login_required
def hello(request):
    return HttpResponse('Olá mundo')
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/Post_detail.html"
    #context_object_name = 'custom'

class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/Post_new.html"

    success_message = "%(field)s - criado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )
class BlogUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/Post_edit.html"
    #fields = ('titulo','conteudo')
    success_message = "%(field)s - alterado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field=self.object.titulo,
        )
class BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    model = Post
    template_name = "blog/Post_delete.html"
    success_url = reverse_lazy('home')
    success_message = "excluído com sucesso"
    def delete(self,request,*args,**kwargs):
        messages.success(self.request,self.success_message)
        return super(BlogDeleteView,self).delete(request,*args,**kwargs)

