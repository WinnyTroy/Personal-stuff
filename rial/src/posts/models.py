from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.FileField(upload_to="photos/%Y/%m/%d",
                             null=True,
                             blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def create_slug(self, instance, new_slug=None):
        slug = slugify(instance.title)
        if new_slug is not None:
            slug = new_slug

        qs = Post.objects.filter(slug=slug).order_by("-id")
        exists = qs.exists()

        if exists:
            new_slug = "%s-%s" % (slug, qs.first().id)
            return self.create_slug(self, instance, new_slug=new_slug)
        return slug

    @classmethod
    def pre_save_post_receiver(cls, sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = Post.create_slug(instance, instance)


pre_save.connect(Post.pre_save_post_receiver, sender=Post)
