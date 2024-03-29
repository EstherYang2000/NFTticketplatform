from cProfile import label
from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.template import loader
import unicodedata
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Events,CustomerProfile,Transfer
from django.forms.fields import DateTimeField
from django.forms.fields import DateTimeInput
from .models import Order




UserModel = get_user_model()


def _unicode_ci_compare(s1, s2):
    """
    Perform case-insensitive comparison of two identifiers, using the
    recommended algorithm from Unicode Technical Report 36, section
    2.11.2(B)(2).
    """
    return (
        unicodedata.normalize("NFKC", s1).casefold()
        == unicodedata.normalize("NFKC", s2).casefold()
    )

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
        is_staff = forms.BooleanField(label="Comapny or not?" ,help_text='Company registration?',required=False)

        fields = ('username', 'email','password1', 'password2','is_staff')
        # widgets = {
        #     'is_staff': forms.BooleanField(attrs={'width':'50px','height':'50px',
        #         }),
        #     'email': forms.fields.EmailInput(attrs={
        #                 'class':'form-control',
        #                 'placeholder':'Email here',
        #         }),
        #     'password1': forms.fields.PasswordInput(attrs={
        #                 'class':'form-control',
        #                 'placeholder':'Password here',
        #         }),
        #     'password2': forms.fields.PasswordInput(attrs={
        #                 'class':'form-control',
        #                 'placeholder':'Re-enter Your Password here',
        #         }),

        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':_('Username.....'),'class':'form-control rounded-pill personal-input'})
        self.fields['email'].widget.attrs.update({'placeholder':_('Email....'),'class':'form-control rounded-pill personal-input'})
        self.fields['password1'].widget.attrs.update({'placeholder':_('Password....'),'class':'form-control rounded-pill personal-input'})
        self.fields['password2'].widget.attrs.update({'placeholder':_('Repeat password....'),'class':'form-control rounded-pill personal-input'})
        self.fields['is_staff'].widget.attrs.update({'style':'width:30 px;height:30px;float: left ; border: none;width=30%;',})
class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'

# from django.core.validators import RegexValidator
# my_validator = RegexValidator(r"^0x{1}[a-z\d]{64}$", "Unvalid or empty wallet id entered!")

class CustomerProfileForm(forms.ModelForm):
    personal_walletId = forms.CharField(
        max_length=100,
        label='User Wallet:',
        # validators=[my_validator],
        widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'0x00012132423423'}))
    avatars =forms.ImageField()
    class Meta:
        model = CustomerProfile
        fields = ('personal_walletId','avatars')
        widgets = {
            'personal_walletId': forms.TextInput(attrs={'class': 'form-control'}),

        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['personal_walletId']

class EventCreateForm(forms.ModelForm):
    CATEGORY = (
            ('Performance', 'Performance'),
            ('exhibition', 'exhibition'),
            )
    category = forms.CharField(label='活動類型',widget=forms.RadioSelect(choices=CATEGORY))
    eventname = forms.CharField(max_length=100, label='活動名稱:', widget = forms.TextInput(attrs={'class': 'form-control rounded-pill','placeholder':'OneOffs NFT 國際藝術博覽會'}))
    eventdescription = forms.CharField(max_length=200, label='活動內容:',widget = forms.TextInput(attrs={'class': 'form-control rounded-pill','placeholder':'W Taipei 登場。橫跨藝術、區塊鏈、 VR 等不同領域，為未來的全球島嶼連線策展鳴啟第一槍。',}))
    eventticketnumber = forms.IntegerField( label='票券數量:',widget = forms.TextInput(attrs={'class': 'form-control rounded-pill','placeholder':'50','maxlength':'100',
    'minlength':'1'}))
    eventprice = forms.DecimalField(label='票券價格:',widget = forms.NumberInput(attrs={'class': 'form-control rounded-pill','placeholder':'0.99', }))
    date_StartTime=forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M:%S'],
        widget=forms.DateTimeInput(
            format ='%d/%m/%Y %H:%M:%S',
            attrs={
            'type': 'datetime-local',
            'class': 'form-control rounded-pill datetimepicker-input',
            'placeholder':'March 31, 2022, 12:56 p.m.'
            # 'data-target': '#datetimepicker1'
        })
    )
    date_EndTime=forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M:%S'],
        widget=forms.DateTimeInput(
            format ='%d/%m/%Y %H:%M:%S',
            attrs={
            'type': 'datetime-local',
            'class': 'form-control rounded-pill datetimepicker-input',
            'placeholder':'April 30, 2022, 12:56 p.m.'

            # 'data-target': '#datetimepicker1'
        })
    )
    event_pic = forms.ImageField()

