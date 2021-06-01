from django.core.exceptions import RequestAborted
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager




class MyAccounManager(BaseUserManager):
    def create_user(self, name, phone_number, password = None):
        if not phone_number:
            raise ValueError('ggy')
        
        user = self.model(
            phone_number = phone_number,
            name = name,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password):
        user = self.create_user(
            phone_number = phone_number,
            name = name,
            password = password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    phone_number        = models.CharField(max_length=50, unique=True, verbose_name="Телефон номер")
    name                = models.CharField(max_length=50, verbose_name="Имя")

    date_joined         = models.DateTimeField(auto_now_add=True)
    last_login          = models.DateTimeField(auto_now_add=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_superadmin       = models.BooleanField(default=False)

    USERNAME_FIELD      = 'phone_number'
    REQUIRED_FIELDS     = ['name']

    objects = MyAccounManager()

    def __str__(self):
        return self.phone_number
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True


class forgotPassword(models.Model):
    name            = models.CharField(max_length=100, verbose_name="Имя")
    phone_number    = models.CharField(max_length=50, verbose_name="Телефон номер")

    def __str__(self):
        return self.phone_number

    
    