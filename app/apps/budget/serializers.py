from .models import AnnualBudgetManagement, AnnualBudgetStatistics
from rest_framework import serializers

class AnnualBudgetManagementSerializer(serializers.Serializer):
    class Meta:
        model = AnnualBudgetManagement
        fields = '__all__'
        
class AnnualBudgetStatisticsSerializer(serializers.Serializer):
    class Meta:
        model = AnnualBudgetStatistics
        fields = '__all__'