from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from authentication.models import Profile


class BookStore(models.Model):
    STATE = (
        ("available", "Available"),
        ("not_available", "Not Available"),
    )

    title = models.CharField("Title", max_length=50)
    description = models.TextField("Description", max_length=2000)
    # subscribed_users = models.ManyToManyField(User)
    availability = models.CharField(choices=STATE, max_length=20)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class NewsLetter(models.Model):
    title = models.CharField("title", max_length=50, null=True)
    description = models.TextField("Description", max_length=2000, null=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=NewsLetter)
def send_mail_func(sender, instance, created, **kwargs):
    print("workinggggggggggg")
    subject = instance.title
    body = instance.description

    profile = Profile.objects.filter(subscribed=True)
    for users in profile:
        user_obj = User.objects.filter(id=users.user.id)
        for us in user_obj:
            if created:
                send_mail(subject, body, 'shivamrawat829@gmail.com', [us.email,])


post_save.connect(send_mail_func, sender=NewsLetter)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# post_save.connect(create_profile, sender=User)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()