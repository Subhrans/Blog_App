from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import  views
app_name = "blog"
urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)