from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("myapp.urls")),
    path('', include("tasks.urls")),
    path('', include("userprofile.urls")),
    path('', include("notifications.urls")),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(template_name="myapp/login.html"), name="login"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
