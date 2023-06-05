# Tax Management System Models

This Django application provides models for managing income tax, sales tax, and related calculations and payments.

**Models**

**IncomeTaxReturn**
- user: ForeignKey to the User model provided by Django's `contrib.auth` module.
- filing_type: CharField to indicate the type of filing (salaried or normal).
- income: DecimalField to store the income amount.
- expenses: DecimalField to store the expenses amount.
- deduction: DecimalField to store the deduction amount.
- tax_amount: DecimalField to store the tax amount.
- filing_date: DateField to store the filing date.

**IncomeTaxRegistration**
- user: ForeignKey to the User model.
- registration_number: CharField to store the registration number.
- registration_date: DateField to store the registration date.

**SalesTaxRegistration**
- user: ForeignKey to the User model.
- registration_number: CharField to store the registration number.
- registration_date: DateField to store the registration date.

**TaxVerification**
- user: ForeignKey to the User model.
- verification_status: BooleanField to indicate the verification status.

**TaxCalculation**
- user: ForeignKey to the User model.
- vat_amount: DecimalField to store the VAT amount.
- tax_amount: DecimalField to store the tax amount.
- calculation_date: DateField to store the calculation date.

**EPayment**
- user: ForeignKey to the User model.
- payment_type: CharField to indicate the type of payment (income tax, sales tax, federal excise duty).
- amount: DecimalField to store the payment amount.
- payment_date: DateField to store the payment date.
- payment_status: CharField to store the payment status.

**PaymentRecord**
- user: ForeignKey to the User model.
- payment_date: DateField to store the payment date.
- amount: DecimalField to store the payment amount.
- payment_type: CharField to indicate the type of payment.
- transaction_id: CharField to store the transaction ID.

**PenaltyCalculation**
- user: ForeignKey to the User model.
- penalty_amount: DecimalField to store the penalty amount.
- penalty_reason: CharField to store the reason for the penalty.
- calculation_date: DateField to store the calculation date.

## Usage

These models provide the necessary fields to manage income tax returns, tax registrations, tax verifications, tax calculations, e-payments, payment records, and penalty calculations. You can use these models as a foundation for building your tax management system in Django.

Feel free to customize these models according to your specific requirements.

Please note that these models assume the existence of the User model provided by Django's `contrib.auth` module. Ensure that you have the required authentication and user management set up in your Django project.
