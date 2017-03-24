from django.db import models
from django.db.models import Model
from django.utils.encoding import smart_text
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

from .validators import auther_email

# Create your models here.

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('send', 'Send'),
)


class Post(Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)  # can empty in the database
    title = models.CharField(max_length=240, default='new post', verbose_name='post title', unique=True)

    # add a verbose name to show a name on view but didnt change a name in database
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, null=True, blank=True, validators=[auther_email])

    def save(self, *args, **kwargs):
        # if not self.slug:
        #     if self.title:
        #         self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'postHa'
        verbose_name_plural = 'addPost'
        # unique_together = [('active' , 'title')]

    def __str__(self):
        return smart_text(self.title)

#
# def post_save_receiver():
#     pass


def post_save_receiver(sender, instance, created , *args , **kwargs):

    if created:
        print("in recieiver")
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)
            instance.save()

post_save.connect(post_save_receiver, sender=Post)

def post_pre_save_reciever(sender,instance,*args,**kwargs):
    print("before save")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)
        instance.save()
pre_save.connect(post_pre_save_reciever ,sender=Post)