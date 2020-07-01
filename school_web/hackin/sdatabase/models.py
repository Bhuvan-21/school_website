from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self,full_name,contact,mother,father,email, password= None,is_active=True, is_staff=False, is_admin=False,is_manager=False):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not password:
            raise ValueError('Users must have a full name')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            mother=mother,
            father=father,
            contact=contact,
        )

        user.set_password(password)
        user.staff=is_staff
        user.admin=is_admin
        user.save(using=self._db)
        return user
    def create_staffuser(self, email,full_name,contact,mother,father, password):
            user = self.create_user(
            full_name,
            contact,
            mother,
            father,
            email,
            password,
            is_staff=True
            )
            user.save(using=self._db)
            return user
    def create_superuser(self,full_name,contact,mother,father,email,password):
            user = self.create_user(
            full_name,
            contact,
            mother,
            father,
            email,
            password,
            is_staff=True,
            is_admin=True
            )
            user.save(using=self._db)
            return user

class CustomUser(AbstractBaseUser):
    email= models.EmailField(unique= True,max_length= 255,)
    full_name=models.CharField(max_length=50, unique= False)
    staff=True
    admin=False
    contact=models.CharField(unique=True,max_length=10)
    mother=models.CharField(max_length=50, unique= False)
    father=models.CharField(max_length=50, unique= False)
    USERNAME_FIELD= 'email'

    REQUIRED_FIELDS=['full_name','contact','father','mother',]
    objects=UserManager()

    def get_full_name(self):
        return self.full_name

    def get_contact(self):
        return self.contact

    def get_mother(self):
        return self.mother

    def get_father(self):
        return self.father

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
