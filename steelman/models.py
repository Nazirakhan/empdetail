from django.db import models

class empdata(models.Model):
    name = models.CharField(max_length=75)
    company = models.CharField(max_length=80)
    designation = models.CharField(max_length = 100)
    joined_date = models.DateField()
    photo = models.ImageField(upload_to='photos/employee')
    country = models.CharField(max_length=40)

    class Meta:
        db_table = "Employee Data"
        verbose_name = "Employee Data"
        verbose_name_plural = "Employee Data's"

    def __str__(self):
        return self.name