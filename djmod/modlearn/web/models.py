from django.db import models
from django.db.models import Model
from django.utils.encoding import smart_text
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify

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
    slug = models.SlugField(null=True , blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.IntegerField(default=0)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email = models.EmailField(max_length=240, null=True, blank=True, validators=[auther_email])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        # print("here")
        # self.title = 'the title is changed '
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'postHa'
        verbose_name_plural = 'addPost'
        # unique_together = [('active' , 'title')]

    def __str__(self):
        return smart_text(self.title)
