from django.db import models

class OccasionMessage(models.Model):
    occasion = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    message = models.TextField()
    theme_color = models.CharField(max_length=7, default="#ff69b4")
    emojis = models.CharField(max_length=100, default="🎂🎈🎉")
    custom_image = models.ImageField(upload_to='occasion_images/', blank=True, null=True)

    def __str__(self):
        return self.occasion

class FriendWish(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(default="Happy Birthday! 🎂")
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name