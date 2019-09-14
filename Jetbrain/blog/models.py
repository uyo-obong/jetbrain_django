from PIL import Image
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.admin import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 370 or img.width > 700:
            resize_image = (370, 700)
            img.thumbnail(resize_image)
            img.save(self.image.path)

        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

