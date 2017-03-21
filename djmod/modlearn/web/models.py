from django.db import models
from django.db.models import Model
from django.utils.encoding import smart_text
# Create your models here.

PUBLISH_CHOICES = (
    ('draft','Draft'),
    ('send','Send'),
)
class Post(Model):
    id =models.BigAutoField(primary_key=True)
    active = models.BooleanField(default= True) # can empty in the database
    title = models.CharField(max_length=240 , default='new post' ,verbose_name='post title')
    # add a verbose name to show a name on view but didnt change a name in database
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120,choices=PUBLISH_CHOICES , default='draft')
    view_count =models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False , auto_now_add=True)



    class Meta:
        verbose_name = 'postHa'
        verbose_name_plural = 'addPost'

    def __str__(self):
        return smart_text(self.title)
