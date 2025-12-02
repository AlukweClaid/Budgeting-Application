from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import (
    BudgetItem,
    Category,
    Transaction,
    BudgetGoal,
    ExpenseTracker,
)
from .forms import (
    BudgetItemForm,
    CategoryForm,
    TransactionForm,
    BudgetGoalForm,
    ExpenseTrackerForm,
    RecurringExpenseForm,
)


def budget_home(request):
    """Render a simple dashboard with counts of a few models."""
    counts = {
        'budget_items': BudgetItem.objects.count(),
        'categories': Category.objects.count(),
        'transactions': Transaction.objects.count(),
        'goals': BudgetGoal.objects.count(),
        'expenses': ExpenseTracker.objects.count(),
    }
    return render(request, 'BudgetingApp/index.html', {'counts': counts})


# Generic CRUD views for BudgetItem
class BudgetItemListView(ListView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_list.html'


class BudgetItemDetailView(DetailView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_detail.html'


class BudgetItemCreateView(CreateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = 'BudgetingApp/BudgetItem_form.html'
    success_url = reverse_lazy('budgetitem-list')


class BudgetItemUpdateView(UpdateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = 'BudgetingApp/BudgetItem_form.html'
    success_url = reverse_lazy('budgetitem-list')


class BudgetItemDeleteView(DeleteView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_confirm_delete.html'
    success_url = reverse_lazy('budgetitem-list')


# Generic CRUD views for Category
class CategoryListView(ListView):
    model = Category
    template_name = 'BudgetingApp/Category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'BudgetingApp/Category_detail.html'


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'BudgetingApp/Category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'BudgetingApp/Category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'BudgetingApp/Category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


# Generic CRUD views for Transaction
class TransactionListView(ListView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_list.html'


class TransactionDetailView(DetailView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_detail.html'


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'BudgetingApp/Transaction_form.html'
    success_url = reverse_lazy('transaction-list')


class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'BudgetingApp/Transaction_form.html'
    success_url = reverse_lazy('transaction-list')


class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction-list')
