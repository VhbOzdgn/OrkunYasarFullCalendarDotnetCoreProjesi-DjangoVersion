from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class AppUser(AbstractUser):
    class Roles(models.TextChoices):
        SECRETARY = '1', _('Sekreter')
        DENTIST = '2', _('Hekim')

    is_dentist = models.BooleanField(verbose_name="Hekim mi", editable=False)
    color = models.CharField(max_length=20, unique=True, verbose_name="Renk", blank=True, null=True)
    role = models.CharField(
        choices=Roles.choices, verbose_name="Rol", max_length=1, default=Roles.SECRETARY)

    class Meta:
        db_table = "app_users"
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        return self.username
    
    def save(self, *args, **kwargs):
        self.is_dentist = self.role == self.Roles.DENTIST
        return super().save(*args, **kwargs)
