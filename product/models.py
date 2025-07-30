from django.db import models
from users.models import User, BaseModel
from django.core.validators import FileExtensionValidator



class Category(BaseModel):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    
    def __str__(self):
        return self.name
    
    
    
class Product(BaseModel):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(default="", blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    
    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
    
    def __str__(self):
        return self.name
    


