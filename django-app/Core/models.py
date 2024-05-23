from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)


# class MyUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     # other fields here

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


class CadastroCliente(models.Model):
    nome = models.CharField(max_length=512, blank=True)
    email = models.EmailField(max_length=512, blank=False, unique=True)
    nasc = models.DateField(blank=True, null=True)
    cidade = models.CharField(max_length=512, blank=True)
    criado_por = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modificado_por = models.CharField(max_length=255, blank=True, null=True)
    modificado_em = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nome
