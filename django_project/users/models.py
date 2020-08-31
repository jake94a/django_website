from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # these are User fields, could include things like Bio or Location
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
