from django.db import models

# Create your models here.
class ViewAccount(models.Model):
    class Meta:
        db_table = "ViewAccount"

class EditAccount(models.Model):
    class Meta:
        db_table = "EditAccount"