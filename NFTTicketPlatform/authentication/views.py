import datetime
import email
from http.client import HTTPResponse
from multiprocessing import Event
from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib import messages
from operator import itemgetter
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .form import RegistrationForm,EventCreateForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import (
#     PasswordChangeForm,
#     PasswordResetForm,
#     SetPasswordForm,
# )
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.http import url_has_allowed_host_and_scheme, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import mysql.connector as sql
from mysql.connector import Error
from authentication.models import CompanyProfile,CustomerProfile,Events
UserModel = get_user_model()
from web3 import Web3,HTTPProvider
from hexbytes import HexBytes as hb
import sys

from django.dispatch import receiver
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from DjangoBackend import *
# sys.path.append("..")



# Create your views here.
# @login_required(login_url='login_user')
def home(request):
    return render(request,'index.html')
pass
def login_user(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method =="POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request,username = username, password= password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username OR password is incorrect')
            context = {}
            return render(request,'signIn.html',context)
    except Exception as e:
        print(e)
pass

Pn =" "
Pem = " "
Ppw1 = " "
Pw2 = " "
Pst=False



def register(request):
    global Pn,Pem,Ppw1,Pw2, Pst
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                print(username)
                is_staff = form.cleaned_data.get('is_staff')
                # if(is_staff == True):

                #     CompanyProfile.objects.create(companyuser=request.user)
                # else:
                #     CustomerProfile.objects.create(user=request.user)


                print(is_staff)

                try:

                    p=sql.connect(host='127.0.0.1',user='root',password='Sester890627',database='nftticketplatform')
                    if p.is_connected():

                        # 顯示資料庫版本
                        db_Info = p.get_server_info()
                        print("資料庫版本：", db_Info)

                        pcursor=p.cursor()
                        print("連資料庫成功")

                        d=request.POST
                        print("取得資料成功")
                        for key,value in d.items():
                            if key =='username':
                                Pn = value
                            elif key =='email':
                                Pem = value
                            elif key == 'password1':
                                Ppw1 = value
                            elif key =='password2' :
                                Ppw2 = value
                            else:
                                Pst = value
                                print(Pst)
                        print("取得各資料成功")
                        if (Ppw1 == Ppw2):
                            print("密碼符合")
                            if is_staff == True:
                                print("公司註冊")

                                companyuser = CompanyProfile.objects.create(companyuser = user,company_email = user.email)
                                # CompanyProfile.objects.create(user)
                                # name=user.objects.get(username=),
                                # companyuserID =companyuser.company_id
                                print("公司註冊完成")
                                person = "INSERT INTO companyprofile (companyName, companyEmail,companyPassword) VALUES (%s, %s,%s)"
                                val = (Pn, Pem,Ppw1)
                                pcursor.execute(person,val)
                                p.commit()

                                messages.success(request,"Successfully Insert the data into company database !!")
                                print("Successfully Insert the data into company database !!")


                            elif is_staff ==False:
                                print("顧客註冊")
                                customeruser = CustomerProfile.objects.create(companyuser=user)
                                # customeruserID = customeruser.Customer_id
                                person = "INSERT INTO customerprofile (CustomerName, CustomerEmail,CustomerPassword) VALUES (%s, %s,%s)"
                                val = (Pn, Pem,Ppw1)
                                pcursor.execute(person,val)
                                p.commit()
                                messages.success(request,"Successfully Insert the data into customer database !!")
                                print("Successfully Insert the data into customer database !!")


                        else:
                            print("密碼錯誤")
                            messages.success(request,"Check your password!!")
                except Error as e:
                    print("資料庫連接失敗：", e)

                finally:
                    if (p.is_connected()):
                        pcursor.close()
                        p.close()
                        print("資料庫連線已關閉")
                messages.success(request, 'Account was created for ' + user.username)
                return redirect('login_user')
        context = {'form':form}
        return render(request, 'signup.html', context)
pass


def signout_user(request):
    logout(request)
    # messages.success(request,("You were logged out!!"))
    return redirect('home')
pass

def resetP(request):
    return render(request,'forgotP.html')
pass

@login_required(login_url='login_user')
def personal(request):
    return render(request,'personal.html')
pass


def company(request):

    if request.user.is_authenticated:
        user =request.user


        companyuserProfile = CompanyProfile.objects.get(companyuser = user)
        print(companyuserProfile)
        eventstatus =[0,1,2,3]
        # eventstatus = (Web3GetCompanyActNumber(companyuserProfile.company_walletId))
        del eventstatus[0]
        print(eventstatus)
        context = {'companyuserProfile': companyuserProfile,'eventstatus':eventstatus}
        print(context)
        # if is_company == True:
        #     print("is company")


        # else:
        #      print("is not company")


    return render(request,'company.html',context)
pass

def createevent(request):
    if request.user.is_authenticated:


        user =request.user
        companyuserProfile = CompanyProfile.objects.get(companyuser = user)
        eventform = EventCreateForm()
        # form = EventCreateForm(instance=event)
        print(companyuserProfile)
        if request.method == 'POST':
            print("save event")
            eventform = EventCreateForm(request.POST,request.FILES)
            for field in eventform:
                print("Field Error:", field.name,  field.errors)
            # form = EventCreateForm(request.POST, instance=event)
            if eventform.is_valid():

                name = request.user.username
                category = eventform.cleaned_data['category']
                print(category)
                eventname = eventform.cleaned_data['eventname']
                print(eventname)
                eventdescription = eventform.cleaned_data['eventdescription']
                print(eventdescription)
                eventticketnumber = eventform.cleaned_data['eventticketnumber']
                print(eventticketnumber)
                eventprice = eventform.cleaned_data['eventprice']
                print(eventprice)
                date_StartTime = eventform.cleaned_data['date_StartTime']
                print(date_StartTime)
                date_EndTime = eventform.cleaned_data['date_EndTime']
                print(date_EndTime)
                event_pic = eventform.cleaned_data['event_pic']
                status = "Not Started"
                # GetEvent =  Events.objects.get(eventname=eventname)
                if not Events.objects.filter(eventname=eventname).exists():
                    event = Events.objects.create(companycreater=companyuserProfile,category = category, eventname=eventname, eventdescription=eventdescription,
                    eventticketnumber = eventticketnumber,eventprice = eventprice,date_StartTime=date_StartTime,date_EndTime = date_EndTime,event_pic = event_pic,status = status)

                    event.save()
                    messages.success(request, 'Event was created for ' + eventname)

                else:
                     messages.info(request, 'Event was existed!!')

                try:

                    p=sql.connect(host='127.0.0.1',user='root',password='Sester890627',database='nftticketplatform')
                    if p.is_connected():

                        # 顯示資料庫版本
                        db_Info = p.get_server_info()
                        print("資料庫版本：", db_Info)

                        pcursor=p.cursor()
                        print("連資料庫成功")
                        GetEvent =  Events.objects.get(eventname=eventname)
                        if GetEvent:
                            GetID =GetEvent.id
                            Getcompanycreater = companyuserProfile.companyuser.username
                            Getcategory = GetEvent.category
                            Geteventname = GetEvent.eventname
                            # Geteventdescription = GetEvent.eventdescription
                            Geteventticketnumber = GetEvent.eventticketnumber
                            Geteventprice = GetEvent.eventprice
                            Getdate_created = GetEvent.date_created
                            Getdate_StartTime = GetEvent.date_StartTime
                            Getdate_EndTime = GetEvent.date_EndTime
                            Getstatus = GetEvent.status
                            # Getevent_pic = GetEvent.event_pic

                            print(GetEvent)
                            print("取得各資料成功")
                            person = "INSERT INTO event SET companyID = (SELECT companyID FROM companyprofile WHERE companyName = %s),eventID=%s,category = %s, eventname=%s,eventticketnumber=%s,eventprice=%s,date_created=%s,date_StartTime=%s,date_EndTime=%s,eventstatus=%s;"

                            val = (Getcompanycreater, GetID, Getcategory,Geteventname,Geteventticketnumber,Geteventprice,Getdate_created,Getdate_StartTime,Getdate_EndTime,Getstatus)
                            pcursor.execute(person,val)
                            p.commit()
                            eventID = "SELECT eventID FROM event WHERE eventname = %s"
                            value =(Geteventname,)
                            print(value)
                            pcursor.execute(eventID,value)
                            eventpk =pcursor.fetchall()

                            eventpk=eventpk[0][0]
                            # cmpWallet = companyuserProfile.company_walletId
                            # print(cmpWallet)
                            # print(Web3SetActivity(str(eventpk),cmpWallet,int(Geteventticketnumber),int(Geteventprice)))
                            # print('活動ID:'+eventID)

                            # Web3SetActivity()
                            messages.success(request,"Successfully Insert the data into event database !!")
                        #     print("Successfully Insert the data into company database !!")
                        else:

                            print("取得資料不成功")

                except Error as e:
                    print("資料庫連接失敗：", e)

                finally:
                    if (p.is_connected()):
                        pcursor.close()
                        p.close()
                        print("資料庫連線已關閉")

            else:
                messages.success(request,  'form is not valid')
                print(eventform.errors)

        # form = EventCreateForm()
        context = {'eventform': eventform}


    return render(request,'createevent.html',context)
pass

def updateevent(request,pk):
    event = Events.objects.get(id=pk)
    # event = Events.objects.filter(id=pk)
    updateeventform = EventCreateForm(instance = event)
    print(updateeventform)
    messages.info(request,"Please select the starting time and ending time again!!")
    print("id值"+str(event.id))

    if request.method =="POST":
        updateeventform=EventCreateForm(request.POST,request.FILES,instance = event)

        if updateeventform.is_valid():
            updateeventform.save()

            try:

                p=sql.connect(host='127.0.0.1',user='root',password='Sester890627',database='nftticketplatform')
                if p.is_connected():

                # 顯示資料庫版本
                    db_Info = p.get_server_info()
                    print("資料庫版本：", db_Info)

                    pcursor=p.cursor()
                    print("連資料庫成功")
                if event:
                    companyuserProfile = CompanyProfile.objects.get(companyuser = request.user)
                    Getcompanycreater = companyuserProfile.companyuser.username
                    Getcategory = event.category
                    Geteventname = event.eventname
                    # Geteventdescription = GetEvent.eventdescription
                    Geteventticketnumber = event.eventticketnumber
                    Geteventprice = event.eventprice
                    Getdate_created = event.date_created
                    Getdate_StartTime = event.date_StartTime
                    Getdate_EndTime = event.date_EndTime
                    Getstatus = event.status
                    GetID =event.id
                    # Getevent_pic = GetEvent.event_pic

                    print(event)
                    print("取得各資料成功")
                    updateevent = "UPDATE event SET category = %s, eventname=%s,eventticketnumber=%s,eventprice=%s,date_created=%s,date_StartTime=%s,date_EndTime=%s,eventstatus=%s WHERE eventID = %s;"

                    val = (Getcategory,Geteventname,Geteventticketnumber,Geteventprice,Getdate_created,Getdate_StartTime,Getdate_EndTime,Getstatus,GetID)
                    pcursor.execute(updateevent,val)
                    p.commit()
                    messages.success(request,"Upadate data from database succesfully")

                    return redirect('companyAsset')

                else:

                    print("取得資料不成功")

            except Error as e:
                    print("資料庫連接失敗：", e)

            finally:
                if (p.is_connected()):
                    pcursor.close()
                    p.close()
                    print("資料庫連線已關閉")

    context={"updateeventform":updateeventform}

    return render(request,'updateevent.html',context)
pass

def deleteevent(request,pk):

    deleteevent = Events.objects.get(id=pk)
    deleteevent.delete()
    messages.info(request,"Delete the data from model succeefully!!")

    try:

        p=sql.connect(host='127.0.0.1',user='root',password='Sester890627',database='nftticketplatform')
        if p.is_connected():

                # 顯示資料庫版本
            db_Info = p.get_server_info()
            print("資料庫版本：", db_Info)

            pcursor=p.cursor()
            print("連資料庫成功")
            if deleteevent:

                Geteventname = deleteevent.eventname
                GetID =deleteevent.id
                    # Getevent_pic = GetEvent.event_pic

                print(deleteevent)
                print("取得各資料成功")

                deleteeevent = "DELETE FROM event WHERE eventID = %s and eventname=%s ;"

                val = (Geteventname,GetID)
                pcursor.execute(deleteeevent,val)
                p.commit()
                messages.success(request,"Delete data from database succesfully")



            else:

                print("取得資料不成功")

    except Error as e:
            print("資料庫連接失敗：", e)

    finally:
            if (p.is_connected()):
                pcursor.close()
                p.close()
                print("資料庫連線已關閉")

    return redirect('companyAsset')
pass

def eventcreatform(request):
    eventform = EventCreateForm()
    context ={'eventform':eventform}


    return render(request,'createevent.html',context)
def exhibition(request):
    exhibitionEvents = Events.objects.filter(category="exhibition",status ="Not Started" or "Ongoing").order_by('date_StartTime')
    print(exhibitionEvents)

    context ={"exhibitionEvents":exhibitionEvents}

    # events = Events.objects.order_by('-price').filter(category='exhibition')
    # page_num = request.GET.get("page")
    # paginator = Paginator(events, 2)
    # try:
    #     events = paginator.page(page_num)
    # except PageNotAnInteger:
    #     events = paginator.page(1)
    # except EmptyPage:
    #     events = paginator.page(paginator.num_pages)
    # context = {
    #     'events': events,

    # }
    return render(request,'exhibition.html',context)
pass
def exhibitionDetail(request,pk):
    # print(eachExhibition.pk)
    eachExhibition = Events.objects.get(id=pk)
    print(eachExhibition.id)
    context = {
        'eachExhibition':eachExhibition

    }
    return render(request,'exhibitionDetail.html',context)

def performance(request):
    performanceEvents = Events.objects.filter(category="Performance",status ="Not Started" or "Ongoing").order_by('date_StartTime')
    print(performanceEvents)
    context ={"exhibitionEvents":performanceEvents}
    return render(request,'show.html',context)
pass
def companyInfowallet(request):
    # if request.user.is_authenticated:
        user = request.user

        cmpwalletID = request.POST['cmpwalletid']

        companyuserProfile = CompanyProfile.objects.get(companyuser = user)
        companyuserProfile.company_walletId =  cmpwalletID
        print(companyuserProfile.company_walletId)
        companyuserProfile.save()  #寫入資料庫

        context={'companyuserProfile':companyuserProfile}
        print(context)
        try:
            p=sql.connect(host='127.0.0.1',user='root',password='Sester890627',database='nftticketplatform')
            if p.is_connected():
                    # 顯示資料庫版本
                db_Info = p.get_server_info()
                print("資料庫版本：", db_Info)
                pcursor=p.cursor()
                print("連資料庫成功")
                cmpusername = companyuserProfile.companyuser.username
                person = "UPDATE companyprofile SET companyWalletAddress = %s WHERE companyName = %s;"

                val = (cmpwalletID,cmpusername)
                pcursor.execute(person,val)
                p.commit()
                messages.success(request,"insert wallet into database succesfully")
                print("insert wallet succesfully")
            else:
                print("連接失敗")


        except Error as e:
                print("資料庫連接失敗：", e)

        finally:
            if (p.is_connected()):
                pcursor.close()
                p.close()
                print("資料庫連線已關閉")
                messages.success(request,  'walletid is updated')

        return  render(request,'company.html',context)


def companyAsset(request):
    user =request.user
    companyuserProfile = CompanyProfile.objects.get(companyuser = user)
    print(companyuserProfile)
    companyAssetEvents = Events.objects.filter(companycreater=companyuserProfile).order_by('date_created')
    print(companyAssetEvents)



    # eventID = "SELECT eventID FROM event WHERE eventname = %s"

    # value =(Geteventname,)
    # print(value)
    # pcursor.execute(eventID,value)
    # eventpk =pcursor.fetchall()

    context ={"companyAssetEvents":companyAssetEvents}

    return  render(request,'companyasset.html',context)

def salesstatus(request):

    return  render(request,'salesstatus.html')

def companyhelpcenter(request):

    return  render(request,'companyhelpcenter.html')







