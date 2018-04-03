from django.db import models
from django.utils.text import Truncator
from accounts.models import UserProfile
from threads.models import Thread


class Post(models.Model):
    """ Model to represent the post in a thread """
    content = models.TextField(max_length=4000)
    thread = models.ForeignKey(Thread, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    creator = models.ForeignKey(UserProfile, related_name='posts')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        truncated_content = Truncator(self.content)
        return truncated_content.chars(30)
