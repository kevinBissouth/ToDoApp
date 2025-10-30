from django.db import models

class Tache(models.Model):
    tache = models.CharField(max_length=100)

    def __str__(self):
        return self.tache
