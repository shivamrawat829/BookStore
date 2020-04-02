from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BookStore(models.Model):
    STATE = (
        ("available", "Available"),
        ("not_available", "Not Available"),
    )

    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description", max_length=2000)
    # subscribed_users = models.ManyToManyField(User)
    availability = models.CharField(choices=STATE, max_length=20)

    def __str__(self):
        return self.title


class NewsLetter(models.Model):

    subscribed_users = models.ManyToManyField(User)

    def __str__(self):
        return self.id
