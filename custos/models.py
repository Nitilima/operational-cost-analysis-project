from django.db import models

# Create your models here.

class Cost(models.Model):
    categoria = models.CharField(max_length=255)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return f"{self.categoria} - R$ {self.valor} - {self.data}"