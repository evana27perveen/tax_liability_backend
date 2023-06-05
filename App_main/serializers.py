from rest_framework import serializers
from .models import (
    IncomeTaxReturn,
    IncomeTaxRegistration,
    SalesTaxRegistration,
    TaxVerification,
    TaxCalculation,
    EPayment,
    PaymentRecord,
    PenaltyCalculation,
)


class IncomeTaxReturnSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = IncomeTaxReturn
        fields = '__all__'


class IncomeTaxRegistrationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = IncomeTaxRegistration
        fields = '__all__'


class SalesTaxRegistrationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SalesTaxRegistration
        fields = '__all__'


class TaxVerificationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaxVerification
        fields = '__all__'


class TaxCalculationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaxCalculation
        fields = '__all__'


class EPaymentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = EPayment
        fields = '__all__'


class PaymentRecordSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PaymentRecord
        fields = '__all__'


class PenaltyCalculationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PenaltyCalculation
        fields = '__all__'
