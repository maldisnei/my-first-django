from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import PostForm,CommentForm
from .models import Comment,Sobre_mim
from django.contrib.auth.decorators import login_required
def post(request):
	
	postes = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

	
	
	return render(request,'blog/post.html',{'postes':postes})



def detail(request, slug):
	post = get_object_or_404(Post,slug=slug)

	return render(request,'blog/detail.html',{'post':post})

def post_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.auth=request.user
			
			form.save()
			return redirect('blog.views.detail',slug=post.slug)
	else:
		form=PostForm()
	return render(request,'blog/post_new.html',{"form":form})

@login_required
def remove(request,slug):
	post=get_object_or_404(Post,slug=slug)
	post.delete()
	
	return redirect('blog.views.post')

def post_edit(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		form = PostForm(request.POST,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.auth=request.user
			
			form.save()
			return redirect("blog.views.detail", slug=post.slug)
	else:
		form=PostForm(instance=post)
	return render(request,'blog/post_new.html',{'form':form})

def comments(request,slug):
	post = get_object_or_404(Post,slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.poste = post

			comment.save()

			return redirect('blog.views.detail', slug=post.slug)
	else:
		form = CommentForm()
	return render(request,'blog/add_comment.html',{'form':form})
	return render(request,'blog/detail.html',{'comments':comments})

@login_required
def comment_approve(request,pk):
	comment=get_object_or_404(Comment,pk=pk)
	comment.approved()
	return redirect('blog.views.detail', slug=comment.poste.slug)
@login_required
def comment_remove(request,pk):
	comment=get_object_or_404(Comment,pk=pk)
	post_comment= comment.poste.slug
	comment.delete()
	return redirect('blog.views.detail', slug=post_comment)

def posts_rascunho(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request,'blog/posts_rascunho.html',{'posts':posts})

def post_published(request,slug):
	post=get_object_or_404(Post,slug=slug)
	post.publish()

	return redirect('blog.views.post')
def sobre_mim(request):
	sobre_auth=Sobre_mim.objects.get(id=1)
	return render(request,'blog/sobre_mim.html',{'sobre_auth':sobre_auth})
