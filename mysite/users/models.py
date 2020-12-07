from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .conf import settings
from .managers import UserInheritanceManager, UserManager

from datetime import datetime
import json
import time


def birthday_filter(birthday):
    t = time.time()
    dt = datetime.fromtimestamp(t)
    b_year = birthday[:4]
    b_month = birthday[4:6]
    b_day = birthday[6:]
    age = int(dt.year) - int(b_year) - 1
    if int(b_month) > int(dt.month):
        if int(b_day) > int(dt.day):
            age += 1
    return age


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL

    email = models.EmailField(
        _('email address'), max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(
        _('active'), default=USERS_AUTO_ACTIVATE,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, editable=False)

    objects = UserInheritanceManager()
    base_objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = True

    def get_full_name(self):
        """ Return the email."""
        return self.email

    def get_short_name(self):
        """ Return the email."""
        return self.email

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.user_type_id:
            self.user_type = ContentType.objects.get_for_model(self, for_concrete_model=False)
        super(AbstractUser, self).save(*args, **kwargs)


class User(AbstractUser):

    """
    Concrete class of AbstractUser.
    Use this if you don't need to extend User.
    """

    name = models.CharField(max_length=20, default='第一次登陆')
    sex = models.CharField(max_length=2, default='男')
    birthday = models.CharField(max_length=30, default='1970-01-01')
    job_number = models.CharField(max_length=10, default='00001')

    political_landscape = models.CharField(max_length=10, default='群众')
    political_time = models.CharField(max_length=10, default='1970-01-01')

    job = models.CharField(max_length=30, default='工程师')
    job_time = models.CharField(max_length=20, default='1970-01-01')

    job_2 = models.CharField(max_length=30, default='员工')
    id_number = models.CharField(max_length=30, default='00001')
    schooling = models.CharField(max_length=30, default='本科')
    school = models.CharField(max_length=30, default='北京大学')
    graduate_time = models.CharField(max_length=30, default='1970-01-01')
    job_join_time = models.CharField(max_length=30, default='1970-01-01')
    team_belong = models.CharField(max_length=20, default='OOS')

    phone = models.CharField(max_length=11, default='17890987654')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.name

    def age(self):
        return birthday_filter(self.birthday)




