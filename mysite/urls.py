# mysite/urls.py
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth

urlpatterns = [
    path('', auth.LoginView.as_view(template_name="chat/login.html"), name="login"),
    path('logout/', auth.LogoutView.as_view(next_page="/"), name="logout"),
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]
