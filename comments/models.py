from django.db import models


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    captcha = models.CharField(max_length=10)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='comment_images/', null=True, blank=True)
    file = models.FileField(upload_to='comment_files/', null=True, blank=True)

