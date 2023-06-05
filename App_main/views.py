from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (
    IncomeTaxRegistration,
    SalesTaxRegistration,
    TaxVerification,
    TaxCalculation,
    EPayment,
    PaymentRecord,
    PenaltyCalculation,
)
from .serializers import (
    IncomeTaxRegistrationSerializer,
    SalesTaxRegistrationSerializer,
    TaxVerificationSerializer,
    TaxCalculationSerializer,
    EPaymentSerializer,
    PaymentRecordSerializer,
    PenaltyCalculationSerializer,
)


class IncomeTaxRegistrationCreateView(APIView):
    def post(self, request):
        serializer = IncomeTaxRegistrationSerializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeTaxRegistrationListView(APIView):
    def get(self, request):
        queryset = IncomeTaxRegistration.objects.filter(user=request.user)
        serializer = IncomeTaxRegistrationSerializer(queryset, many=True)
        return Response(serializer.data)


class IncomeTaxRegistrationDetailView(APIView):
    def get_object(self, pk):
        try:
            return IncomeTaxRegistration.objects.get(pk=pk, user=self.request.user)
        except IncomeTaxRegistration.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = IncomeTaxRegistrationSerializer(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = IncomeTaxRegistrationSerializer(instance, data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Similarly, define the remaining views for other models: SalesTaxRegistration, TaxVerification,
# TaxCalculation, EPayment, PaymentRecord, and PenaltyCalculation.


