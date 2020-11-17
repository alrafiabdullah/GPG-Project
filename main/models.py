from django.db import models

# Create your models here.


class Payload(models.Model):
    passphrase = models.CharField(max_length=256)
    message = models.TextField(max_length=8192)
    decrypted_message = models.CharField(max_length=8192)

    def __str__(self):
        return self.passphrase