#        input_formats=['%m/%d/%y %H:%M %p'],


    class Meta:
        model = Events
        fields = ('category', 'eventname', 'eventdescription', 'eventticketnumber', 'eventprice','date_StartTime','date_EndTime','event_pic')
        widgets = {
            'category': forms.RadioSelect(attrs={'class': 'form-control rounded-pill'}),
            'eventname': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'eventdescription': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'eventticketnumber': forms.TextInput(attrs={'class': 'form-control rounded-pill'}),
            'eventprice': forms.NumberInput(attrs={'class': 'form-control rounded-pill'}),
            'date_StartTime':forms.DateTimeInput(attrs={'class': 'form-control rounded-pill'}),
            'date_EndTime':forms.DateTimeInput(attrs={'class': 'form-control rounded-pill'}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['eventname']




class OrderForm(forms.ModelForm):
    # user_name = forms.CharField(max_length=100)
    # wallet_ID= forms. CharField(max_length=100)
    # email = forms.EmailField()
    # eventname = forms.CharField(max_length=100)
    # eventcategory = forms.CharField(max_length=100)
    # ordernumber = forms.DecimalField(widget=forms.NumberInput)
    class Meta:
        model = Order
        fields = '__all__'
class AcceptTransferForm(forms.ModelForm):
    # user_name = forms.CharField(max_length=100)
    # wallet_ID= forms. CharField(max_length=100)
    # email = forms.EmailField()
    # eventname = forms.CharField(max_length=100)
    # eventcategory = forms.CharField(max_length=100)
    # ordernumber = forms.DecimalField(widget=forms.NumberInput)
    class Meta:
        model = Transfer
        fields = '__all__'

# class OrderFormStepOne(forms.ModelForm):
#     user_name = forms.CharField(max_length=100)
#     wallet_ID= forms. CharField(max_length=100)
#     email = forms.EmailField()

#     class Meta:
# 	    model = Order

# class OrderFormStepTwo(forms.ModelForm):
#     eventname = forms.CharField(max_length=100)
#     eventcategory = forms.CharField(max_length=100)
#     ordernumber = forms.DecimalField(widget=forms.NumberInput)
#     class Meta:
# 	    model = Order
# class OrderFormStepThree(forms.ModelForm):
#     ticketcost = forms.DecimalField(max_length=100)
#     handlingcharge = forms.DecimalField(max_length=100)
#     totalcost =forms.DecimalField(max_length=100)
#     class Meta:
# 	    model = Order

    #     self.fields['category'].widget.attrs.update({
    #         'class': 'form-input',
    #         'required':'True',
    #         'name':'category',
    #         'id':'category',
    #         'type':'radio',
    #         })
    #     self.fields['eventname'].widget.attrs.update({
    #         'class': 'form-control',
    #         'required':'True',
    #         'name':'username',
    #         'id':'username',
    #         'type':'text',
    #         'placeholder':'OneOffs NFT 國際藝術博覽會',
    #         'maxlength': '20',
    #         'minlength': '6',
    #         })


    #     self.fields['eventdescription'].widget.attrs.update({
    #         'class': 'form-control',
    #         'required':'True',
    #         'name':'eventdescription',
    #         'id':'eventdescription',
    #         'type':'text',
    #         'placeholder':'W Taipei 登場。橫跨藝術、區塊鏈、 VR 等不同領域，為未來的全球島嶼連線策展鳴啟第一槍。回顧 2021 年，OneOffs 團隊參與舉辦今年五月的 WHAAAAAT’S 國際當代藝術博覽會，吸引超過萬人造訪，並締造超過 5,000 萬的銷售額佳績。',
    #         'maxlength': '100',
    #         'minlength': '20',
    #         })
    #     self.fields['eventticketnumber'].widget.attrs.update({
    #         'class': 'form-control',
    #         'required':'True',
    #         'name':'eventticketnumber',
    #         'id':'eventticketnumber',
    #         'type':'number',
    #         'placeholder':'50',
    #         'maxlength':'20',
    #         'minlength':'1'
    #         })
    #     self.fields['eventprice'].widget.attrs.update({
    #         'class': 'form-control',
    #         'required':'True',
    #         'name':'eventprice',
    #         'id':'eventprice',
    #         'type':'number',
    #         'placeholder':'0.99',
    #         'maxlength':'22',
    #         'minlength':'1'
    #         })
        # self.fields['date_StartTime'].widget.attrs.update({
        #     'class': 'form-control',
        # #     'required':'True',
        # #     # 'name':'activity-start-datetime',
        # #     # 'id':'activity-start-datetime',
        # #     'type':'datetime-local',
        # #     # 'maxlength':'50',
        # #     # 'minlength':'1'
        #     })
        # self.fields['date_EndTime'].widget.attrs.update({
        #     'class': 'form-control',
        # #     # 'required':'True',
        # #     # 'name':'date_EndTime',
        # #     'id':'datetimepicker1',
        # #     # 'maxlength':'50',
        # #     # 'minlength':'1'
        #     })


    # CATEGORY = (('exhibition', 'Performance'),)
    # category = forms.CharField(label='活動類型',widget=forms.RadioSelect(choices=CATEGORY))
    # eventname = forms.CharField(max_length=100, label='活動名稱:')
    # eventdescription = forms.CharField(max_length=200, label='活動內容:')
    # eventticketnumber = forms.IntegerField( label='票券數量:')
    # eventprice = forms.DecimalField(label='票券價格:')
    # date_StartTime = forms.DateField( label='活動開始日期時間:')
    # date_EndTime = forms.DateField( label='活動結束日期時間:')
    # date_StartTime = forms.DateTimeField( label='活動開始日期時間:',widget=DateTimePickerInput)
    # date_EndTime = forms.DateTimeField(label='活動結束日期時間:',widget=DateTimePickerInput)


    # def clean_email(self):
    #     email = self.cleaned_data['email'].lower()
    #     try:
    #         user = User.objects.get(email =email)
    #     except Exception as e:
    #         return email
    #     raise forms.ValidationError(f"Email{email} is already taken")
    # def clean_username(self):
    #     username = self.cleaned_data['username'].lower()
    #     try:
    #         user = User.objects.get(username =username)
    #     except Exception as e:
    #         return username
    #     raise forms.ValidationError(f"username{username} is already taken")

    # class loginInForm(UserCreationForm):
    #     class Meta:
    #         model = User

    #         fields = ('email','password1')
        # def clean_email(self):
        #     email = self.cleaned_data['email'].lower()
        #     try:
        #         user = User.objects.get(email =email)
        #     except Exception as e:
        #         return email
        #     raise forms.ValidationError(f"Email{email} is already taken")
        # def clean_username(self):
        #     username = self.cleaned_data['username'].lower()
        #     try:
        #         user = User.objects.get(username =username)
        #     except Exception as e:
        #         return username
        #     raise forms.ValidationError(f"username{username} is already taken")

# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(
#         label=_("Email"),
#         max_length=254,
#         widget=forms.EmailInput(attrs={"autocomplete": "email"}),
#     )

#     def send_mail(
#         self,
#         subject_template_name,
#         email_template_name,
#         context,
#         from_email,
#         to_email,
#         html_email_template_name=None,
#     ):
#         """
#         Send a django.core.mail.EmailMultiAlternatives to `to_email`.
#         """
#         subject = loader.render_to_string(subject_template_name, context)
#         # Email subject *must not* contain newlines
#         subject = "".join(subject.splitlines())
#         body = loader.render_to_string(email_template_name, context)

#         email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
#         if html_email_template_name is not None:
#             html_email = loader.render_to_string(html_email_template_name, context)
#             email_message.attach_alternative(html_email, "text/html")

#         email_message.send()

#     def get_users(self, email):
#         """Given an email, return matching user(s) who should receive a reset.
#         This allows subclasses to more easily customize the default policies
#         that prevent inactive users and users with unusable passwords from
#         resetting their password.
#         """
#         email_field_name = UserModel.get_email_field_name()
#         active_users = UserModel._default_manager.filter(
#             **{
#                 "%s__iexact" % email_field_name: email,
#                 "is_active": True,
#             }
#         )
#         return (
#             u
#             for u in active_users
#             if u.has_usable_password()
#             and _unicode_ci_compare(email, getattr(u, email_field_name))
#         )

#     def save(
#         self,
#         domain_override=None,
#         subject_template_name="registration/password_reset_subject.txt",
#         email_template_name="registration/password_reset_email.html",
#         use_https=False,
#         token_generator=default_token_generator,
#         from_email=None,
#         request=None,
#         html_email_template_name=None,
#         extra_email_context=None,
#     ):
#         """
#         Generate a one-use only link for resetting password and send it to the
#         user.
#         """
#         email = self.cleaned_data["email"]
#         if not domain_override:
#             current_site = get_current_site(request)
#             site_name = current_site.name
#             domain = current_site.domain
#         else:
#             site_name = domain = domain_override
#         email_field_name = UserModel.get_email_field_name()
#         for user in self.get_users(email):
#             user_email = getattr(user, email_field_name)
#             context = {
#                 "email": user_email,
#                 "domain": domain,
#                 "site_name": site_name,
#                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                 "user": user,
#                 "token": token_generator.make_token(user),
#                 "protocol": "https" if use_https else "http",
#                 **(extra_email_context or {}),
#             }
#             self.send_mail(
#                 subject_template_name,
#                 email_template_name,
#                 context,
#                 from_email,
#                 user_email,
#                 html_email_template_name=html_email_template_name,
#             )


# class SetPasswordForm(forms.Form):
#     """
#     A form that lets a user change set their password without entering the old
#     password
#     """

#     error_messages = {
#         "password_mismatch": _("The two password fields didn’t match."),
#     }
#     new_password1 = forms.CharField(
#         label=_("New password"),
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         strip=False,
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     new_password2 = forms.CharField(
#         label=_("New password confirmation"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#     )

#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super().__init__(*args, **kwargs)

#     def clean_new_password2(self):
#         password1 = self.cleaned_data.get("new_password1")
#         password2 = self.cleaned_data.get("new_password2")
#         if password1 and password2:
#             if password1 != password2:
#                 raise ValidationError(
#                     self.error_messages["password_mismatch"],
#                     code="password_mismatch",
#                 )
#         password_validation.validate_password(password2, self.user)
#         return password2

#     def save(self, commit=True):
#         password = self.cleaned_data["new_password1"]
#         self.user.set_password(password)
#         if commit:
#             self.user.save()
#         return self.user


