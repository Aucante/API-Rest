from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
