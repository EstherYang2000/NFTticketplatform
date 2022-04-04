from datetime import timezone
from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver



class CustomerProfile(models.Model):
    # Customer_id = models.AutoField(primary_key=True)
    customeruser = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    personal_email = models.CharField(max_length=200, null=True)
    personal_walletId = models.CharField(max_length=100,blank=True)
    avatars = models.ImageField(upload_to=settings.MEDIA_ROOT,default='imgs/avatar.jpg', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.customeruser.username
pass

class CompanyProfile(models.Model):
    # company_id = models.AutoField(primary_key=True)
    companyuser = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    company_email = models.CharField(max_length=200, null=True)
    company_walletId = models.CharField(max_length=100,blank=True)
    company_avatars = models.ImageField(upload_to=settings.MEDIA_ROOT, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.companyuser.username
pass


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Events(models.Model):
    CATEGORY = (
            ('Performance', 'Performance'),
            ('exhibition', 'exhibition'),
            )
    # event_id = models.AutoField(primary_key=True)
    companycreater = models.ForeignKey(CompanyProfile,related_name="events", on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    eventname = models.CharField(max_length=200, null=True)
    eventdescription = models.CharField(max_length=200, null=True, blank=True)
    eventticketnumber = models.IntegerField(null=False)
    eventprice = models.DecimalField(null=True,max_digits=5, decimal_places=2)
    totalorderedTicket = models.IntegerField(null=False,default=0)
    remainedTicketNum = models.IntegerField(null=False,default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_StartTime = models.DateTimeField(null=True)
    date_EndTime = models.DateTimeField(null=True)
    event_pic = models.ImageField(null = True, blank = True,upload_to=settings.MEDIA_ROOT)
    status =(("Not Started","Not Started"),("Ongoing","Ongoing"),("Expired","Expired"))
    status = models.CharField(max_length=200, null=True, choices=status,default="Not Started")

    # tags = models.ManyToManyField(Tag)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE =300,300
        if self.event_pic:
            pic = Image.open(self.event_pic.path)
            pic.thumbnail(SIZE,Image.LANCZOS)
    def __str__(self):
        return self.eventname
    def changestatus(self):
        status=""
        if timezone.now() < self.date_StartTime:
            status = "Not Started"
        elif timezone.now() > self.date_StartTime and timezone.now() < self.date_EndTime:
            status ="Ongoing"
        else:
            status ="Expired"
        return status

class Order(models.Model):
    STATUS = (
            ('Unpaid', 'Unpaid'),
            ('Paid', 'Paid'),
            )
    tokenID = models.IntegerField(null=False,default=0)
    customer = models.ForeignKey(CustomerProfile, null=True, on_delete=models.SET_NULL)
    events = models.ForeignKey(Events, null=True, on_delete=models.SET_NULL)

    orderNumber = models.IntegerField(null=False,default=1)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    orderPrice = models.DecimalField(null=False,max_digits=5, decimal_places=4,default=0)
    orderHandlingfee =models.DecimalField(null=False,max_digits=5, decimal_places=4,default=0)
    orderTotalPrice = models.DecimalField(null=False,max_digits=5, decimal_places=4,default=0)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.events.eventname


class Transfer(models.Model):
    STATUS = (
            #sender send the transferring form
            ('UnConfirmed', 'UnConfirmed'), #
            ('Success', 'Success'),
            )
    Sender = models.ForeignKey(CustomerProfile, null=True, related_name="sender",on_delete=models.SET_NULL)
    Receiver = models.ForeignKey(CustomerProfile, null=True, related_name="receiver",on_delete=models.SET_NULL)
    senderOrder = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    tranferEvent = models.ForeignKey(Events, null=True, on_delete=models.SET_NULL)
    transferFee = models.DecimalField(null=False,max_digits=5, decimal_places=4,default=0)
    senderNote = models.CharField(max_length=200, null=True, blank=True)
    receiverNote = models.CharField(max_length=200, null=True, blank=True)
    transferDate_created = models.DateTimeField(auto_now_add=True, null=True)
    transferDate_Success = models.DateTimeField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS,default="UnConfirmed")

    def __str__(self):
        return self.status


# from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     personal_id = models.AutoField(primary_key=True, blank=False)
#     personal_walletId = models.CharField(max_length=100,blank=False)


# class CustomUser(AbstractUser):
#     personal_id = models.AutoField(primary_key=True, blank=False)
#     personalwalletId = models.CharField(max_length=100,blank=False)
#     # is_staff = models.BooleanField(_('staff'), default=False)




# from django.db import models
# from django.core.mail import send_mail
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _

# from .managers import UserManager


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email address'), unique=True)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
#     is_active = models.BooleanField(_('active'), default=True)
#     is_staff = models.BooleanField(_('staff'), default=True)
#     personal_id = models.AutoField(primary_key=True, blank=False)

#     personal_walletId = models.CharField(max_length=100,blank=False)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

#     def get_full_name(self):
#         '''
#         Returns the first_name plus the last_name, with a space in between.
#         '''
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()

#     def get_short_name(self):
#         '''
#         Returns the short name for the user.
#         '''
#         return self.first_name

#     def email_user(self, subject, message, from_email=None, **kwargs):
#         '''
#         Sends an email to this User.
#         '''
#         send_mail(subject, message, from_email, [self.email], **kwargs)


















# from django.db import models
# from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser



# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name='profile'
#     )
#     personal_id = models.AutoField(primary_key=True, blank=False)
#     personal_walletId = models.CharField(max_length=100,blank=False)

#     pass

# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     personal_id = models.AutoField(primary_key=True, blank=False,on_delete=models.CASCADE)
#     personal_walletId = models.CharField(max_length=100,blank=False)

#     def __unicode__(self):
#         return self.user.username
#     def __str__(self):
#         return  self.user.email

# def create_user_profile(sender, instance, created, **kwargs):
#     """Create the UserProfile when a new User is saved"""
#     if created:
#         profile = UserProfile()
#         profile.user = instance
#         profile.save()


# class CustomUser(AbstractUser):
#     class Meta:
#         ordering = ["email"]
#     def __str__(self):
#         return  f"{self.username}:{self.email}"

# class MyUserManager(BaseUserManager):
#     def create_user(self,email,personal_walletId,password=None):
#         if not email:
#             raise ValueError("email is required")
#         if not personal_walletId:
#             raise ValueError("WalletId is required")
#         user = self.model(
#             personal_email=self.normalize_email(email),
#             personal_walletId = personal_walletId
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     pass
#     def create_superuser(self,email,personal_walletId,password=None):
#         user=self.create_user(
#             personal_email = email,
#             personal_password = password,
#             personal_walletId = personal_walletId
#         )
#         user.is_admin = True
#         user.is_superUser = True
#         user.save(using = self._db)
#         return user
#     pass



# class MyUser(AbstractBaseUser):
#     email = models.EmailField(verbose_name=("Display Email"),max_length=100,help_text=("will be shown"),unique=True)
#     personal_id = models.AutoField(primary_key=True, blank=False)
#     personal_walletId = models.CharField(max_length=100,blank=False)
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(null=True)
#     is_admin = models.BooleanField(default=FALSE)
#     is_superuser =models.BooleanField(default=FALSE)
#     is_active = models.BooleanField(default=True)
#     USERNAME_FIELD  ="email"
#     REQUIRED_FIELDS  = ['personal_walletId']
#     objects = MyUserManager()

#     def __str__(self):
#         return self.email
#     def has_perm(self,perm,obj=None):
#         return True
#     def has_module_perms(self,app_label):
#         return True

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     ersonal_id = models.AutoField(primary_key=True, blank=False)
#     personal_walletId = models.CharField(max_length=100,blank=False)

#     def __unicode__(self):
#         return self.user.username

# class   Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     personal_id = models.AutoField(primary_key=True)
#     personal_walletId = models.CharField(max_length=30)

#     def __str__(self):
#         return self.personal_id

# class   Company(models.Model):
#     Company_id = models.AutoField(primary_key=True)
#     Company_email = models.EmailField(unique=True)
#     Company_name = models.CharField(max_length=150)
#     Company_password = models.CharField(max_length=30)
#     Company_repassword = models.CharField(max_length=30)
#     Company_walletid = models.CharField(max_length=50)
#     def __str__(self):
#         return self.Company_id

# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
# from django.contrib.auth import get_user_model
# from django.utils import timezone

# class AccountManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, email, name, walletid, password, **extra_fields):
#         values = [email, name, walletid]
#         field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
#         for field_name, value in field_value_map.items():
#             if not value:
#                 raise ValueError('The {} value must be set'.format(field_name))

#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             name=name,
#             walletid=walletid,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, name, walletid, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, name, walletid, password, **extra_fields)

#     def create_superuser(self, email, name, walletid, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, name, walletid, password, **extra_fields)


# class Account(AbstractBaseUser, PermissionsMixin):
#     personal_id = models.AutoField(primary_key=True)
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=150)
#     walletid = models.CharField(max_length=50)
#     # picture = models.ImageField(blank=True, null=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(null=True)

#     objects = AccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'walletid']

#     def get_full_name(self):
#         return self.name

#     def get_short_name(self):
#         return self.name.split()[0]




# class MyCustomerManager(BaseUserManager):
#     def create_user(self,personal_email,personal_userName,personal_walletId,personal_password=None):
#         if not personal_email:
#             raise ValueError("email is required")
#         if not personal_userName:
#             raise ValueError("email is required")
#         # if not personal_password:
#         #     raise ValueError("password is required")
#         # if not personal_repassword:
#         #     raise ValueError("repassword is required")
#         if not personal_walletId:
#             raise ValueError("WalletId is required")
#         user = self.model(
#             personal_email=self.normalize_email(personal_email),
#             personal_userName = personal_userName,
#             #personal_password = personal_password,
#             #personal_repassword = personal_repassword,
#             personal_walletId = personal_walletId

#         )
#         user.set_password(personal_password)
#         user.save(using=self._db)
#         return user
#     pass
#     def create_superuser(self,personal_email,personal_userName,personal_walletId,password=None):
#         user=self.create_user(
#             personal_email = personal_email,
#             personal_userName = personal_userName,
#             personal_password = password,
#             #personal_repassword = personal_repassword,
#             personal_walletId = personal_walletId

#         )
#         user.is_admin = True
#         user.is_superUser = True
#         user.save(using = self._db)
#         return user
#     pass



# class MyCustomer(AbstractBaseUser):
#     personal_id = models.AutoField(primary_key=True)
#     personal_email = models.EmailField(verbose_name="email address",max_length=60, unique=True)
#     personal_userName = models.CharField(verbose_name ="User name",max_length=30)
#     #personal_password = models.CharField(max_length=100,null=False)
#     #personal_repassword = models.CharField(max_length=100,null=False)
#     personal_walletId = models.CharField(max_length=100,null=False)
#     personal_date_joined = models.DateTimeField(verbose_name="",auto_now_add=True)
#     personal_last_joined = models.DateTimeField(verbose_name="",auto_now_add=True)
#     is_admin=models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)

#     USERNAME_FIELD  ="personal_email"
#     REQUIRED_FIELDS  = ['personal_userName','personal_walletId']
#     objects = MyCustomerManager()

#     def __str__(self):
#         return self.personal_email
#     def has_perm(self,perm,obj=True):
#         return True
#     def has_module_perms(self,app_label):
#         return True

# class Customer(models.Model):
#     personal_id = models.AutoField(primary_key=True)
#     personal_userName = models.CharField(max_length=30)
#     personal_email = models.EmailField(max_length=100,default=False)
#     personal_password = models.CharField(max_length=100,default=False)
#     personal_repassword = models.CharField(max_length=100,default=False)
#     personal_walletId = models.CharField(max_length=100,default=False)


#     def __str__(self):
#         return str(self.personal_id)
#     pass
# Create your models here.
# class AccountManager(BaseUserManager):
#     def create_user(self, email, walletid, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             email=self.normalize_email(email),
#             walletid=walletid,
#           )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, walletid, password=None):
#         user = self.create_user(
#              email,
#              password=password,
#              walletid=walletid,
#           )
#          user.is_admin = True
#          user.save(using=self._db)
#          return user
#     pass
