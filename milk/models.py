from django.db import models

class MilkProduction(models.Model):
    date = models.DateField()
    quantity = models.FloatField(help_text="Litres produced")

    def __str__(self):
        return f"{self.date} - {self.quantity} litres"


class Sale(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('mobile', 'Mobile Money'),
        ('bank', 'Bank Transfer'),
    ]

    date = models.DateField()
    customer = models.CharField(max_length=100)
    litres_sold = models.FloatField()
    price_per_litre = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='cash')

    def __str__(self):
        return f"{self.customer} - {self.date}"

    @property
    def total_sale(self):
        return self.litres_sold * float(self.price_per_litre)

    @property
    def balance(self):
        return self.total_sale - float(self.paid)


class Expense(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.description}"


class SpoiledMilk(models.Model):
    date = models.DateField()
    litres = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.litres} litres"
