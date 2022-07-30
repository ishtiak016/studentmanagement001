from django.db import models
from django.utils.html import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Category(MPTTModel):
    status =(
    ('True','true'),
    ('False','false'),
    )
    parent =TreeForeignKey(
    'self',on_delete=models.CASCADE, null=True, blank=True , related_name='children')
    """docstring for Category."""

    title=models.CharField(max_length=200)
    keywords=models.CharField(max_length=200)
    image=models.ImageField(blank=True, upload_to='category')
    status=models.CharField(max_length=20, choices=status)
    slug=models.SlugField(null=True, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class MPTTMeta:
        order_insertion_by = ['title']
    def __str__(self):
        return self.title
class Product(models.Model):
    status =(
    ('True','true'),
    ('False','false'),
    )
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    keywords=models.CharField(max_length=200)
    image=models.ImageField(blank=True, upload_to='product/')
    new_price=models.DecimalField(decimal_places=2, max_digits=15, default=0)
    old_price=models.DecimalField(decimal_places=2, max_digits=15)
    amount=models.IntegerField(default=0)
    min_amount=models.IntegerField(default=3)
    details=models.TextField()
    status=models.CharField(max_length=20, choices=status)
    slug=models.SlugField(null=True, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'


    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""
    def get_absolute_url(self):
        return reverse('product_element',kwargs={'slug': self.slug})
class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='product/')

    def __str(self):
        return self.title
