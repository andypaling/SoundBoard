from django.db import models
from PIL import Image
from django.contrib.auth.models import User


# Create your models here.
class SoundPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    sound = models.FileField(upload_to='sounds')
    image = models.ImageField(upload_to='images', default='images/default.png')
    title = models.CharField(max_length=20)
    adds = models.IntegerField(default=0)

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            img.thumbnail((100, 100))
            img.save(self.image.path)

    def __str__(self):
        return self.title


class UserSoundBoard(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sounds = models.ForeignKey(SoundPost, on_delete=models.CASCADE)

    def __str__(self):
        return 'User = ' + str(self.user) + ' | ' + 'Sound = ' + str(self.sounds)
