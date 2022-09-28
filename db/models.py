import sys
from urllib.parse import MAX_CACHE_SIZE

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class Malumotlar(models.Model):
    full_name = models.CharField(max_length=500)
    phone =  models.CharField(max_length=500)
    who =  models.CharField(max_length=500)
    bolim =  models.CharField(max_length=500)
    kimga =  models.CharField(max_length=500)
    text = models.TextField()
    chat_id  =  models.PositiveBigIntegerField()
    data = models.DateField(auto_now= True)



    def __str__(self):
        return self.full_name

