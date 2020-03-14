from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from transactions.filters import PaymentFilterSet
from transactions.models import Payment
from transactions.serializers import PaymentSerializer


class PaymentModelViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = PaymentFilterSet
    ordering_fields = ['date']
    ordering = ['-date']
