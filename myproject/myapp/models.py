from django.db import models

# # Create your models here.
from django.db import models

class User(models.Model):
    use_in_makemigrations = True
    userid = models.CharField(primary_key=True, max_length=50)
    userpw = models.CharField(max_length=50)
    username = models.TextField()
    hp = models.TextField()
    email = models.TextField()
    gender = models.TextField()

    class Meta:
        db_table = 'member'
        app_label = 'main'