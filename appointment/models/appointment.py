from django.db import models
from account.models import AppUser

class Appointment(models.Model):
    created_date = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Düzenlenme Tarihi", auto_now=True)
    start_date = models.DateTimeField(verbose_name="Başlangıç Tarihi")
    end_date = models.DateTimeField(verbose_name="Bitiş Tarihi")
    patient_name = models.CharField(max_length=30,verbose_name="Hasta Adı")
    patient_surname = models.CharField(max_length=30,verbose_name="Hasta Soyadı")
    description = models.TextField(max_length=500, verbose_name="Açıklama", blank=True, null=True)
    user = models.ForeignKey(AppUser, related_name="appointments", on_delete=models.CASCADE)

    class Meta:
        db_table = "appointments"
        verbose_name = "Randevu"
        verbose_name_plural = "Randevular"

    def patient_full_name(self):
        return f"{self.patient_name} {self.patient_surname}"