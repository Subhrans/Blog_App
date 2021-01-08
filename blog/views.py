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
    return render(request, 'blog/home.html', context={'posts':posts})


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
                user = reqeust.user
                image = pf.cleaned_data['image']
                postdata = Post(title=title, description=description, user=user, image=image)
                postdata.save()
                return HttpResponseRedirect('/')

        else:
            pf = PostForm()
    else:
        return HttpResponseRedirect('/login/')
    return render(reqeust,'blog/add_post.html',{'postform':pf})

def dashboard(request,pk):
    dash = ProfileForm()
    chpic = ChangeProfilePicForm()
    userprofile = UserProfile.objects.get(user__username=pk)
    post_data = Post.objects.filter(user__username=pk)
    context = {"posts":post_data,'dashboard':dash, 'userprofile':userprofile, 'chpic':chpic}
    return render(request,'blog/profile.html',context)


def changeProfilePic(request):
    if request.method == 'POST':
        chpic = ChangeProfilePicForm(request.POST, request.FILES)
        if chpic.is_valid():
            chpic.save()
    else:
        chpic = ChangeProfilePicForm()
    return render(request,'blog/profile.html', {'chpic':chpic})
