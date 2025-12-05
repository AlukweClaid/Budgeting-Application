from django.conf import settings
from django.http import JsonResponse
from datetime import datetime
import requests
import base64
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django import forms
import json

from django_daraja.mpesa.core import MpesaClient

from .models import (
    BudgetItem,
    Category,
    Transaction,
    BudgetGoal,
    ExpenseTracker,
    SubAccount,
    Payment,
    PaymentAllocation,
    RecurringExpense,
    IncomeSource,
    SavingsAccount,
    BudgetReminder,
    FinancialReport,
)

from .forms import (
    BudgetItemForm,
    CategoryForm,
    TransactionForm,
    BudgetGoalForm,
    ExpenseTrackerForm,
    RecurringExpenseForm,
    PaymentForm,
    IncomeSourceForm,
    SavingsAccountForm,
    BudgetReminderForm,
    FinancialReportForm,
)

# -----------------------------
# M-PESA TEST VIEW
# -----------------------------
def index(request):
    cl = MpesaClient()
    phone_number = '0110085152'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


# -----------------------------
# DASHBOARD VIEW
# -----------------------------
def budget_home(request):
    if request.user.is_authenticated:
        counts = {
            'budget_items': BudgetItem.objects.filter(owner=request.user).count(),
            'categories': Category.objects.filter(owner=request.user).count(),
            'transactions': Transaction.objects.filter(owner=request.user).count(),
            'goals': BudgetGoal.objects.filter(owner=request.user).count(),
            'expenses': ExpenseTracker.objects.filter(owner=request.user).count(),
            'recurring': RecurringExpense.objects.filter(owner=request.user).count(),
            'incomes': IncomeSource.objects.filter(owner=request.user).count(),
            'savings': SavingsAccount.objects.filter(owner=request.user).count(),
            'reminders': BudgetReminder.objects.filter(owner=request.user).count(),
            'reports': FinancialReport.objects.filter(owner=request.user).count(),
        }
    else:
        counts = {'budget_items': 0, 'categories': 0, 'transactions': 0, 'goals': 0,
                  'expenses': 0, 'recurring': 0, 'incomes': 0, 'savings': 0,
                  'reminders': 0, 'reports': 0}

    return render(request, 'BudgetingApp/index.html', {'counts': counts})


# -----------------------------
# AUTH VIEWS
# -----------------------------
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
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('budget_home')
            return redirect('login')

        return render(request, 'BudgetingApp/register.html', {'form': form})


# -----------------------------
# M-PESA PAYMENT FORM 
# -----------------------------
class MpesaPaymentForm(forms.Form):
    phone_number = forms.CharField(
        label='Phone Number',
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'})
    )
    amount = forms.DecimalField(
        label='Amount',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'})
    )

# -----------------------------
# CRUD VIEWS
# -----------------------------

