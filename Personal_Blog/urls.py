
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name ='index'),
    path('about/', views.about , name ='about'),
    path('blog/', views.blog , name ="blog"),
    path('contact/', views.contact , name ="contact"),
    path('single/', views.single , name ="single"),

    
   

]

