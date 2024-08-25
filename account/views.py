from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# User ctrl tıkla   /  go to definition 
# AbstractUser  ctrl tıkla :  ordaki firts_name leri kullanıyoruz
def login_request(request):
            
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request,"account/login.html", { "error": "username ya da parolayanlış"})
        
        

    return render(request, "account/login.html")

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
                return render(request,"account/register.html",{"error":"username kullanılıyor"}) 
            else:
                if User.objects.filter(email=email).exists(): 
                    return render(request,"account/register.html",{"error":"email kullanılıyor"})
                else: 
                    # Kullanıcı oluşturma alanı : sonra login sayfasina yönlendirioz 
                    #create_user fonksiyonuna parametre veriyoruz
                    user = User.objects.create_user(username=username, email=email, first_name=firstname,
                                               last_name=lastname, password=password)
                    user.save()
                    return redirect("login")  #! kullanıcı giriş sayfasina yönlendirioz 
        else:
        # eşit değil ise sayfayi tekrar gönderioz
        # yaninda hata mesaji 
            return render(request, "account/register.html",{"eroor":"parola eşleşmiyor"})
    return render(request, "account/register.html")

def logout_request(request):
    return redirect("home")

