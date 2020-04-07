from django.db import models

# Create your models here.
class Account (models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username, self.password