# BudgetItem CRUD
class BudgetItemListView(LoginRequiredMixin, ListView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BudgetItem.objects.filter(owner=self.request.user)
        return BudgetItem.objects.none()


class BudgetItemDetailView(LoginRequiredMixin, DetailView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_detail.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BudgetItem.objects.filter(owner=self.request.user)
        return BudgetItem.objects.none()


class BudgetItemCreateView(LoginRequiredMixin, CreateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = 'BudgetingApp/BudgetItem_form.html'
    success_url = reverse_lazy('budgetitem-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)

        if self.request.POST.get('save_and_pay'):
            pay_url = reverse('payments') + f'?budget_item={self.object.id}'
            return redirect(pay_url)

        return response


class BudgetItemUpdateView(LoginRequiredMixin, UpdateView):
    model = BudgetItem
    form_class = BudgetItemForm
    template_name = 'BudgetingApp/BudgetItem_form.html'
    success_url = reverse_lazy('budgetitem-list')

    def get_queryset(self):
        return BudgetItem.objects.filter(owner=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.POST.get('save_and_pay'):
            pay_url = reverse('payments') + f'?budget_item={self.object.id}'
            return redirect(pay_url)
        return response


class BudgetItemDeleteView(LoginRequiredMixin, DeleteView):
    model = BudgetItem
    template_name = 'BudgetingApp/BudgetItem_confirm_delete.html'
    success_url = reverse_lazy('budgetitem-list')

    def get_queryset(self):
        return BudgetItem.objects.filter(owner=self.request.user)


# Category CRUD
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'BudgetingApp/Category_list.html'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'BudgetingApp/Category_detail.html'

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'BudgetingApp/Category_form.html'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'BudgetingApp/Category_form.html'
    success_url = reverse_lazy('category-list')

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'BudgetingApp/Category_confirm_delete.html'
    success_url = reverse_lazy('category-list')

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)


# Transaction CRUD
class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_list.html'

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_detail.html'

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'BudgetingApp/Transaction_form.html'
    success_url = reverse_lazy('transaction-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'BudgetingApp/Transaction_form.html'
    success_url = reverse_lazy('transaction-list')

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'BudgetingApp/Transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction-list')

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


# RecurringExpense CRUD
class RecurringExpenseListView(LoginRequiredMixin, ListView):
    model = RecurringExpense
    template_name = 'BudgetingApp/RecurringExpense_list.html'

    def get_queryset(self):
        return RecurringExpense.objects.filter(owner=self.request.user)


class RecurringExpenseCreateView(LoginRequiredMixin, CreateView):
    model = RecurringExpense
    form_class = RecurringExpenseForm
    template_name = 'BudgetingApp/RecurringExpense_form.html'
    success_url = reverse_lazy('recurringexpense-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class RecurringExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = RecurringExpense
    form_class = RecurringExpenseForm
    template_name = 'BudgetingApp/RecurringExpense_form.html'
    success_url = reverse_lazy('recurringexpense-list')

    def get_queryset(self):
        return RecurringExpense.objects.filter(owner=self.request.user)


class RecurringExpenseDeleteView(LoginRequiredMixin, DeleteView):
    model = RecurringExpense
    template_name = 'BudgetingApp/RecurringExpense_confirm_delete.html'
    success_url = reverse_lazy('recurringexpense-list')

    def get_queryset(self):
        return RecurringExpense.objects.filter(owner=self.request.user)


# IncomeSource CRUD
class IncomeSourceListView(LoginRequiredMixin, ListView):
    model = IncomeSource
    template_name = 'BudgetingApp/IncomeSource_list.html'

    def get_queryset(self):
        return IncomeSource.objects.filter(owner=self.request.user)


class IncomeSourceCreateView(LoginRequiredMixin, CreateView):
    model = IncomeSource
    form_class = IncomeSourceForm
    template_name = 'BudgetingApp/IncomeSource_form.html'
    success_url = reverse_lazy('incomesource-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class IncomeSourceUpdateView(LoginRequiredMixin, UpdateView):
    model = IncomeSource
    form_class = IncomeSourceForm
    template_name = 'BudgetingApp/IncomeSource_form.html'
    success_url = reverse_lazy('incomesource-list')

    def get_queryset(self):
        return IncomeSource.objects.filter(owner=self.request.user)


class IncomeSourceDeleteView(LoginRequiredMixin, DeleteView):
    model = IncomeSource
    template_name = 'BudgetingApp/IncomeSource_confirm_delete.html'
    success_url = reverse_lazy('incomesource-list')

    def get_queryset(self):
        return IncomeSource.objects.filter(owner=self.request.user)


# SavingsAccount CRUD
class SavingsAccountListView(LoginRequiredMixin, ListView):
    model = SavingsAccount
    template_name = 'BudgetingApp/SavingsAccount_list.html'

    def get_queryset(self):
        return SavingsAccount.objects.filter(owner=self.request.user)


class SavingsAccountCreateView(LoginRequiredMixin, CreateView):
    model = SavingsAccount
    form_class = SavingsAccountForm
    template_name = 'BudgetingApp/SavingsAccount_form.html'
    success_url = reverse_lazy('savingsaccount-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class SavingsAccountUpdateView(LoginRequiredMixin, UpdateView):
    model = SavingsAccount
    form_class = SavingsAccountForm
    template_name = 'BudgetingApp/SavingsAccount_form.html'
    success_url = reverse_lazy('savingsaccount-list')

    def get_queryset(self):
        return SavingsAccount.objects.filter(owner=self.request.user)


class SavingsAccountDeleteView(LoginRequiredMixin, DeleteView):
    model = SavingsAccount
    template_name = 'BudgetingApp/SavingsAccount_confirm_delete.html'
    success_url = reverse_lazy('savingsaccount-list')

    def get_queryset(self):
        return SavingsAccount.objects.filter(owner=self.request.user)


# BudgetReminder CRUD
class BudgetReminderListView(LoginRequiredMixin, ListView):
    model = BudgetReminder
    template_name = 'BudgetingApp/BudgetReminder_list.html'

    def get_queryset(self):
        return BudgetReminder.objects.filter(owner=self.request.user)


class BudgetReminderCreateView(LoginRequiredMixin, CreateView):
    model = BudgetReminder
    form_class = BudgetReminderForm
    template_name = 'BudgetingApp/BudgetReminder_form.html'
    success_url = reverse_lazy('budgetreminder-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BudgetReminderUpdateView(LoginRequiredMixin, UpdateView):
    model = BudgetReminder
    form_class = BudgetReminderForm
    template_name = 'BudgetingApp/BudgetReminder_form.html'
    success_url = reverse_lazy('budgetreminder-list')

    def get_queryset(self):
        return BudgetReminder.objects.filter(owner=self.request.user)


class BudgetReminderDeleteView(LoginRequiredMixin, DeleteView):
    model = BudgetReminder
    template_name = 'BudgetingApp/BudgetReminder_confirm_delete.html'
    success_url = reverse_lazy('budgetreminder-list')

    def get_queryset(self):
        return BudgetReminder.objects.filter(owner=self.request.user)


# FinancialReport List + Detail
class FinancialReportListView(LoginRequiredMixin, ListView):
    model = FinancialReport
    template_name = 'BudgetingApp/FinancialReport_list.html'

    def get_queryset(self):
        return FinancialReport.objects.filter(owner=self.request.user)


class FinancialReportDetailView(LoginRequiredMixin, DetailView):
    model = FinancialReport
    template_name = 'BudgetingApp/FinancialReport_detail.html'

    def get_queryset(self):
        return FinancialReport.objects.filter(owner=self.request.user)
    
    




def payment(request):
    """
    Display payment form and trigger STK push on POST.
    Uses MPESA credentials from Django settings.
    """
    if request.method == "POST":
        phone = request.POST.get("phone")
        amount = request.POST.get("amount")

        # basic validation
        if not phone or not amount:
            from django.contrib import messages
            messages.error(request, "Phone and amount are required.")
            return render(request, "BudgetingApp/payment_form.html", {"phone": phone, "amount": amount})

        try:
            # get access token
            token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
            r = requests.get(token_url, auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET), timeout=30)
            r.raise_for_status()
            access_token = r.json().get("access_token")

            shortcode = settings.MPESA_EXPRESS_SHORTCODE
            passkey = settings.MPESA_PASSKEY
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            password = base64.b64encode(f"{shortcode}{passkey}{timestamp}".encode()).decode()

            payload = {
                "BusinessShortCode": shortcode,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": int(amount),
                "PartyA": phone,
                "PartyB": shortcode,
                "PhoneNumber": phone,
                "CallBackURL": request.build_absolute_uri("/BudgetingApp/mpesa-callback/"),
                "AccountReference": "BudgetingApp",
                "TransactionDesc": "Budget payment"
            }

            headers = {"Authorization": f"Bearer {access_token}", "Content-Type": "application/json"}
            stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            resp = requests.post(stk_url, json=payload, headers=headers, timeout=30)
            resp.raise_for_status()
            # Pass response to template or messages
            from django.contrib import messages
            messages.success(request, "STK Push sent. Check your phone to complete the payment.")
            return redirect("payment-success")
        except Exception as e:
            from django.contrib import messages
            messages.error(request, f"Error sending STK Push: {e}")
            return render(request, "BudgetingApp/payment_form.html", {"phone": phone, "amount": amount})

    return render(request, "BudgetingApp/payment_form.html")


def payment_success(request):
    return render(request, "BudgetingApp/payment_success.html")


@csrf_exempt
def mpesa_callback(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        # Here you could parse the callback and save to DB or update transaction status
        print("Mpesa callback received:", data)
        return JsonResponse({"ResultCode": 0, "ResultDesc": "Callback processed"})
    except Exception as e:
        print("Mpesa callback parse error:", e)
        return JsonResponse({"ResultCode": 1, "ResultDesc": "Error parsing callback"}, status=400)
