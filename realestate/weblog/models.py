from django.db import models

class BlogModel(models.Model):
    title = models.CharField()
    question = models.TextField()
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.title}'


