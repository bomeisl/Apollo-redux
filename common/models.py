from django.contrib.auth.models import User
from django.db import models


class Feed(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    tagline = models.CharField(max_length=100, default='', blank=True)
    author_username = models.CharField(max_length=60, default='', blank=True)
    body = models.CharField(max_length=300, default='', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    feed = models.ForeignKey(
        Feed,
        on_delete=models.CASCADE,
        default=None
    )


class Navbar(models.Model):
    page = models.CharField(max_length=100, default='home', blank=True)

    def __str__(self):
        return self.page


class NavBarItem(models.Model):
    label = models.CharField(max_length=100, default='', blank=True)
    url = models.CharField(max_length=100, default='', blank=True)
    nav_bar = models.ForeignKey(to=Navbar, on_delete=models.CASCADE, default=None)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.label