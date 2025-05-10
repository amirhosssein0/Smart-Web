from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup_view, name='signup'),
    path('delete/account/', DeleteAccountView.as_view(), name='delete_account'),
    path('password/reset/', CustomPasswordReset.as_view(), name='password_reset'),
    path('password/reset/done/', CustomPasswordDone.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', CustomPasswordConfirm.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', CustomPasswordComplete.as_view(), name='password_reset_complete'),
]