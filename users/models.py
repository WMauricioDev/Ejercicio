from django.db import models

# Create your models here.
class Tareas(models.Model):
    tareas =  models.CharField
    def __str__(self):
        return self.nombres