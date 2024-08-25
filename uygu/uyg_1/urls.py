from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

 # ana sayfa
    path('', views.home, name="home"),
    path('ü/', views.ü, name="ü"),
    path('h/', views.h, name="h"),
    path('i/', views.i, name="ii"),
    path('f/', views.f, name="ff"),
    # login 
    path('login/', views.login_request, name="e"),
    path('in/', views.login_request, name="innn"),
    path('in/profil_1/<str:username>/', views.profil_1, name='profil_1'),  # Kullanıcı adını ekledik
    path("login/", views.login_request, name ="login" ), 
  # register
    path("register", views.register_request, name ="register" ), 
  # logout 
    path("logout", views.logout_request, name ="logout" ), 
    path('profil/<str:username>/', views.profil_1, name='profil_1'),
    # login logout.html
    path('in/profil_1.html', views.profil_s, name='profil_s'),
    path('in/profil_1/<str:username>/', views.profil_s, name='profil_s'),
    path('profil/<str:username>/', views.profil_s, name='profil'),
    path('in/profil_1/<str:username>/', views.profil_1, name='profil_1'),
# çıkış
    path('outtt', views.out,  name='outtt'),
# kayit ol 
    path('register/', views.rrr, name="rrr"),
    # ürün detay sayfası
    path('urunler/', views.ü, name='urunler_listesi'),

    path('ürün_detay/<str:ürün_id>/', views.urun_detay, name='urun_detay'),
    path('profil_12.html', views.profil_12, name='profil_12'),
    path('profil_like.html', views.profil_like, name='profil_like'),
    path('profil_save.html', views.profil_save, name='profil_save'),
 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ADMIN PANELİNDE:
admin.site.site_title = 'Extreme Başlık'
admin.site.site_header = 'Extreme admin portalı'
admin.site.index_title = 'Yönetici portalına hoş geldiniz'
