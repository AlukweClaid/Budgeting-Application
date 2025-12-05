from django.contrib import admin
from .models import (
    BudgetItem,
    Category,
    BudgetItemCategory,
    RecurringExpense,
    BudgetGoal,
    ExpenseTracker,
    IncomeSource,
    SavingsAccount,
    Transaction,
    FinancialReport,
    BudgetReminder,
    SubAccount,
    Payment,
    PaymentAllocation,
)


@admin.register(BudgetItem)
class BudgetItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'amount', 'urgency', 'created_at')
    list_filter = ('urgency', 'created_at')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(BudgetItemCategory)
class BudgetItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('budget_item', 'category')
    search_fields = ('budget_item__name', 'category__name')


@admin.register(RecurringExpense)
class RecurringExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'frequency', 'next_due_date')
    list_filter = ('frequency', 'next_due_date')
    search_fields = ('name',)


@admin.register(BudgetGoal)
class BudgetGoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'target_amount', 'current_amount', 'deadline')
    list_filter = ('deadline',)
    search_fields = ('name',)


@admin.register(ExpenseTracker)
class ExpenseTrackerAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'category')
    list_filter = ('date', 'category')
    search_fields = ('notes',)


@admin.register(IncomeSource)
class IncomeSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'frequency')
    list_filter = ('frequency',)
    search_fields = ('name',)


@admin.register(SavingsAccount)
class SavingsAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'interest_rate')
    search_fields = ('name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'transaction_type', 'category')
    list_filter = ('date', 'transaction_type', 'category')
    search_fields = ('category__name',)


@admin.register(FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'generated_on')
    list_filter = ('report_type', 'generated_on')


@admin.register(BudgetReminder)
class BudgetReminderAdmin(admin.ModelAdmin):
    list_display = ('message', 'remind_on', 'is_sent')
    list_filter = ('remind_on', 'is_sent')
    search_fields = ('message',)


@admin.register(SubAccount)
class SubAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'budget_item', 'balance', 'owner')
    search_fields = ('name',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'amount', 'method', 'status', 'created_at')
    list_filter = ('method', 'status', 'created_at')
    search_fields = ('external_id',)


@admin.register(PaymentAllocation)
class PaymentAllocationAdmin(admin.ModelAdmin):
    list_display = ('payment', 'budget_item', 'amount')
    search_fields = ('budget_item__name',)
