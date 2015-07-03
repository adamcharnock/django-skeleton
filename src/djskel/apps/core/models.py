from django.conf import settings
from django.db import models
from django_smalluuid.models import SmallUUIDField, uuid_typed_default


class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    uuid = SmallUUIDField(default=uuid_typed_default(type=1))
    slug = models.SlugField(unique=True, max_length=40)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    blog_url = models.URLField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.slug
