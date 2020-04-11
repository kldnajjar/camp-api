from django.db.models import Sum, Q, F, Func
from rest_framework.generics import ListAPIView
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from transactions.filters import PaymentFilterSet
from transactions.models import Payment
from transactions.serializers import PaymentSerializer
from utils.db import Round2


class PaymentModelViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (DjangoModelPermissions,)
    filterset_class = PaymentFilterSet
    ordering_fields = ['date']
    ordering = ['-date']


class DailyCashAPIView(ListAPIView):
    def list(self, request, *args, **kwargs):
        queryset = Payment.objects.values('date').annotate(
            total_amount=Sum('amount'),
            total_expenses=Sum('expenses'),
            total_cash=Sum('amount', filter=Q(payment_type=Payment.TYPE.cash)),
            total_credit=Sum('amount', filter=Q(payment_type=Payment.TYPE.credit)),
            gross=Round2((F('total_cash') - F('total_expenses')))
        ).order_by('-date')
        return Response(list(queryset))
