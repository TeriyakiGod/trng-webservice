from django.db import models

class Generator(models.Model):
    ip = models.GenericIPAddressField()
    country = models.CharField(max_length=100, default="Unknown")
    city = models.CharField(max_length=100, default="Unknown")
    online = models.BooleanField(default=False)