from django.db import models
from django.contrib.auth.models import User

LANGS = (
    ("py", "python"),
    ("js", "JavaScript"),
    ("cpp", "C++"),
)
class Langs(models.Model):
    #shot_name = models.CharField(max_length=8)
    name = models.CharField(max_length=32)
    icon = ...
    def __str__(self):
        return f" {self.name}"

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.ForeignKey(to=Langs, on_delete=models.PROTECT,
                            blank=True, null=True)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.PROTECT,
                             blank=True, null=True)
    private = models.BooleanField(default=True)

    def __str__(self):
        return f"Snippet {self.name} | {self.user}"

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name='comments')
