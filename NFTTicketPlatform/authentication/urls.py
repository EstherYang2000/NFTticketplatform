from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from ecommerce import urls
urlpatterns = [
    path('',views.home,name="home"),
    path('login_user',views.login_user,name='login_user'),
    path('register',views.register,name='register'),
    path('signout_user',views.signout_user,name='signout_user'),
    path('company/',views.company,name='company'),
    path('company/eventcreatform',views.eventcreatform,name='eventcreatform'),
    path('company/createevent',views.createevent,name='createevent'),
    path('company/updateevent/<int:pk>',views.updateevent,name='updateevent'),
    path('company/deleteevent/<int:pk>',views.deleteevent,name='deleteevent'),
    path('company/companyInfowallet',views.companyInfowallet,name='companyInfowallet'),
    path('company/companyAsset',views.companyAsset,name='companyAsset'),
    path('company/salesstatus',views.salesstatus,name='salesstatus'),
    path('company/companyhelpcenter',views.companyhelpcenter,name='companyhelpcenter'),
    path('exhibition',views.exhibition,name='exhibition'),
    path('exhibition/<int:pk>',views.exhibitionDetail,name='exhibitionDetail'),

    path('performance',views.performance,name='performance'),



    # path('reset_Password/',auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="reset_password", ),
    # path('reset_Password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    # path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    # path('resetpassword_complete',auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_complete"),

    # path("password_reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
    #     name="password_reset_complete",
    # ),

 path("password_reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"),
        name="password_reset_complete",
    ),


    path('personal',views.personal,name='personal'),




]


#Password reset sent
#We’ve emailed you instructions for setting your password, if an account exists with the email you entered. You should receive them shortly.

#If you don’t receive an email, please make sure you’ve entered the address you registered with, and check your spam folder.

