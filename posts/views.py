from tokenize import Comment
from django.shortcuts import render, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_list(request):
    post_list = Post.objects.all().order_by('-published_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(post_list, 10) 
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'posts/post_list.html', {'posts': posts})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home') 
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



# Представление списка постов
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3
    

# Представление деталей поста
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

# Представление для создания поста
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'body', 'author', ]
    success_url = reverse_lazy('post_list')

# Представление для обновления поста
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'body', 'author', ]
    success_url = reverse_lazy('post_list')

# Представление для удаления поста
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

