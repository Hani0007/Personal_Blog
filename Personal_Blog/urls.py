from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name ='index'),
    path('about/', views.about , name ='about'),
    path('blog/', views.blog , name ="blog"),
    path('contact/', views.contact , name ="contact"),
    path('single/', views.single , name ="single"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
