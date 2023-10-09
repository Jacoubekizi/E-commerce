from django.urls import path
from . import views
from django.contrib.auth import views as views_auth
urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views_auth.LoginView.as_view(template_name='register/login.html', next_page='store'), name='login'),
    path('logout/',views_auth.LogoutView.as_view(next_page='login') , name='logout'),
    path('change_password/', views.ChangePassword, name='changepassword')
]