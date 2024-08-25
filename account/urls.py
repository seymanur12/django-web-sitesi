from django.urls import path 
from . import views 

urlpatterns = [ 
    # login 
  path("login/", views.login_request, name ="login" ), 




  # register
  path("register", views.register_request, name ="register" ), 


  # logout 
  path("logout", views.logout_request, name ="logout" ), 

] 