from django.db import models

# Create your models here.


class Payload(models.Model):
    passphrase = models.CharField()
    message = models.CharField()

   def __str__(self):
        return self.passphrase
    
