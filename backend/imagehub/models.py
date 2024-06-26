from django.contrib.postgres.fields import ArrayField
from django.db import models
from users.models import Account


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Tag(models.Model):
    tag = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.tag


class Post(models.Model):
    user = models.ForeignKey(Account, related_name='posts', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=45)
    description = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    tag = models.ForeignKey(Tag, related_name='post_tag', on_delete=models.SET_NULL, null=True)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='commented_by', on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment_text


class Subcomment(models.Model):
    parrent_comment = models.ForeignKey(Comment, related_name='subcomment_parent', on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, related_name='subcomment_post', on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name='subcomment_user', on_delete=models.CASCADE)
    comment_text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.comment_text


class PostLike(models.Model):
    type = models.BooleanField()
    user = models.ForeignKey(Account, related_name='likes_user' , on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes_post', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type)


# class CommentLike(models.Model): 
#     like_type = models.BooleanField()
#     user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
#     comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.id