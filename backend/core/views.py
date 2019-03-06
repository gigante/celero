from rest_framework import serializers
from rest_framework import viewsets, filters
from .models.account import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'currency', 'flow', 'created_at', 'updated_at')


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name', 'currency')
