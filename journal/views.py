from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from .tables import PostTable
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig

def post_table(request):
    table = PostTable(Post.objects.all().order_by('published_date'))
    RequestConfig(request).configure(table)
    return render(request, 'journal/post_table.html', {'table': table})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'journal/post_detail.html', {'post': post})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_table')

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        new_or_edit = "New"
    return render(request, 'journal/post_edit.html', {'form': form, 'new_or_edit': new_or_edit})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_table')
    else:
        form = PostForm(instance=post)
        new_or_edit = "Edit"
    return render(request, 'journal/post_edit.html', {'form': form, 'new_or_edit': new_or_edit})
