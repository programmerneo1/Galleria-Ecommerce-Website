from app.models import Wishlist
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.home),
    path('productdetail/<int:pk>',
         views.ProductDetailView.as_view(), name='productdetail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('ordersuccess/', views.order_success, name='order_success'),
    path('about_us/', views.about_us, name='about_us'),
    path('terms_and_conditions/', views.terms_and_conditions,
         name='terms_and_conditions'),
    path('privacy_and_policy/', views.privacy_and_policy,
         name='privacy_and_policy'),
    path('delivery_information/', views.delivery_information,
         name='delivery_information'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('wishlist/', views.wishlist_items, name='wishlist_items'),
    path('wishlist/<int:pk>', views.wishlist, name='wishlist'),
    path('remove-from-wishlist/', views.remove_from_wishlist,
         name='remove_from_wishlist'),



    path('buy/', views.buy_now, name='buy-now'),
    #     path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('mens/', views.mens, name='mens'),
    path('mens/', views.MensProductView.as_view(), name='mens'),
    path('mens/<slug:data>', views.MensProductView.as_view(), name='Sortedmens'),

    path('womens/', views.WomensProductView.as_view(), name='womens'),

    path('mobile/', views.mobile, name='mobile'),


    path('deals/', views.Deals.as_view(), name='deals'),


    # for Users
    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),  # for the registration
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                                         authentication_form=LoginForm), name='login'),  # for the login
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),
         name='logout'),  # for the logout


    # for passwords
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',
                                                                  form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),  # onclick of changepassword
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'), name='passwordchangedone'),  # after filling the form of changepassword

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
