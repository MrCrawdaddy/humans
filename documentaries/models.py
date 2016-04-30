from django.db import models
from django.contrib.auth import models as auth_model

class Documentary(models.Model):
    title = models.CharField(max_length=200)#required
    subject = models.CharField(max_length=100, blank=True, default="")
    length = models.DurationField(blank=True, default=0)
    date_uploaded = models.DateTimeField()#required
    description = models.TextField(blank=True, default="")
    contributor = models.ManyToManyField(auth_model.User, related_name='contributor_user')#required
    tags = models.CharField(max_length=200, blank=True, default="")
    location = models.CharField(max_length=100, blank=True, default="NA")
    state = models.CharField(max_length=2, blank=True, default="NA")
    file_location = models.URLField(max_length=200)#required
    likes = models.ManyToManyField(auth_model.User, related_name='like_user', blank=True, default=[])

    def __str__(self):
        return str(self.title)

