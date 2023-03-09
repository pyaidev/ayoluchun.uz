from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.safestring import mark_safe
from django.db import models
from django.core.validators import RegexValidator
from .regex import imkon_regex, linkden_regex, telegram_regex, facebook_regex
from .choosen import GENDER


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if username is None:
            raise TypeError('Phone did not come')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        if not username:
            raise TypeError('Password did not come')
        user = self.create_user(username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_sponsor = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Name')
    surname = models.CharField(max_length=50, blank=True, null=True, verbose_name='Surname')
    patronymic = models.CharField(max_length=50, blank=True, null=True, verbose_name='Patronymic')
    username = models.CharField(max_length=255, blank=True, unique=True, verbose_name='Phone')
    phone = PhoneNumberField(region='UZ')
    email = models.EmailField(max_length=255, blank=True, null=True, verbose_name='Email')
    email_is_verified = models.BooleanField(default=False, verbose_name='Email is verified')
    paid_course = models.ManyToManyField('courses.Course', blank=True, related_name='paid_course',
                                         verbose_name='Paid course')
    complete_course = models.ManyToManyField('courses.Course', blank=True, related_name='complete_course',
                                             verbose_name='Complete course')
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser")
    is_staff = models.BooleanField(default=False, verbose_name="Admin")
    is_active = models.BooleanField(default=True)
    date_login = models.DateTimeField(auto_now=True, verbose_name='Date login')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date created')

    objects = AccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
        return data


class Speciality(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.title


class Region(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile', verbose_name='User')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Bio')
    image = models.ImageField(upload_to='profile/', null=True, blank=True, verbose_name='Image')
    gender = models.CharField(max_length=211, choices=GENDER, blank=True, verbose_name='Gender')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Country')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Region')
    zip_code = models.CharField(max_length=30, blank=True, verbose_name='Zip code')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Birth date')
    workplace = models.CharField(max_length=255, blank=True, verbose_name='Workplace')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, null=True, blank=True,
                                   verbose_name='Speciality')
    imkon_profile = models.CharField(max_length=255, validators=[RegexValidator(regex=imkon_regex)], blank=True,
                                     verbose_name='Imkon profile')
    facebook_profile = models.CharField(max_length=255, validators=[RegexValidator(regex=facebook_regex)], blank=True,
                                        verbose_name='Facebook profile')
    telegram_profile = models.CharField(max_length=255, validators=[RegexValidator(regex=telegram_regex)], blank=True,
                                        verbose_name='Telegram profile')
    linkden_profile = models.CharField(max_length=255, validators=[RegexValidator(regex=linkden_regex)], blank=True,
                                       verbose_name='Linkden profile')

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'

    def __str__(self):
        return self.username
