from django_filters import rest_framework as filters

from transactions.models import Payment


class PaymentFilterSet(filters.FilterSet):
    class Meta:
        model = Payment
        fields = '__all__'
