from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

# News Model
class News(models.Model):
    class NewsStatus(models.TextChoices):
        PUBLISHED = "PUB", "Published"
        DRAFT = "DRF", "Draft"

    image = models.ImageField(upload_to='photo/')
    title = models.CharField(max_length=255)
    content = CKEditor5Field("Text", config_name="extends")
    status = models.CharField(
        max_length=3, choices=NewsStatus.choices, default=NewsStatus.DRAFT
    )
    created_at = models.DateTimeField(default=timezone.now)
    published_date = models.DateField()

    def __str__(self):
        return self.title


# Notice Model
class Notice(models.Model):
    class NoticeStatus(models.TextChoices):
        PUBLISHED = "PUB", "Published"
        DRAFT = "DRF", "Draft"

    file = models.FileField(upload_to='notices/images/')  # fixed: FileField instead of FieldFile
    title = models.CharField(max_length=255)
    content = CKEditor5Field("Text", config_name="extends")
    status = models.CharField(
        max_length=3, choices=NoticeStatus.choices, default=NoticeStatus.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)  # fixed typo
    published_date = models.DateField()

    def __str__(self):
        return self.title
