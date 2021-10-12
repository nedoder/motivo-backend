from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'management', views.BudgetManagementViewSet, basename='budgetmanagement')
router.register(r'categories', views.BudgetCategoriesViewSet, basename='budgetcategories')



urlpatterns = [
    path('', include(router.urls)),
]

