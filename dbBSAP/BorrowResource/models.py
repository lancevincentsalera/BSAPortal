from django.db import models
from dbBSAP.CreateAccount.models import User
# Create your models here.


class Resource(models.Model):
    resource_id = models.BigAutoField(primary_key=True)
    resourceQuantity = models.IntegerField()
    resourceName = models.CharField(max_length=25)
    isAvailable = models.BooleanField()

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table = "Resource"


class BorrowResource(models.Model):
    borrowResources_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    borrowDate = models.DateField()
    returnDate = models.DateField()

    class Meta:
        db_table = "BorrowResource"
