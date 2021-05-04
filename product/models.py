from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(null=True, max_length=150, db_index=True)
    slug = models.SlugField(null=True, unique=True)
    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('products:products_by_category', args=[self.slug])

class Product(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    price = models.IntegerField(default=None)
    productimg = models.ImageField(upload_to='images', blank=True)
    slug = models.SlugField(max_length=250, null=True, unique_for_date='publish')
    product_description = models.TextField(null=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='all_products')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
       return reverse('products:product_detail',args=[self.id,])

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(null=True, max_length=30)
    lastname = models.CharField(null=True, max_length=30)
    username = models.CharField(null=True, max_length=30)
    password = models.CharField(null=True, max_length=30)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = "web_member"