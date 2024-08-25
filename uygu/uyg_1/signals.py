from django.contrib.auth.models import User # Hazır User modelimiz 
from .models import *  # Profil Modelini alıyoruz
from django.db.models.signals import post_save 
from django.dispatch import receiver 
# receiver dinleyici 
@receiver(post_save, sender=User) 
# User modelinde save olur ise , gel burdaki fonksiyonu çalıştır: 
def create_profile(sender, instance, created, **kwargs):
    if created: 
        Profil.objects.create(user=instance)
        # objects.create ile Profili oluşturuyoruz 
    # Register Modelindeki, user değişkeni = instance 'dir
    #