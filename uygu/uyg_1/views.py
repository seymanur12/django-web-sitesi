from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponseRedirect
from uyg_1.models import Blog   # Blog classini aldik
from .models import Ürün, Category 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import Settingg


def home(request):
     
    context = {
      "blogs" : Blog.objects.all(),
      # from ... Category
      # models.py deki 
      "categories" :  Category .objects.all()
      # category nin .objects.all 
      }
    return render(request, "blog/ana_s.html" , context)




def h(request):
   return render(request,"blog/hakkinda.html" )
def ü(request):

   urunler = Ürün.objects.all()  # Doğru model adınızı kullanarak tüm ürünleri alıyoruz
   for urun in urunler:
    print(urun.isim)  # Ürünün ismini yazdır
    print(urun.ozellikler)  # Ürünün özelliklerini yazdır
    print(urun.fiyat)  # Ürünün fiyatını yazdır
    print(urun.id)
   context = {'urunler': urunler}  # Context'i oluşturuyoruz
   # Ürünlerin listelendiği sayfayı gösteriyoruz
   return render(request, "blog/ürünler.html", context)

def out(request):
    logout(request)
    return redirect("a")


def profil_1(request, username ):
   user = User.objects.get(username=username)
   profil = Profil.objects.get(user_id=user.id)
   context = { "profil" : profil }
   return render(request, "blog/profil_1.html", context)

def profil_s(request, username ):
    
   username = User.objects.get(username=username)
      # Kullanıcının profil sayfasını oluşturmak için kullanıcı verisini şablonla birlikte render et
   return render(request, 'profil_sablonu.html', username)


def profil_12(request):
   

   return render(request, "blog/profil_12.html")

def profil_like(request):
   return render(request, "blog/profil_like.html")
def profil_save(request):
   return render(request, "blog/profil_save.html")
def i(request):
   return render(request,"blog/iletisim.html" )
def f(request):
   return render(request,"blog/forum.html" )
# account/ templates/ account içindeki: login ve register sayfalari
def ll(request):
   return render(request,"blog/login.html" )
def rrr(request):
   return render(request,"blog/register.html" )
# from .models import Ürün  
# ürün detay sayfasi. urls.py 
# ürünlerden gelecek olan ürün_id
def urun_detay(request , ürün_id ):
   # ürün_id ile veritabanindan ilgili ürünü aliyoruz
   ürün = get_object_or_404(Ürün, id = ürün_id )

   # gönderiyoruz
   return render(request,"blog/ürün_detay.html" , {'ürün': ürün }) 
   # return render(request,"blog/ürün_detay.html" , {'ürün': ürün }) 

#! LOGİN
# User ctrl tıkla   /  go to definition 
# AbstractUser  ctrl tıkla :  ordaki firts_name leri kullanıyoruz
def login_request(request):
            
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None: # başarılı ise
            login(request, user)
            return redirect("a/")
        else:
            return render(request,"blog/login.html", { "error": "username ya da parolayanlış"})
        
        

    return render(request, "blog/login.html")

def register_request(request):
    if request.method =="POST": 
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]   

        # password ile repasssword eşit ise. eşit değil ise sayfayi tekrar gönderioz
        # yaninda hata mesaji 
        if password ==repassword:
            # kontrol edilcek diğer şeyler : 
            # username bilgisi daha önce var mı 
            # 
            if User.objects.filter(username=username).exists():
                return render(request,"blog/register.html",{"error":"username kullanılıyor"}) 
            else:
                if User.objects.filter(email=email).exists(): 
                    return render(request,"blog/register.html",{"error":"email kullanılıyor"})
                else: 
                    # Kullanıcı oluşturma alanı : sonra login sayfasina yönlendirioz 
                    #create_user fonksiyonuna parametre veriyoruz
                    user = User.objects.create_user(username=username,first_name=firstname, last_name=lastname,
                                                     email=email, 
                                               password=password)
                    user.save()
                    return redirect("login")  #! kullanıcı giriş sayfasina yönlendirioz 
        else:
        # eşit değil ise sayfayi tekrar gönderioz
        # yaninda hata mesaji 
            return render(request, "blog/register.html",{"error":"parola eşleşmiyor"})
    return render(request, "blog/register.html")

def logout_request(request):
    return redirect("home")

