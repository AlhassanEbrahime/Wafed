from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager



class AppUserManager(BaseUserManager):
	def create_user(self,email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user


	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password)
        
		user.is_superuser = True
		user.save()
		return user



class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)  
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()
    def __str__(self):
            return self.username


class UserData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    college = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    

    
class Broker(models.Model):
    ### Rent ranges
    class_C = '1500-3000'
    class_B = '3000-5000'
    class_A = '5000-8000'
    
    RENT = [
        (class_A,'5000-8000'),
        (class_B,'3000-5000'),
        (class_C,'1500-3000')
    ]
    number_of_rooms = models.PositiveBigIntegerField()
    apartment_condition = models.CharField(max_length=255)
    rent = models.CharField(max_length=9,choices=RENT, default=class_C)
    comments = models.CharField(max_length=500)
    
    
          