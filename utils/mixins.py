from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_created=True)