from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=25)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(max_length=5)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-created']
    
class Media(models.Model):
    owner = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png')

    def __str__(self) -> str:
        name = str(self.image)
        return name[:-4]
