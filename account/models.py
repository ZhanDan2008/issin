import random
from uuid import uuid4
from .managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
# from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.dispatch import receiver
from django.db.models.signals import pre_save
STATUS_CHOISE=(
    ("Мужской","Man"),
    ("Женский","Woman"),
    ("Другое","Другой")
)
class CustomUser(AbstractUser):
    email = models.EmailField('email address',unique=True)
    gender = models.CharField(choices=STATUS_CHOISE,max_length=10,default='')
    password = models.CharField(max_length=255)
    activation_code = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=100,blank=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatars/default_avatar.jpg')
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
     )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return f'{self.email}'

    def create_activation_code(self):
        code = str(uuid4())
        self.activation_code = code

@receiver(post_save,sender=CustomUser)
def order(sender,instance,*args,**kwargs):
    a = instance.username
    d = CustomUser.objects.get(username=a)

