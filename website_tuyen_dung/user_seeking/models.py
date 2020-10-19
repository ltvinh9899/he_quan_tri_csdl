from django.db import models

# Create your models here.

class user_account(models.Model):
    id_user = models.IntegerField(max_length=20)
    user_type_id = models.IntegerField(max_length=10)
    email_user = models.EmailField(max_length=255)
    password_user = models.CharField(max_length=255)



