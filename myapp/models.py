from django.db import models

# Create your models here.
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')  # Assuming you want to upload images for each blog post
    date_published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_excerpt(self):
        # Returns the first 30 words of the content
        return ' '.join(self.content.split()[:30]) + '...'
