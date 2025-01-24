from django.urls import path
from .views import customLoginView, UserRegistrationView, VendorDashboardView, BuyerDashboardView, UserDashboardView, no_permission

urlpatterns = [
    path('login/', customLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('vendor/dashboard/', VendorDashboardView.as_view(), name='vendor_dashboard'),
    path('buyer/dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('user/dashboard/', UserDashboardView.as_view(), name='user_dashboard'),
    path('no_permission/dashboard/', no_permission, name='no_permission_dashboard'),
 

]