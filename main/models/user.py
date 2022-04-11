from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from model_utils.managers import InheritanceManager

from . import Profile


class EmailUserManager(BaseUserManager, InheritanceManager):
    "Inheriting InheritanceManager helps deciding which usertype has some user we get (e. g. from request)"

    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.profile = Profile.objects.create()
        user.role = self.model.default_role
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class EmailUser(AbstractUser):

    USERNAME_FIELD = 'email'

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="user")
    username = models.CharField(max_length=30, default='user')
    email = models.EmailField('email address', unique=True)  # changes email to unique and blank to false

    role = models.TextField(default=Profile.NO_ROLE, max_length=30, choices=Profile.roles_repr.items())

    default_role = Profile.NO_ROLE

    objects = EmailUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.profile) if hasattr(self, 'profile') else 'noprofile'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def concretize(self):
        "return inherited version of self"
        return EmailUser.objects.get_subclass(id=self.id)


class StudentUser(EmailUser):
    default_role = Profile.STUD_ROLE

    class Meta:
        verbose_name = 'StudentUser'


class LecturerUser(EmailUser):
    default_role = Profile.LECT_ROLE

    class Meta:
        verbose_name = 'LectorUser'


@receiver(post_delete, sender=EmailUser)
def auto_delete_profile(sender, instance, **kwargs):
    instance.profile.delete()
