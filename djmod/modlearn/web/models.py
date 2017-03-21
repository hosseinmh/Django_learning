from django.db import models
from django.db.models import Model
# Create your models here.


class Post(Model):
    id =models.BigAutoField(primary_key=True)
    active = models.BooleanField(default= True) # can empty in the database
    title = models.CharField(max_length=240 , default='new post' ,verbose_name='post title')
    # add a verbose name to show a name on view but didnt change a name in database
    content = models.TextField(null=True , blank=True)
    pass

