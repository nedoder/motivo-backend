from django.shortcuts import render
from rest_framework import viewsets
from .models import AnnualBudgetManagement, Profile
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from django.db.models import Q, Count
import json
from django.core import serializers
from django.http import FileResponse, JsonResponse
from .serializers import AnnualBudgetStatisticsSerializer, AnnualBudgetManagementSerializer

import datetime
import json

# Create your views here.

class BudgetManagementViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = AnnualBudgetManagementSerializer
    
    def list(self, request):
        """Get all the budget data for authenticated user"""
        budgets = list(AnnualBudgetManagement.objects.filter(user=request.user) \
                                                     .prefetch_related('user') \
                                                     .values()
                                                     .order_by('-status'))
        
        # Adjust data to be properly displayed in frontend part
        for b in budgets:
            b['when'] = b['when'].strftime('%Y-%m-%d')
            
        today = datetime.date.today()
        end_of_the_year = datetime.date(today.year, 12, 31)
        days_left = end_of_the_year - today
        
        return Response({"budgets_table_data": budgets, 
                         "budget_left": str(request.user.budget_left_gross) + " PLN", 
                         "annual_personal_budget_amount": str(request.user.annual_budget_gross) + " PLN", 
                         "days_left_to_burn_budget": str(days_left.days) + " days" })
        
    def create(self,request):
        """Handle upcoming request from user to create a new budget position."""
        # Get incoming parameters
        budget_data = json.loads(request.data['budget_data'])
        
        amount = int(budget_data['amount'])
        if amount > request.user.budget_left_gross:
            return Response({"message":"You don't have enough budget to perform this action"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create proper position in database
        AnnualBudgetManagement.objects.create(user=request.user, 
                                            title=budget_data['title'], 
                                            category=budget_data['category'], 
                                            when=budget_data['when'], 
                                            amount=amount,
                                            comment=budget_data['comment'],
                                            file=request.data['file'])
        
        # Take the budget from user's account
        request.user.budget_left_gross -= amount
        request.user.save()
        
        return Response({"message":"Added new budget position"})

class BudgetCategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = AnnualBudgetManagementSerializer
    
    def list(self, request):
        """Get all the categories of the budget"""
        data = [{"value": x, "label": y} for x,y in AnnualBudgetManagement.CATEGORIES]
        return Response(data)