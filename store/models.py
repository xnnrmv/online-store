from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Avtomatik slug yaratish
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    UZ='sum'
    RU='rub'
    USD='$'
    type_money=(
        (UZ,'sum'),
        (RU, 'rub'),
        (USD, '$')
    )
    price_type=models.CharField(max_length=10,
                                choices=type_money,
                                default='sum')
    price = models.PositiveIntegerField()
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Avtomatik slug yaratish
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name