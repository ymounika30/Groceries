from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class Category(models.Model):
    category_name=models.SlugField(max_length=50,unique=True)
    slug=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='photos/categories/',blank=True)
    
    class Meta:
        verbose_name='category',
        verbose_name_plural='categories'
    
    # def __str__(self):
    #     self.category_name
        
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User must have an Email Address")
        if not username:
            raise ValueError("User must have an username ")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_super_user(self,first_name,last_name,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_super_admiin=True
        user.save(using=self.db)
        return user
    

class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    mobileno=models.CharField(max_length=50)
    
    #required
    date_joined=models.DateField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']
    objects=MyAccountManager()
    # def __str__(self):
    #     self.email
    def has_perm(self,obj=None):
        self.is_admin
    def has_module_perms(self,add_label):
        return True
    
class Product(models.Model):
    productname=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField()
    price=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_add_now=True)
    modified_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        self.productname
    