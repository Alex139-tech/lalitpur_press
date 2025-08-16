from django.db import models

class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Member(models.Model):
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True) 
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    quotation = models.TextField(blank=True, null=True)  

    POSITION_TYPE_CHOICES = [
        ('Executive', 'Executive'),
        ('Regular', 'Regular'),
    ]
    member_type = models.CharField(
        max_length=10,
        choices=POSITION_TYPE_CHOICES,
        default='Regular'
    )

    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, blank=True) 
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
