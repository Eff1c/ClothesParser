from django.db import models


class ClothingType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ClothingSex(models.Model):
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.sex


class ShoppingSite(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name


class Clothing(models.Model):
    name = models.CharField(max_length=400)
    media = models.JSONField()
    url = models.URLField()
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    color = models.CharField(max_length=100, blank=True)
    parse_date = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(ClothingType, on_delete=models.CASCADE)
    site = models.ForeignKey(ShoppingSite, on_delete=models.CASCADE)
    sex = models.ForeignKey(ClothingSex, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
