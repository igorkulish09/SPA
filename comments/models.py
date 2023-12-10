from django.db import models


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    captcha = models.CharField(max_length=10)
    text = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

