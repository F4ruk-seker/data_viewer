from django.db import models


class Office(models.Model):
    name = models.TextField()
    performance = models.ForeignKey('product_operation.PerformanceMetric',on_delete=models.CASCADE,default=None,blank=True)

    def __str__(self):
        return str(self.name)