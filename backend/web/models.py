from django.db import models
from django.utils.text import slugify
import uuid

class User(models.Model):
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    email = models.EmailField(primary_key=True)
    password = models.TextField(null=True)
    is_subscribed = models.BigIntegerField(default=0)

    def is_subscribed_to_channel(self, channel: int):
        return self.is_subscribed & channel != 0


class Classification(models.Model):
    name = models.TextField()
    slug = models.SlugField(default="", null=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Issue(models.Model):
    name = models.TextField()
    slug = models.SlugField(default="", null=False)
    cover = models.ImageField(null=True, upload_to='images/articleCovers/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# Create your models here.
class Article(models.Model):
    article_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.TextField()
    author = models.TextField()
    date_published = models.DateTimeField()
    image = models.ImageField(null=True, upload_to='images/')
    textual_content = models.TextField()
    description = models.TextField(null=True)
    article_classification = models.ForeignKey(
        Classification,
        on_delete=models.DO_NOTHING,
        related_name="classificationOfArticle",
        null=True,
    )
    issue = models.ForeignKey(
        Issue,
        on_delete=models.DO_NOTHING,
        related_name="issueWhenPublished",
        null=True,
    )
    featured = models.BooleanField(null=True)

    def __str__(self):
        return str(self.article_id)


class Author(models.Model):
    name = models.TextField()
    bio = models.TextField()
    location = models.TextField()
    online_user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="authorUser", null=True
    )


class LikedArticle(models.Model):
    liker = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="userWhoLikedTheArticle"
    )
    article = models.ForeignKey(
        Article, on_delete=models.DO_NOTHING, related_name="articleTheUserLiked"
    )


class ArticleComment(models.Model):
    commenter = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="commenter"
    )
    article = models.ForeignKey(
        Article, on_delete=models.DO_NOTHING, related_name="articleTheUserCommentedOn"
    )
    date_commented = models.DateTimeField(auto_created=True, null=True)
    comment_content = models.TextField(null=True)

# TODO create a model for an ISSUE for each article
