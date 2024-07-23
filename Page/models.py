from django.db import models

# Create your models here.
class Datas(models.Model):
    ID=models.IntegerField(auto_created=True)
    name=models.CharField(("Name"),max_length=100)
    email=models.EmailField(("Email"), max_length=254)
    def __str__(self) -> str:
        return self.name