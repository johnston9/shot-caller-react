"""
    Opened model
"""
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from departments.models import Department


class Opened(models.Model):
    """
    Opened model for Posts, related to 'owner' and 'post'.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='opens', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'


class OpenedDept(models.Model):
    """
    Opened model for Department and Latest posts, related to 'owner' and 'post'.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Department, related_name='opendept', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
