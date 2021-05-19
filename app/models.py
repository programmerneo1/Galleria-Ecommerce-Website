from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


STATE_CHOICES = (("Andhra Pradesh", "Andhra Pradesh"), ("Arunachal Pradesh ", "Arunachal Pradesh "), ("Assam", "Assam"), ("Bihar", "Bihar"), ("Chhattisgarh", "Chhattisgarh"), ("Goa", "Goa"), ("Gujarat", "Gujarat"), ("Haryana", "Haryana"), ("Himachal Pradesh", "Himachal Pradesh"), ("Jammu and Kashmir ", "Jammu and Kashmir "), ("Jharkhand", "Jharkhand"), ("Karnataka", "Karnataka"), ("Kerala", "Kerala"), ("Madhya Pradesh", "Madhya Pradesh"), ("Maharashtra", "Maharashtra"), ("Manipur", "Manipur"), ("Meghalaya", "Meghalaya"), ("Mizoram", "Mizoram"), ("Nagaland", "Nagaland"), ("Odisha", "Odisha"),
                 ("Punjab", "Punjab"), ("Rajasthan", "Rajasthan"), ("Sikkim", "Sikkim"), ("Tamil Nadu", "Tamil Nadu"), ("Telangana", "Telangana"), ("Tripura", "Tripura"), ("Uttar Pradesh", "Uttar Pradesh"), ("Uttarakhand", "Uttarakhand"), ("West Bengal", "West Bengal"), ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"), ("Chandigarh", "Chandigarh"), ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"), ("Daman and Diu", "Daman and Diu"), ("Lakshadweep", "Lakshadweep"), ("National Capital Territory of Delhi", "National Capital Territory of Delhi"), ("Puducherry", "Puducherry"))


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField(default=123456789)
    locality = models.CharField(max_length=200)
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    zipcode = models.IntegerField()

    # def __str__(self):
    #     return self(self.id)


CATAGORY_CHOICES = (
    ('MS', 'MENS SHIRTS'),
    ('MT', 'MENS T-SHIRTS'),
    ('MJ', 'MENS JEANS'),
    ('MCS', 'MENS CASUAL SHOES'),
    ('MSS', 'MENS SPORTS SHOES'),
    ('MCO', 'MENS CLOTHES OTHERS'),
    ('MSO', 'MENS SHOES OTHERS'),
    ('WS', 'WOMENS SHIRTS'),
    ('WT', 'WOMENS T-SHIRTS'),
    ('WJ', 'WOMENS JEANS'),
    ('WCS', 'WOMENS CASUAL SHOES'),
    ('WSS', 'WOMENS SPORTS SHOES'),
    ('WCO', 'WOMENS CLOTHES OTHERS'),
    ('WSO', 'WOMENS SHOES OTHERS'),
)

GENDER_CHOICES = (
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('U', 'UNISEX'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATAGORY_CHOICES, max_length=3)
    product_image = models.ImageField(upload_to='productimg', max_length=300)
    product_rating = models.FloatField()
    sex = models.CharField(choices=GENDER_CHOICES, max_length=1, default='M')

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse("mens", kwargs={"data": self.slug})


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
