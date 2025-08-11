from django.db import models

class Member(models.Model):
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Admin'),
            ('editor', 'Editor'),
             ('author', 'author'),
            ('reporter', 'Reporter'),
            ('reader', 'Reader'),

        ],
        default='reader'
    )
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
