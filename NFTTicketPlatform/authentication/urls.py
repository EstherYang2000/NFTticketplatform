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
    path('exhibition/<int:pk>/exhibitionOrder',views.exhibitionOrder,name='exhibitionOrder'),

    path('searchEvent',views.searchEvent,name='searchEvent'),

    path('performance',views.performance,name='performance'),
    path('personal',views.personal,name='personal'),

    path("personal/personalAvatar",views.personalAvatar,name='personalAvatar'),
    path('personal/personalInfowallet',views.personalInfowallet,name='personalInfowallet'),
    path('personal/personalasset',views.personalasset,name='personalasset'),
    path('personal/Accept',views.Accept,name='Accept'),
    path('personal/Auth',views.Auth,name='Auth'),
    path('personal/personaltransfer',views.personaltransfer,name='personaltransfer'),
    path('personal/personalhelp',views.personalhelp,name='personalhelp'),



    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
    #     name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='pwd/password_reset.html'),name='password_reset'),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(template_name='pwd/password_reset_done.html'),name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>",auth_views.PasswordResetConfirmView.as_view(template_name='pwd/password_reset_confirm.html'),name='password_reset_confirm'),
    path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(template_name='pwd/password_reset_complete.html'),name ='password_reset_complete')

    # path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    #  name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    #  name='password_reset_complete'),


]



