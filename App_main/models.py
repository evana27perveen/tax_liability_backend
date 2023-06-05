from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class IncomeTaxReturn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filing_type = models.CharField(max_length=255)  # salaried or normal
    income = models.DecimalField(max_digits=12, decimal_places=2)
    expenses = models.DecimalField(max_digits=12, decimal_places=2)
    deduction = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)
    filing_date = models.DateField()

    def __str__(self):
        return f"Income Tax Return - {self.user.name}"

class IncomeTaxRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=255)
    registration_date = models.DateField()

    def __str__(self):
        return f"Income Tax Registration - {self.user.name}"

class SalesTaxRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=255)
    registration_date = models.DateField()

    def __str__(self):
        return f"Sales Tax Registration - {self.user.name}"

class TaxVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Tax Verification - {self.user.name}"

class TaxCalculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vat_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2)
    calculation_date = models.DateField()

    def __str__(self):
        return f"Tax Calculation - {self.user.name}"

class EPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=255)  # income tax, sales tax, federal excise duty
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=255)

    def __str__(self):
        return f"E-Payment - {self.user.name}"

class PaymentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_type = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)

    def __str__(self):
        return f"Payment Record - {self.user.name}"

class PenaltyCalculation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    penalty_amount = models.DecimalField(max_digits=12, decimal_places=2)
    penalty_reason = models.CharField(max_length=255)
    calculation_date = models.DateField()

    def __str__(self):
        return f"Penalty Calculation - {self.user.name}"
