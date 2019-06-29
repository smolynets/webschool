from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    video_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
