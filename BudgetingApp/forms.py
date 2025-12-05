from django import forms
from .models import BudgetItem, Category, Transaction, BudgetGoal, ExpenseTracker, RecurringExpense
from .models import IncomeSource, SavingsAccount, BudgetReminder, FinancialReport


class BudgetItemForm(forms.ModelForm):
    class Meta:
        model = BudgetItem
        fields = ['name', 'category', 'amount', 'description', 'urgency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Groceries'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'urgency': forms.Select(attrs={'class': 'form-select'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'amount', 'transaction_type', 'category']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'transaction_type': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }


class BudgetGoalForm(forms.ModelForm):
    class Meta:
        model = BudgetGoal
        fields = ['name', 'target_amount', 'current_amount', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'target_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'current_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ExpenseTrackerForm(forms.ModelForm):
    class Meta:
        model = ExpenseTracker
        fields = ['date', 'amount', 'category', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class RecurringExpenseForm(forms.ModelForm):
    class Meta:
        model = RecurringExpense
        fields = ['name', 'amount', 'frequency', 'next_due_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'frequency': forms.Select(attrs={'class': 'form-select'}),
            'next_due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class IncomeSourceForm(forms.ModelForm):
    class Meta:
        model = IncomeSource
        fields = ['name', 'amount', 'frequency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'frequency': forms.Select(attrs={'class': 'form-select'}),
        }


class SavingsAccountForm(forms.ModelForm):
    class Meta:
        model = SavingsAccount
        fields = ['name', 'balance', 'interest_rate']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class BudgetReminderForm(forms.ModelForm):
    class Meta:
        model = BudgetReminder
        fields = ['message', 'remind_on', 'is_sent']
        widgets = {
            'message': forms.TextInput(attrs={'class': 'form-control'}),
            'remind_on': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_sent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class FinancialReportForm(forms.ModelForm):
    class Meta:
        model = FinancialReport
        fields = ['report_type', 'content']
        widgets = {
            'report_type': forms.Select(attrs={'class': 'form-select'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
        }


class PaymentForm(forms.Form):
    PAYMENT_METHODS = [
        ('stripe', 'Card (Stripe)'),
        ('mpesa', 'M-Pesa'),
    ]
    budget_item = forms.ModelChoiceField(queryset=BudgetItem.objects.all(), widget=forms.Select(attrs={'class': 'form-select'}))
    amount = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))
    method = forms.ChoiceField(choices=PAYMENT_METHODS, widget=forms.RadioSelect)
    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2547XXXXXXXX'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['budget_item'].queryset = BudgetItem.objects.filter(owner=user)
