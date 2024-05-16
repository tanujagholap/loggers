from django.db import models


class Otp(models.Model):
    email = models.CharField(max_length=40)
    otp = models.CharField(max_length=40)

