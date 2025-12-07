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
    path('transactions/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<int:pk>/delete/', views.TransactionDeleteView.as_view(), name='transaction-delete'),

  
    #path('about/', views.about, name='about'),
    #path('contact/', views.contact, name='contact'),
    #path('payment/', views.payment, name='payment'),
    #path('payment/success/', views.index, name='payment-success'),
    
    # Recurring expenses
    path('recurring/', views.RecurringExpenseListView.as_view(), name='recurringexpense-list'),
    path('recurring/add/', views.RecurringExpenseCreateView.as_view(), name='recurringexpense-add'),
    path('recurring/<int:pk>/edit/', views.RecurringExpenseUpdateView.as_view(), name='recurringexpense-edit'),
    path('recurring/<int:pk>/delete/', views.RecurringExpenseDeleteView.as_view(), name='recurringexpense-delete'),

    # Income sources
    path('incomes/', views.IncomeSourceListView.as_view(), name='incomesource-list'),
    path('incomes/add/', views.IncomeSourceCreateView.as_view(), name='incomesource-add'),
    path('incomes/<int:pk>/edit/', views.IncomeSourceUpdateView.as_view(), name='incomesource-edit'),
    path('incomes/<int:pk>/delete/', views.IncomeSourceDeleteView.as_view(), name='incomesource-delete'),

    # Savings accounts
    path('savings/', views.SavingsAccountListView.as_view(), name='savingsaccount-list'),
    path('savings/add/', views.SavingsAccountCreateView.as_view(), name='savingsaccount-add'),
    path('savings/<int:pk>/edit/', views.SavingsAccountUpdateView.as_view(), name='savingsaccount-edit'),
    path('savings/<int:pk>/delete/', views.SavingsAccountDeleteView.as_view(), name='savingsaccount-delete'),

    # Budget reminders
    path('reminders/', views.BudgetReminderListView.as_view(), name='budgetreminder-list'),
    path('reminders/add/', views.BudgetReminderCreateView.as_view(), name='budgetreminder-add'),
    path('reminders/<int:pk>/edit/', views.BudgetReminderUpdateView.as_view(), name='budgetreminder-edit'),
    path('reminders/<int:pk>/delete/', views.BudgetReminderDeleteView.as_view(), name='budgetreminder-delete'),

    # Financial reports
    path('reports/', views.FinancialReportListView.as_view(), name='financialreport-list'),
    path('reports/<int:pk>/', views.FinancialReportDetailView.as_view(), name='financialreport-detail'),

    

   # M-PESA PAYMENT URLS
path('payments/', views.payment_form, name='payments'),  
path('pay/process/', views.process_payment, name='process_payment'),
path('mpesa-callback/', views.mpesa_callback, name='mpesa-callback'),
#path('index/', views.index, name='index'),


]