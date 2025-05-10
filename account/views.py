from django.shortcuts import render, redirect
from django.contrib.auth import  login, logout
from account.forms import *
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView


class CustomLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('pages:home')
    success_message = "Login Successfully"
    

class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html'  
    next_page = reverse_lazy('pages:home') 


    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            return super().dispatch(request, *args, **kwargs)
        return TemplateView.as_view(template_name=self.template_name)(request, *args, **kwargs)


@csrf_protect
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,('Signup Successfully'))
            return redirect('pages:home')
        else:
            messages.error(request, ('There Is A Problem'))
            return redirect('account:signup')
            
    else:
        form = SignupForm()
        
    return render(request, 'account/signup.html', {'form':form})
    

class CustomPasswordReset(PasswordResetView):
    template_name = 'account/password_reset.html'
    email_template_name = 'account/password_reset_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_url = reverse_lazy('account:password_reset_done')
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Password reset link sent to your email")
        return response

class CustomPasswordDone(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class CustomPasswordConfirm(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account:password_reset_complete')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your password has been updated successfully")
        return response

class CustomPasswordComplete(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
    
class DeleteAccountView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'account/delete_account.html'
    success_url = reverse_lazy('pages:home')
    
    def get_object(self, queryset = None):
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        logout(request)
        messages.success(request, 'Account Delete Successfully')
        return response
    






