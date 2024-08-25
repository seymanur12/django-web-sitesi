from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


# oluşturulan modeller :  admin.py de tanıtılmali . 
# Create your models here.
class Foo(models.Model):
   content = RichTextField()

class Blog(models.Model): 

    title = models.CharField(max_length=200, default='default_title')
    image = models.CharField(max_length=50)
    description = models.TextField( default="")
    is_active = models.BooleanField()
    is_home = models.BooleanField()


class Category(models.Model): 
    STATUS = (
        ('True', 'Evet'),
        ('False' , 'Hayır'),
    )
    title = models.CharField(max_length=30, default='default_title')
    keywords = models.CharField(max_length=255, default="default_keywords")

    description = models.CharField(max_length=255, default="")
    image = models.ImageField(blank=True , upload_to='Post-İmage/')
    status = models.CharField(max_length=10, choices=STATUS, default='default_status')
    
    slug = models.SlugField(default="default-slug")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Post-İmage")
    baslik = models.TextField( default='default_title')
    description = models.TextField( default="")
    # postu beğenenler, kaydedenler
    likes = models.ManyToManyField(User, related_name="Beğenenler")
    post_save = models.ManyToManyField(User, related_name="Kaydedenler")
    eklenme_tarihi = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.baslik 
    
class Product(models.Model): 
    STATUS = ((True, 'Evet'), (False,'Hayır'))
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='default_title')

    keywords = models.CharField(max_length=255, default="default_keywords")
    description = models.CharField(max_length=255, default="")

    image = models.ImageField(blank=True, upload_to='Post-İmage/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()

    def __str__(self):
        return self.title



class Settingg(models.Model): 
    title = models.CharField(max_length=150, default='default_title')
    keywords = models.CharField(max_length=255, default="default_keywords")
    descriptions = models.CharField(max_length=255, default="")
    email = models.CharField(blank=True, max_length=15)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail =  models.CharField(blank=True,max_length=20)
    smtppassword =  models.CharField(blank=True,max_length=10)
    smtpport =  models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images')

    facebook = models.CharField(blank=True,max_length=50)
    ins = models.CharField(blank=True,max_length=50)
    twit = models.CharField(blank=True,max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    def __str__(self):
        return self.title

# BİRDEN FAZLA RESSİm, bir ürüne 
class Images(models.Model): 
    product = models.CharField(max_length=50)
   
    image = models.ImageField(blank=True, upload_to='im')
    def __str__(self):
        return self.title
 
class Ürün(models.Model):
    isim = models.CharField(max_length=100, default='default_title')
    ozellikler = models.CharField(max_length=100, default='default')
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    gorsel = models.ImageField(upload_to='product_images', default='default')  # Ürün görseli için ImageField ekledik
    def __str__(self):
        return self.isim

# FORM SİTESİ     

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date= models.DateTimeField(auto_now_add=True)

# KULLANICI PROFİLİ   
class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Profil-İmage")
    bio = models.TextField()
#user = User.objects.get(username=username)
# profil = Profil.objects.get(user_id=user.id)

class Takip(models.Model):
    profil = models.ForeignKey(Profil, related_name="takipci_profil",  on_delete=models.CASCADE)
    takip_edilen = models.ForeignKey(Profil, related_name="takip_edilen",  on_delete=models.CASCADE)

class Takipci(models.Model):
    profil = models.ForeignKey(Profil, related_name="takip_profil" ,  on_delete=models.CASCADE)
    takip_eden = models.ForeignKey(Profil, related_name="takip_eden" , on_delete=models.CASCADE)


class Kayitettiklerim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Beğendiklerim(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Kayitedenler(models.Model): 
    # Postu kayit edenler 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

