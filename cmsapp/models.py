# from django.db import models
# from django.contrib.auth.models import User

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     content = models.TextField()
#     creation_date = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_public = models.BooleanField(default=True)

# class Like(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)



from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Like {self.id} for Post {self.post_id}"