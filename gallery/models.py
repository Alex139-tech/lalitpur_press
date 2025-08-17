from django.db import models

class PhotoGallery(models.Model):
    feature_image = models.ImageField(upload_to="gallery/feature/", null=False, blank=False)
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
    

class GalleryImage(models.Model):
    gallery = models.ForeignKey(PhotoGallery, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="gallery/images/")

    def __str__(self):
        return f"Image of {self.gallery.title}"
