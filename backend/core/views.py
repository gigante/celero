from rest_framework import serializers
from rest_framework import viewsets, filters
from .models.account import Account, FlowType


class AccountSerializer(serializers.ModelSerializer):
    display_currency = serializers.SerializerMethodField(source='currency')
    display_flow = serializers.SerializerMethodField(source='flow')

    def get_display_currency(self, obj):
        signal = "+" if obj.flow == FlowType.RECIPE else "-"
        return f'{signal} R$ {obj.currency}'

    def get_display_flow(self, obj):
        dict_types = dict(FlowType.TYPES)
        return dict_types[obj.flow]

    class Meta:
        model = Account
        fields = (
            'id', 'name', 'currency', 'display_currency',
            'flow', 'display_flow', 'created_at', 'updated_at')


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name', 'currency')
