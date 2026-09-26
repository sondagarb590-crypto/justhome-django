from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    LISTING_TYPE = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    ]
    PROPERTY_TYPE = [
        ('villa', 'Modern Villa'),
        ('apartment', 'Apartment'),
        ('townhouse', 'Town House'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    listing_type = models.CharField(max_length=10, choices=LISTING_TYPE, default='sale')
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE, default='villa')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    area_sqft = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='properties/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ['-created_at']


class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
