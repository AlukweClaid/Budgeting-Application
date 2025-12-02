from django import forms
from .models import BudgetItem, Category, Transaction, BudgetGoal, ExpenseTracker, RecurringExpense


class BudgetItemForm(forms.ModelForm):
    class Meta:
        model = BudgetItem
        fields = ['name', 'amount', 'description', 'urgency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
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
