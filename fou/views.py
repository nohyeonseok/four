from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Portfolio, Comment
from .forms import NewBlog, CommentForm
# Create your views here.

def home(request):  #crud들어가는 곳
    return render(request, 'home.html')

def new(request): # 본모델 보여주는곳
    blogs = Portfolio.objects.all()  #모델전부전택
    return render(request, 'new.html',{'blogs':blogs})

def detail(request, pk):  #선택된 모델의 전체부분을 보여주는 페이지
    post = get_object_or_404(Portfolio, pk = pk)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context) 

def create(request):
    
    if request.method =="POST":
        form = NewBlog(request.POST, request.FILES) #request.FILES: 이미지,파일 전송때 필요
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('new') 
    
    else :
        form = NewBlog()
        return render(request, 'create.html', {'form':form})

def update(request, pk):
    # 어떤 블로그를 수정할지 객체 갖고오기
    blog = get_object_or_404(Portfolio, pk = pk)
    # 해당하는 블로그 번호(pk)에 맞는 입력공간 
    form = NewBlog(request.POST, request.FILES, instance=blog)
    
    if form.is_valid():
        form.save()
        return redirect('new')

    return render(request, 'create.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Portfolio, pk = pk)
    blog.delete()
    return redirect('new')

#댓글
def comment(request,post_pk):
    post = get_object_or_404(Portfolio, pk=post_pk)
      #몇번째 본문
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():  #유효성검사
            comment = form.save(commit=False)  #중복저장방지
            comment.post = post  #어디 달건지 저장   
            comment.save()
            return redirect('new') 
    
    else :
        form = CommentForm()
        return render(request, 'create.html', {'form':form})
#수정
def upda(request, post_pk):
    pos = get_object_or_404(Comment, pk=post_pk)  #몇번째 댓글 지정

    if request.method =="POST":
        form = CommentForm(request.POST, instance=pos)
        if form.is_valid():  
            comment = form.save(commit=False) 
            comment.save()
            return redirect('new') 
    
    else :
        form = CommentForm()
        return render(request, 'create.html', {'form':form})
#삭제
def dele(request,post_pk):
    comment = get_object_or_404(Comment, pk = post_pk)
    comment.delete()
    return redirect('new')

