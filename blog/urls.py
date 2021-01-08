from django.urls import path

from . import  views
app_name = "blog"
urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('profile/<str:pk>/',views.dashboard,name="profile"),
    path('add_post/',views.Addpost,name="add_post"),
    path('postdetail/<int:pk>/',views.detailPost,name='postdetail'),
    path('changeprofilepic/',views.changeProfilePic,name="changepropic"),

    # path('add_post/<str:pk>/',views.Addpost,name="add_post"),
]