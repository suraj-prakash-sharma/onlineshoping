from django.contrib.auth.password_validation import password_changed
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import UserForm,PcForm,passresetform,mysetpasswordform
urlpatterns = [
    path('', views.home),
    path('product-detail/<int:pro_id>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/',views.showcart,name='cart'),
    path('pluscart/',views.pluscart,name='pluscart'),
    path('minuscart/',views.minuscart,name='minuscart'),
    path('removecart/',views.removecart),
    path('paymentdone/',views.paymentdone),
    path('buy/', views.buy_now, name='buy-now'),
    path('accounts/profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('laptop/', views.laptop, name='laptop'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=UserForm), name='login'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=PcForm),name='passwordchange'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='password_change_done'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password-reset.html',form_class=passresetform),name='password-reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password-reset-done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password-reset-confirm.html',form_class=mysetpasswordform),name='password_reset_confirm'),
    path('password-reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password-reset-complete.html'),name='password_reset_complete'),
   
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]
