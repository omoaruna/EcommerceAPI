from django.db import models
class Product(models.Model):
    CATEGORY_CHOICES =(
    ("W","Women"),
    ("M","Men"),
    ("K","Kids"),
    ("E","Electronics")
)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    description = models.TextField()
    category = models.CharField(max_length=15,choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="category_images",default="default.png")
  
    def __str__(self):
      return self.name
  

# Create your models here.
