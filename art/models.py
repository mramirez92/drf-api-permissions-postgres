from django.db import models
from django.contrib.auth import get_user_model


class Art(models.Model):
    person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    artist = models.CharField(max_length=128)
    artwork_name = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'"{self.artwork_name}" by {self.artist}'

