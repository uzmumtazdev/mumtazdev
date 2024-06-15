from django.shortcuts import render, redirect
from .models import Post, Comment
from django.views.generic import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import MyForm
from django.core.paginator import Paginator
# Create your views here.
def list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 7)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data = {
        'page_obj': page_obj
    }
    return render(request, 'list.html', data)

def detail(request, pk):
    post = Post.objects.get(id=pk)
    author = post.author
    username = request.user.username
    if request.method == 'POST':
        if request.POST['n_comment']:
            n_comment = request.POST['n_comment']
            a_comment = request.user
            Comment.objects.create(name=post, author=a_comment, comment=n_comment)
            redirect('/post/'+str(post.pk)+'/')
    data = {
        'post': post,
        'username': str(username),
        'author': str(author),
    }
    return render(request, 'detail.html', data)

@login_required
def delete(request, pk):
    post = Post.objects.get(id=pk)
    if str(post.author) == str(request.user.username):
        post.delete()
        return redirect('/')
    else:
        return redirect('/post/'+str(post.pk)+'/')

class Edit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'summary', 'body', 'image')
    template_name = 'edit.html'
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

@login_required
def post(request):
    form = MyForm()
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        summary = request.POST['summary']
        image = request.FILES.get('image', '')
        user = request.user
        Post.objects.create(title=title, summary=summary, body=body, image=image, author=user)
        return redirect('home')
    return render(request, 'post.html', {'form': form})

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', None)
        posts = Post.objects.filter(title__icontains=query)
        return render(request, 'list.html', {"page_obj": posts})
    else:
        return render(request, 'list.html')

