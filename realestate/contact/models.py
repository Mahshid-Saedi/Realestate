from django.db import models
from account.models import User
from django.urls import reverse

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    subject = models.CharField(max_length=300, verbose_name='عنوان')
    body = models.TextField(verbose_name='پیام')
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.slug}-{self.update}'

    def get_absolute_url(self):
        return reverse('contact:post_detail', args=(self.id, self.slug))

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomments')
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='pcomments')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    body = models.TextField(verbose_name='پیام')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.body[:30]}'

