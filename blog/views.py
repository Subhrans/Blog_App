from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import SignUp,Login,ProfileForm,PostForm,ChangeProfilePicForm
from .models import Post,UserProfile
# Create your views here.

@login_required(login_url='/login/')
def index(request):
    posts = Post.objects.all()
    allpost = posts
    allposts = []
    liked = []
     # likes = Like.objects.filter(like_by__user=request.user)
    for i in posts:
        if i.like.filter(id=request.user.id).exists():
            liked.append(True)
        else:
            liked.append(False)
    print("checking liked or not",liked)
    # print(likes)
    for categories in allpost:
        if categories.category not in allposts:
            allposts.append(categories.category)
    return render(request, 'blog/home.html', context={'posts':posts,'allposts':allposts,'liked':liked})


def category_post_list(request,pk):
    posts = Post.objects.filter(category=pk).order_by('-creation_date')
    allpost = Post.objects.all()
    allposts = []

    for categories in allpost:
        # print("check", categories.category)
        if categories.category not in allposts:
            allposts.append(categories.category)
    print("catogories:",allposts)

    return render(request,'blog/category.html',{'posts':posts,'allposts':allposts})


def detailPost(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'blog/postdetail.html',{'post':post})


def signup(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            usersave = form.save()
            groups = Group.objects.get(name='Users')
            usersave.groups.add(groups)
            UserProfile.objects.create(user=usersave)

            return HttpResponseRedirect('/login/')

    else:
        form = SignUp(label_suffix=" ", auto_id=True)

    return render(request, 'blog/signup.html', {'form':form})


def loginView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            loginform = Login(request=request, data=request.POST)
            if loginform.is_valid():
                uname = loginform.cleaned_data['username']
                password = loginform.cleaned_data['password']
                validauth = authenticate(username=uname,password=password) # it returns none if user not found
                if validauth is not None:
                    login(request,validauth)
                    return HttpResponseRedirect('/')
            else:
                messages.error(request,'Invalid Id or Password')
        else:
            loginform = Login()

        return render(request,'blog/login.html',{'loginform':loginform})
    else:
        return HttpResponseRedirect('/')


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')


def Addpost(reqeust):
    if reqeust.user.is_authenticated:
        if reqeust.method == "POST":
            pf = PostForm(reqeust.POST,reqeust.FILES)
            if pf.is_valid():
                title = pf.cleaned_data['title']
                description = pf.cleaned_data['description']
                category = pf.cleaned_data['category']
                user = reqeust.user
                image = pf.cleaned_data['image']
                postdata = Post(title=title, description=description, user=user,category=category,image=image)
                postdata.save()
                return HttpResponseRedirect('/')

        else:
            pf = PostForm()
    else:
        return HttpResponseRedirect('/login/')
    return render(reqeust,'blog/add_post.html',{'postform':pf})

def updatePost(request,pk):
    if request.user.is_authenticated:
        getpost = Post.objects.get(pk=pk, user__username=request.user.username)
        if request.method == "POST":
            postupdateform = PostForm(request.POST, initial={
                "title": getpost.title,
                "description": getpost.description,
                "image": getpost.image,
                "category":getpost.category,
            },instance=getpost)
            if postupdateform.is_valid():
                postupdateform.save()
                return HttpResponseRedirect('/profile/'+request.user.username+'/')
        if request.method == "GET":
            postupdateform = PostForm(initial={
                "title":getpost.title,
                "description":getpost.description,
                "image":getpost.image,
                "category":getpost.category,
            })
            postid = getpost.id
            return render(request,'blog/add_post.html',context={'postupdateform':postupdateform,'postid':postid})
    else:
        return HttpResponseRedirect('/login/')

def deletePost(request,pk):
    if request.user.is_authenticated:
        post = Post.objects.get(user__username=request.user, pk=pk)
        if request.method == "POST":
            if post:
                post.delete()
                return HttpResponseRedirect('/profile/'+request.user.username+'/')
        if request.method == "GET":
            post_title = post.title
    else:
        return HttpResponseRedirect('/login/')
    return render(request,'blog/profile.html',{"post_title":post_title})


def likeview(request,pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            post = Post.objects.get(id=pk)
            if post.like.filter(id=request.user.id).exists():
                post.like.remove(request.user)
            else:
                post.like.add(request.user)
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')


def dashboard(request,pk):
    dash = ProfileForm()
    chpic = ChangeProfilePicForm()
    print(pk)
    userprofile = UserProfile.objects.get(user__username=pk)
    post_data = Post.objects.filter(user__username=pk)
    context = {"posts":post_data,'dashboard':dash, 'userprofile':userprofile, 'chpic':chpic}
    return render(request,'blog/profile.html',context)


def changeProfilePic(request):
    if request.method == 'POST':
        print(request.FILES)

        #  client file saved / update without using any form

        # here i used DropZone js

        profilepic = request.FILES['file']
        save_pic = UserProfile.objects.get(user=request.user)
        save_pic.profile_Image = profilepic
        save_pic.save()
        # return HttpResponseRedirect('/profile/'+str(save_pic.user)+"/")

    return render(request,'blog/profile.html')


def changeCoverPic(request):
    if request.method == "POST":
        cover_pic = request.FILES['file']
        save_pic = UserProfile.objects.get(user=request.user)
        save_pic.cover_Image = cover_pic
        save_pic.save()


    return render(request,'blog/profile.html')