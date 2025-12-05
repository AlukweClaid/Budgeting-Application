from django.db import models
from django.conf import settings

# Create your models here.
class BudgetItem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='budget_items')
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    urgency = models.CharField(max_length=50, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} - {self.amount}"
class Category(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class BudgetItemCategory(models.Model):
    budget_item = models.ForeignKey(BudgetItem, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='budget_item_categories')
    def __str__(self):
        return f"{self.budget_item.name} in {self.category.name}"
class RecurringExpense(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='recurring_expenses')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ])
    next_due_date = models.DateField()
    def __str__(self):
        return f"{self.name} - {self.amount} every {self.frequency}"
class BudgetGoal(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='budget_goals')
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateField()
    def __str__(self):
        return f"{self.name} - Target: {self.target_amount} by {self.deadline}"
class ExpenseTracker(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='expenses')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.date} - {self.amount} in {self.category.name}"
class IncomeSource(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='income_sources')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency = models.CharField(max_length=50, choices=[
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')
    ])
    def __str__(self):
        return f"{self.name} - {self.amount} every {self.frequency}"
class SavingsAccount(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='savings_accounts')
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.name} - Balance: {self.balance}"
class Transaction(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='transactions')
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=50, choices=[
        ('income', 'Income'),
        ('expense', 'Expense')
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.date} - {self.transaction_type}: {self.amount} in {self.category.name}"
class FinancialReport(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='financial_reports')
    report_type = models.CharField(max_length=50, choices=[
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly')
    ])
    generated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    def __str__(self):
        return f"{self.report_type} report generated on {self.generated_on}"
class BudgetReminder(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='reminders')
    message = models.CharField(max_length=255)
    remind_on = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    def __str__(self):
        return f"Reminder: {self.message} on {self.remind_on}"


class MpesaCallbackLog(models.Model):
    """Store raw M-Pesa callback payloads for auditing and debugging."""
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, null=True, blank=True)
    payload = models.JSONField()
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MpesaCallbackLog {self.id} for payment {self.payment_id} at {self.received_at}"


# Payment & subaccount models
class SubAccount(models.Model):
    """A logical sub-account to route payments to a BudgetItem or other target."""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='subaccounts')
    name = models.CharField(max_length=150)
    budget_item = models.ForeignKey(BudgetItem, on_delete=models.SET_NULL, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.budget_item.name if self.budget_item else 'No item'})"


class Payment(models.Model):
    """Record a payment attempt/receipt from Stripe or M-Pesa."""
    PAYMENT_METHOD_CHOICES = [
        ('stripe', 'Card / Stripe'),
        ('mpesa', 'M-Pesa'),
    ]
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    external_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.id} {self.amount} {self.method} {self.status}"


class PaymentAllocation(models.Model):
    """Allocate part or all of a Payment to a BudgetItem (sub-account)."""
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='allocations')
    budget_item = models.ForeignKey(BudgetItem, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.payment} -> {self.budget_item.name}: {self.amount}"
    

    

    
    