from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_home, name='budget_home'),

    # Authentication URLs
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    # BudgetItem CRUD
    path('budgetitems/', views.BudgetItemListView.as_view(), name='budgetitem-list'),
    path('budgetitems/add/', views.BudgetItemCreateView.as_view(), name='budgetitem-add'),
    path('budgetitems/<int:pk>/', views.BudgetItemDetailView.as_view(), name='budgetitem-detail'),
    path('budgetitems/<int:pk>/edit/', views.BudgetItemUpdateView.as_view(), name='budgetitem-edit'),
    path('budgetitems/<int:pk>/delete/', views.BudgetItemDeleteView.as_view(), name='budgetitem-delete'),

    # Category CRUD
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    # Transaction CRUD
    path('transactions/', views.TransactionListView.as_view(), name='transaction-list'),
    path('transactions/add/', views.TransactionCreateView.as_view(), name='transaction-add'),
    path('transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<int:pk>/edit/', views.TransactionUpdateView.as_view(), name='transaction-edit'),
    path('transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction-delete'),
]