from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

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
# Create your views here.


def budget_home(request):
    """Render a simple dashboard with counts of a few models."""
    if request.user.is_authenticated:
        counts = {
            'budget_items': BudgetItem.objects.filter(owner=request.user).count(),
            'categories': Category.objects.filter(owner=request.user).count(),
            'transactions': Transaction.objects.filter(owner=request.user).count(),
            'goals': BudgetGoal.objects.filter(owner=request.user).count(),
            'expenses': ExpenseTracker.objects.filter(owner=request.user).count(),
        }
    else:
        counts = {'budget_items': 0, 'categories': 0, 'transactions': 0, 'goals': 0, 'expenses': 0}
    return render(request, 'BudgetingApp/index.html', {'counts': counts})


# Generic CRUD views for BudgetItem
class BudgetItemListView(LoginRequiredMixin, ListView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class BudgetItemDetailView(LoginRequiredMixin, DetailView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_detail.html'
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class BudgetItemCreateView(LoginRequiredMixin, CreateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = 'BudgetingApp/BudgetItem_form.html'
    success_url = reverse_lazy('budgetitem-list')
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
        return super().form_valid(form)


class BudgetItemUpdateView(LoginRequiredMixin, UpdateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = 'BudgetingApp/BudgetItem_form.html'
    success_url = reverse_lazy('budgetitem-list')
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class BudgetItemDeleteView(LoginRequiredMixin, DeleteView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_confirm_delete.html'
    success_url = reverse_lazy('budgetitem-list')
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


# Generic CRUD views for Category
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'BudgetingApp/Category_list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'BudgetingApp/Category_detail.html'
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'BudgetingApp/Category_form.html'
    success_url = reverse_lazy('category-list')
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'BudgetingApp/Category_form.html'
    success_url = reverse_lazy('category-list')
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'BudgetingApp/Category_confirm_delete.html'
    success_url = reverse_lazy('category-list')
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


# Generic CRUD views for Transaction
class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_detail.html'
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'BudgetingApp/Transaction_form.html'
    success_url = reverse_lazy('transaction-list')
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'BudgetingApp/Transaction_form.html'
    success_url = reverse_lazy('transaction-list')
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction-list')
    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(owner=self.request.user)
        return qs.none()

# Additional views for authentication can be added here
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
class CustomLoginView(LoginView):
    template_name = 'BudgetingApp/login.html'
    redirect_authenticated_user = True
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('budget_home')
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'BudgetingApp/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # automatically authenticate and log the user in
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('budget_home')
            return redirect('login')
        return render(request, 'BudgetingApp/register.html', {'form': form})
    