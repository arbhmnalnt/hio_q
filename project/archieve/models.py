import datetime
from django.utils.timezone import now
from django.template.defaultfilters import slugify
from django.db import models
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    is_deleted      = models.BooleanField (default=False)
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True

class Ayada(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم العيادة")

    def __str__(self):
        return str(self.name)

class Visit(TimeStampMixin, models.Model):
    ayada   = models.ForeignKey(Ayada, on_delete=models.CASCADE, related_name='ayda', verbose_name="العيادة")
    count   = models.PositiveSmallIntegerField (null=True, blank=True)
    created_by    = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="مسئول الارشيف")

    def __str__(self):
        return "ت " + str(self.ayada.name)
