from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Product(models.Model):

    pName = models.CharField(max_length=100)
    pCategory = models.CharField(max_length=100)
    pDate_posted = models.DateTimeField(default=timezone.now)  # auto_now_add=True adds date when objects created
    pOwner = models.ForeignKey(User, on_delete=models.CASCADE)  # delete when the user gets deleted
    pPrice = models.IntegerField()
    pColor = models.CharField(max_length=100)
    pImage1 = models.ImageField(default='default.jpg', upload_to='product_pics')
    pImage2 = models.ImageField(default='default.jpg', upload_to='product_pics')
    pImage3 = models.ImageField(default='default.jpg', upload_to='product_pics')
    pRating = models.IntegerField()
    

    def __str__(self):
        return self.pName

    # getting error:No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    # when trying to post new content
    # so adding this function

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

class Mobile(Product):
    pMobileProcessor=models.CharField(max_length=100)
    pMobileRearCamera=models.CharField(max_length=100)
    pMobileFrontCamera =models.CharField(max_length=100)
    pMobileDisplay=models.CharField(max_length=100)
    pMobileRam=models.CharField(max_length=100)
    pMobileStorage =models.CharField(max_length=100)
    pMobileBattery =models.CharField(max_length=100)
    pMobileOS=models.CharField(max_length=100)






