from django.contrib import admin
from .models import Post

class postAdmin(admin.ModelAdmin):
    class Meta:
        fields=[
            'title',
            'slug',
            'update',
            'timestamp'
        ]
        readonly_fields=['update','timestamp']
        model = Post
admin.site.register(Post ,postAdmin)
# Register your models here.
