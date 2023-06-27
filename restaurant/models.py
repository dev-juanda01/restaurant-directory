from django.db import models

# Create your models here.

class Restaurant(models.Model):
  name = models.CharField("Nombre", max_length=200, null=False, blank=False)
  description = models.TextField("Descripción", null=False, blank=False)
  direction = models.CharField("Dirección", max_length=255, null=False)
  image = models.URLField("Imagen", max_length=255, null=False, blank=False)

  def __str__(self):
      return self.name
  
  class Meta:
    verbose_name = "Restaurant"
    verbose_name_plural = "Restaurants"
    ordering = ["name"]