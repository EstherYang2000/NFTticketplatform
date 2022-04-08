from asyncio import events
from decimal import Decimal
import json
import locale
from ether import getEtherRate, getUSDTW
from .decorators import unauthenticated_user
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.dispatch import receiver
from hexbytes import HexBytes as hb
import datetime
import email
from http.client import HTTPResponse
from multiprocessing import Event
from unicodedata import category, decimal
from django.shortcuts import redirect, render
from django.contrib import messages
from operator import itemgetter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .form import RegistrationForm, EventCreateForm, CustomerProfileForm, OrderForm
from django.contrib.auth.decorators import login_required
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
from authentication.models import CompanyProfile, CustomerProfile, Events, Order, Transfer
UserModel = get_user_model()
#Smart Contract
from DjangoBackend import *
import sys
sys.path.append("..")

from web3 import Web3, HTTPProvider

from sq import *

# Create your views here.
# @login_required(login_url='login_user')


# --------------------------------------------authentication-----------------------------------

def login_user(request):
    try:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method == "POST":
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request, 'Username OR password is incorrect')
            context = {}
            return render(request, 'signIn.html', context)
    except Exception as e:
        print(e)


pass

Pn = " "
Pem = " "
Ppw1 = " "
Pw2 = " "
Pst = False


def register(request):
    global Pn, Pem, Ppw1, Pw2, Pst
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

                print(is_staff)

                try:

                    p = sql.connect(host=changehost, user=changeuser,
                                        password=changepassword, database='nftticketwebsite')
                    if p.is_connected():

                        # 顯示資料庫版本
                        db_Info = p.get_server_info()
                        print("資料庫版本：", db_Info)

                        pcursor = p.cursor()
                        print("連資料庫成功")

                        d = request.POST
                        print("取得資料成功")
                        for key, value in d.items():
                            if key == 'username':
                                Pn = value
                            elif key == 'email':
                                Pem = value
                            elif key == 'password1':
                                Ppw1 = value
                            elif key == 'password2':
                                Ppw2 = value
                            else:
                                Pst = value
                                print(Pst)
                        print("取得各資料成功")
                        if (Ppw1 == Ppw2):
                            print("密碼符合")
                            if is_staff == True:
                                print("公司註冊")

                                companyuser = CompanyProfile.objects.create(
                                    companyuser=user, company_email=user.email)
                                # CompanyProfile.objects.create(user)
                                # name=user.objects.get(username=),
                                # companyuserID =companyuser.company_id
                                print("公司註冊完成")
                                person = "INSERT INTO companyprofile (companyName, companyEmail,companyPassword) VALUES (%s, %s,%s)"
                                val = (Pn, Pem, Ppw1)
                                pcursor.execute(person, val)
                                p.commit()

                                messages.success(
                                    request, "Successfully Insert the data into company database !!")
                                print(
                                    "Successfully Insert the data into company database !!")

                            elif is_staff == False:
                                print("顧客註冊")
                                customeruser = CustomerProfile.objects.create(
                                    customeruser=user, personal_email=user.email)
                                print("公司註冊完成")
                                # customeruserID = customeruser.Customer_id
                                person = "INSERT INTO customerprofile (CustomerName, CustomerEmail,CustomerPassword) VALUES (%s, %s,%s)"
                                val = (Pn, Pem, Ppw1)
                                pcursor.execute(person, val)
                                p.commit()
                                messages.success(
                                    request, "Successfully Insert the data into customer database !!")
                                print(
                                    "Successfully Insert the data into customer database !!")

                        else:
                            print("密碼錯誤")
                            messages.success(request, "Check your password!!")
                except Error as e:
                    print("資料庫連接失敗：", e)

                finally:
                    if (p.is_connected()):
                        pcursor.close()
                        p.close()
                        print("資料庫連線已關閉")
                messages.success(
                    request, 'Account was created for ' + user.username)
                return redirect('login_user')
        context = {'form': form}
        return render(request, 'signup.html', context)


pass


def signout_user(request):
    logout(request)
    # messages.success(request,("You were logged out!!"))
    return redirect('home')


pass


def resetP(request):
    return render(request, 'forgotP.html')


pass


#搜尋活動
def searchEvent(request):
    print("search!!!!")
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            exhibitionEvents = Events.objects.filter(
                eventname__icontains=query)
            page_num = request.GET.get("page")
            paginator = Paginator(exhibitionEvents, 3)
            try:
                exhibitionEvents = paginator.page(page_num)
            except PageNotAnInteger:
                exhibitionEvents = paginator.page(1)
            except EmptyPage:
                exhibitionEvents = paginator.page(paginator.num_pages)
            messages.success(request, "Search successfully!!")
            return render(request, 'searchEvent.html', {'exhibitionEvents': exhibitionEvents})
        else:
            print("No information to show")
    return render(request, 'searchEvent.html', {})


pass

# -----------------------------------------------Personal--------------------------------------------

#顯示個人資訊
@login_required(login_url='login_user')
def personal(request):
    if request.user.is_authenticated:
        user = request.user

        customerProfile = CustomerProfile.objects.get(customeruser=user)

        print(customerProfile)
        customerProfile = CustomerProfile.objects.get(customeruser=user)

        updatecustomerform = CustomerProfileForm(instance=customerProfile)
        print('列印updatecustomerform')
        print(updatecustomerform)
        context = {'customerProfile': customerProfile,
                   'updatecustomerform': updatecustomerform}
        print(context)

    return render(request, 'personal/personalInfo.html', context)


pass

#顯示照片
def personalAvatar(request):
    user = request.user

    customerProfile = CustomerProfile.objects.get(customeruser=user)

    context = {'customerProfile': customerProfile}

    return render(request, 'personal/personal.html', context)


pass

#個人錢包和照片
def personalInfowallet(request):
    user = request.user
    customerProfile = CustomerProfile.objects.get(customeruser=user)

    updatecustomerform = CustomerProfileForm(instance=customerProfile)
    print('列印updatecustomerform')
    # print(updatecustomerform)

    if request.method == "POST":
        updatecustomerform = CustomerProfileForm(
            request.POST, request.FILES, instance=customerProfile)
        if updatecustomerform.is_valid():
            updatecustomerform.save()

            personalwalletID = updatecustomerform.cleaned_data['personal_walletId']
            personalavatar = updatecustomerform.cleaned_data['avatars']
            print("------------------------------------------------------------------------------------------------------------------------")
            print("personalwalletID:"+str(personalwalletID))
            print("personalavatar"+str(personalavatar))
            # personalwalletID = request.method.GET['peronsalwallet']
            # personalavatar = request.method.GET['peronsalavatar']

            customerProfile.personal_walletId = personalwalletID
            customerProfile.avatars = personalavatar
            print(customerProfile.personal_walletId)
            customerProfile.save()  # 寫入資料庫

        try:
            p = sql.connect(host=changehost, user=changeuser,
                                        password=changepassword, database='nftticketwebsite')
            if p.is_connected():
                # 顯示資料庫版本
                db_Info = p.get_server_info()
                print("資料庫版本：", db_Info)
                pcursor = p.cursor()
                print("連資料庫成功")
                cususername = customerProfile.customeruser.username
                cususerwallet = customerProfile.personal_walletId
                person = "UPDATE customerprofile SET CustomerWalletAdress = %s WHERE CustomerName = %s;"
                val = (cususerwallet, cususername)
                pcursor.execute(person, val)
                p.commit()
                messages.success(
                    request, "insert wallet into database succesfully")
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
    context = {'customerProfile': customerProfile,
               'updatecustomerform': updatecustomerform}
    print(context)
    return render(request, 'personal/personalInfo.html', context)


pass



# 待修改

#個人資產
@login_required(login_url='login_user')
def personalasset(request):
    user = request.user

    customerProfile = CustomerProfile.objects.get(customeruser=user)

# 個人錢包換算
    # get asset
    # myAssertEther = 0.00
    # totalAsset = Decimal(myAssertEther)
    CustomerOrders =[]
    customerOrders = Order.objects.filter(customer=customerProfile)
    myOrders = customerOrders.all()
    # for myOrder in myOrders:
    #     totalPerCost=myOrder[(CustomerOrders[myOrder.events.eventname])]
    #     totalPerCosts =Decimal (totalPerCost)
    #     thisprice = myOrder.orderPrice
    #     thispriceA = Decimal(thisprice)
    #     totalPerCosts+= thispriceA

    # print(CustomerOrders)
    print("_________________________________________________")
    print(customerOrders)
    # etherAsset = {}
    # for myOrder in myOrders:
    #     assetA = Decimal(myOrder.orderPrice)
    #     totalAsset += assetA
    # etherAsset['totalAsset'] = totalAsset
    # print("totalAsset"+str(totalAsset))
    etherAsset = {}
    totaltokennum = Web3balanceOf(customerProfile.personal_walletId)[1]
    totalAsset = Web3GetCustomer(customerProfile.personal_walletId)["TotalCostInSmartContract"]
    print(totalAsset)
    print(type(totalAsset))
    totalAssetD = Decimal(totalAsset)
    lastEtherRate = getEtherRate()

    # Convert to USD
    lastEtherRate = Decimal(lastEtherRate)
    etherToUSD = totalAssetD * lastEtherRate
    print("etherToUSD:"+str(etherToUSD))
    etherToUSD = Decimal(etherToUSD)
    # Convert to TW
    lastUSDTWRate = getUSDTW()
    lastUSDTWRate = Decimal(lastUSDTWRate)
    etherToTWD = etherToUSD*lastUSDTWRate

    locale.setlocale(locale.LC_ALL, '')
    etherToUSD = locale.currency(etherToUSD, grouping=True)
    etherAsset['etherToUSD'] = etherToUSD
    etherToTWD = locale.currency(etherToTWD, grouping=True)
    print("etherToTWD"+str(etherToTWD))
    etherAsset['etherToTWD'] = etherToTWD

    # NFT Chart

    # 訂購資料
    # myOrdersCount = myOrders.count()

    # TransferData
    context = {'myOrders': myOrders, 'customerProfile': customerProfile,
               'totaltokennum': totaltokennum, 'etherAsset': etherAsset,'totalAsset':totalAsset}

    return render(request, 'personal/personalasset.html', context)


pass

# transferFee待補
#個人轉讓中心
@login_required(login_url='login_user')
def personaltransfer(request):
    user = request.user
    customerProfile = CustomerProfile.objects.get(customeruser=user)
    Sender = CustomerProfile.objects.get(customeruser=user)
    customerOrders = Order.objects.filter(customer=customerProfile)
    myAssets = customerOrders.all()

# form
    if request.method == "POST":
        senderName = request.POST.get('s4-sender-username')
        senderWallletID = request.POST.get('s4-sender-wid')
        transferEvent = request.POST.get('s4-sender-itemNum')
        senderNote = request.POST.get('s4-sender-notes')
        receiverWalletID = request.POST.get('s4-recei-wid')
        receiverNote = request.POST.get('s4-recei-notes')

        Receiver = CustomerProfile.objects.filter(
            personal_walletId=receiverWalletID)
        thisevent = Events.objects.filter(eventname=transferEvent)
        # print("----------------------------------------------------------------------")
        # thissenderorder = Order.objects.filter(customer=customerProfile, events=thisevent)

        # print(thissenderorder)
                # firstSenderorder =senderorder[0]
        # mysenderOrder= Order.objects.filter(customer=Sender, events=thisevent)
        # mysenderOrders=mysenderOrder.all()
        # mysenderOrderCount = mysenderOrders.objects.count()
        mysenderOrderCount=Order.objects.filter(customer=customerProfile, events=thisevent).count()
        # mysenderOrderCount= Order.objects.filter(customer__in=Sender, events__in=thisevent).count()
        # print("mysenderOrderCount"+str(mysenderOrderCount)+"-------------------------------")
        # mysenderOrder=senderOrders.all()
        # mysenderOrderCount = mysenderOrder.count()
        # transferFee
        # status = "UnConfirmed"
        # if (mysenderOrderCount>0):
        #     wantToTransfer = Transfer.objects.create(Sender=customerProfile, Receiver=Receiver, senderOrder=senderorder,
        #                                              tranferEvent=thisevent, transferFee=0, status=status, senderNote=senderNote, receiverNote=receiverNote)
        #     wantToTransfer.save()
        #     wantToTransferID = wantToTransferID.id
        #     messages.success(request, "'TransferEvent was created for ' + customerProfile.customeruser.username＋'Status:' + wantToTransfer.status")
        #     try:

        #         p = sql.connect(host=changehost, user=changeuser,
                                        #password=changepassword, database='nftticketwebsite')
        #         if p.is_connected():
        #             # 顯示資料庫版本
        #             db_Info = p.get_server_info()
        #             print("資料庫版本：", db_Info)
        #             pcursor = p.cursor()
        #             print("連資料庫成功")
        #             getTransfer = Transfer.objects.get(id=wantToTransferID)
        #             if getTransfer:
        #                 getTransferID = getTransfer.id
        #                 getSenderWallet = customerProfile.personal_walletId
        #                 getReceiverWallet = getTransfer.Receiver.personal_walletId
        #                 getTokenID = getTransfer.senderorder.tokenID
        #                 getEventID = getTransfer.tranferEvent.id
        #                 getTransferfee = getTransfer.transferFee
        #                 getTransferDate_created = getTransfer.transferDate_created
        #                 getTransferDate_Success = getTransfer.transferDate_Success
        #                 status = getTransfer.status

        #                 print(getTransfer)
        #                 print("取得各資料成功")
        #                 transferticket = "INSERT INTO transferticket SET transferID =%s,senderID = (SELECT CustomerID FROM customerprofile WHERE CustomerWalletAdress = %s),\
        #                         receiverID = (SELECT CustomerID FROM customerprofile WHERE CustomerWalletAdress = %s),tokenID = %s, transferEventID=%s,transferFee=%s,transferDate_created=%s,\
        #                             transferDate_Success=%s,status=%s;"

        #                 val = (getTransferID, getSenderWallet, getReceiverWallet, getTokenID, getEventID,
        #                        getTransferfee, getTransferDate_created, getTransferDate_Success, status)
        #                 pcursor.execute(transferticket, val)
        #                 p.commit()
        #                 # eventID = "SELECT eventID FROM event WHERE eventname = %s"
        #                 # value = (Geteventname,)
        #                 # print(value)
        #                 # pcursor.execute(eventID, value)
        #                 # eventpk = pcursor.fetchall()

        #                 # eventpk = eventpk[0][0]
        #                 # cmpWallet = companyuserProfile.company_walletId
        #                 # print(cmpWallet)
        #                 # print(Web3SetActivity(str(eventpk),cmpWallet,int(Geteventticketnumber),int(Geteventprice)))
        #                 # print('活動ID:'+eventID)

        #                 # Web3SetActivity()
        #                 messages.success(
        #                     request, "Successfully Insert the data into transferticket database !!")
        #                 return redirect('personaltransfer')
        #             #     print("Successfully Insert the data into company database !!")
        #             else:

        #                 print("取得資料不成功")
        #                 return redirect('personaltransfer')
        #     except Error as e:
        #         print("資料庫連接失敗：", e)
        #         return redirect('personaltransfer')

        #     finally:
        #         if (p.is_connected()):
        #             pcursor.close()
        #             p.close()
        #             print("資料庫連線已關閉")
        # else:
        #     messages.info(request, 'TransferEvent was not invalid !!')
        #     return redirect('personaltransfer')

    context = {'customerProfile': customerProfile, 'myAssets': myAssets}
    return render(request, 'personal/personaltransfer.html', context)


pass

#個人服務中心
@login_required(login_url='login_user')
def personalhelp(request):
    user = request.user

    customerProfile = CustomerProfile.objects.get(customeruser=user)

    context = {'customerProfile': customerProfile}
    return render(request, 'personal/personalhelp.html', context)


pass


# 剩連接 TOKENORDER
#購買活動
def exhibitionOrder(request, pk):

    eachExhibition = Events.objects.get(id=pk)
    customerProfile = CustomerProfile.objects.get(
        customeruser=request.user)
    print("--------------------------------------------------------------------")

    # print(exhibitionOrderForm)
    # messages.info(
    #     request, "Please confirm and fill the eventorderform again!!")
    print("id值"+str(eachExhibition.id))
    print(customerProfile)
    orderfee = {}
    orderprice = eachExhibition.eventprice

    print(orderprice)
    if request.method == "POST":

        print("-------------------------orderfee-------------------------")
        # orderNumber = request.POST.get('ticket_num')
        # print('orderNumber'+str(orderNumber))
        # orderPrice = request.POST.get('ticket_cost')
        # print('orderPrice'+str(orderPrice))
        # orderHandlingfee = request.POST.get('fee')
        # print('orderHandlingfee'+str(orderHandlingfee))
        # orderTotalPrice = request.POST.get('total_cost')
        # print('orderTotalPrice'+str(orderTotalPrice))
        orderNumber = 1
        print('orderNumber'+str(orderNumber))
        orderPrice = format(eachExhibition.eventprice, '0.2f')
        print('orderPrice'+str(orderPrice))
        a = Decimal(orderPrice)
        orderHandlingfee = (a*3/100)
        print('orderHandlingfee'+str(orderHandlingfee))
        orderTotalPrice = (a*103/100)
        print('orderTotalPrice'+str(orderTotalPrice))

        GetEvent = Events.objects.get(eventname=eachExhibition.eventname)
        remainticket = eachExhibition.remainedTicketNum
        if(remainticket >= orderNumber):
            # 取TOKEID
            # tokenID =
            orderlist = Web3safeMint(str(eachExhibition.id),customerProfile.personal_walletId,customerProfile.personal_walletId,float(eachExhibition.eventprice))
            print(orderlist)
            tokenID = orderlist[1]
            print(tokenID)
            thisOrder = Order.objects.create(customer=customerProfile, events=GetEvent, orderNumber=orderNumber, orderPrice=orderPrice, tokenID = tokenID,
                                             orderHandlingfee=orderHandlingfee, orderTotalPrice=orderTotalPrice)
            thisOrder.save()

            OrderID = thisOrder.id
            messages.success(
                request,  'Order was created for ' + str(customerProfile.customeruser.username))
            eachExhibition.totalorderedTicket += orderNumber
            eachExhibition.remainedTicketNum = remainticket-orderNumber
            print("totalorderedTicket:"+str(eachExhibition.totalorderedTicket))
            print("remainedTicketNum:" + str(eachExhibition.remainedTicketNum))
            eachExhibition.save()
            try:

                p = sql.connect(host=changehost, user=changeuser,
                                        password=changepassword, database='nftticketwebsite')
                if p.is_connected():
                    # 顯示資料庫版本
                    db_Info = p.get_server_info()
                    print("資料庫版本：", db_Info)

                    pcursor = p.cursor()
                    print("連資料庫成功")
                    GetOrder = Order.objects.get(
                        id=OrderID, customer=customerProfile)

                    if GetOrder:
                     # 取TOKEID
                        # tokenID =
                        getOrderEventID = GetOrder.id
                        getOrdercustomer = GetOrder.customer
                        getevent = GetOrder.events
                        getOrderNumber = GetOrder.orderNumber
                        getTokenID = GetOrder.tokenID
                        getDate_created = GetOrder.date_created
                        getOrderPrice = GetOrder.orderPrice
                        getOrderHandlingfee = GetOrder.orderHandlingfee
                        getOrderTotalPrice = GetOrder.orderTotalPrice
                        print(GetOrder)
                        print("取得訂購各資料成功")
                        eventorder = "INSERT INTO orderevent SET orderEventID=%s,CustomerID = (SELECT CustomerID FROM customerprofile WHERE CustomerName = %s),\
                            eventID= (SELECT eventID FROM event WHERE eventname = %s),OrderNumber = %s,tokenID=%s,orderDate_created=%s,OrderPrice=%s , OrderHandlingfee=%s ,OrderTotalPrice=%s;"

                        val = (OrderID, getOrdercustomer.customeruser.username, getevent.eventname, getOrderNumber, getTokenID, getDate_created, getOrderPrice,
                               getOrderHandlingfee, getOrderTotalPrice)
                        pcursor.execute(eventorder, val)
                        p.commit()
                        # eventID = "SELECT orderID FROM event WHERE orderEventID = %s"
                        # value = (getOrderEventID)
                        # print(value)
                        # pcursor.execute(eventID, value)
                        # eventpk = pcursor.fetchall()

                        # eventpk = eventpk[0][0]
                        # cmpWallet = companyuserProfile.company_walletId
                        # print(cmpWallet)
                        # print(Web3SetActivity(str(eventpk),cmpWallet,int(Geteventticketnumber),int(Geteventprice)))
                        # print('活動ID:'+eventID)

                        # Web3SetActivity()
                        messages.success(
                            request, "Successfully Insert the data into order database !!")

                        event = "UPDATE event SET totalOrderTicketNum = %s,remainedTicketNum = %s WHERE eventID = %s;"

                        val = (getevent.totalorderedTicket,
                               getevent.remainedTicketNum, getevent.id)
                        pcursor.execute(event, val)
                        p.commit()
                        messages.success(
                            request, "Update the ticket number of event into database succesfully")
                        return redirect('exhibition')
                    else:

                        print("取得資料不成功")

            except Error as e:
                print("資料庫連接失敗：", e)

            finally:
                if (p.is_connected()):
                    pcursor.close()
                    p.close()
                    print("資料庫連線已關閉")
                return redirect('exhibition')
        else:
            messages.warning(request, "No enoungh ticket")
            return redirect('exhibition')

    context = {'customerProfile': customerProfile,
               'eachExhibition': eachExhibition}

    return render(request, 'buyConfirm1.html', context)


pass


# -----------------------------------------------Company---------------------------------------------------------
@login_required(login_url='login_user')
def company(request):

    if request.user.is_authenticated:
        user = request.user

        companyuserProfile = CompanyProfile.objects.get(companyuser=user)
        print(companyuserProfile)
        eventstatus =[]
        eventstatus = (Web3GetCompanyActNumber(companyuserProfile.company_walletId))
        print("------------------------------------")
        print(eventstatus)
        del eventstatus[0]
        print(eventstatus)
        num = [0, 1, 2]
        context = {'companyuserProfile': companyuserProfile,
                   'eventstatus': eventstatus, 'num': num}
        print(context)
        # if is_company == True:
        #     print("is company")

        # else:
        #      print("is not company")

    return render(request, 'company/company.html', context)


pass

#公司新增活動
@login_required(login_url='login_user')
def createevent(request):
    if request.user.is_authenticated:

        user = request.user
        companyuserProfile = CompanyProfile.objects.get(companyuser=user)
        eventform = EventCreateForm()
        # form = EventCreateForm(instance=event)
        print(companyuserProfile)
        if request.method == 'POST':
            print("save event")
            eventform = EventCreateForm(request.POST, request.FILES)
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
                remainedTicketNum = eventticketnumber

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
                    event = Events.objects.create(companycreater=companyuserProfile, category=category, eventname=eventname, eventdescription=eventdescription,
                                                  eventticketnumber=eventticketnumber, remainedTicketNum=eventticketnumber, eventprice=eventprice, date_StartTime=date_StartTime, date_EndTime=date_EndTime, event_pic=event_pic, status=status)

                    event.save()
                    messages.success(
                        request, 'Event was created for ' + eventname)

                    try:

                        p = sql.connect(host=changehost, user=changeuser,
                                        password=changepassword, database='nftticketwebsite')
                        if p.is_connected():

                            # 顯示資料庫版本
                            db_Info = p.get_server_info()
                            print("資料庫版本：", db_Info)

                            pcursor = p.cursor()
                            print("連資料庫成功")
                            GetEvent = Events.objects.get(eventname=eventname)
                            if GetEvent:
                                GetID = GetEvent.id
                                Getcompanycreater = companyuserProfile.companyuser.username
                                Getcategory = GetEvent.category
                                Geteventname = GetEvent.eventname
                                # Geteventdescription = GetEvent.eventdescription
                                Geteventticketnumber = GetEvent.eventticketnumber
                                GeteventRemainedTicketNum = GetEvent.remainedTicketNum
                                GeteventtotalorderedTicket = GetEvent.totalorderedTicket
                                Geteventprice = GetEvent.eventprice
                                Getdate_created = GetEvent.date_created
                                Getdate_StartTime = GetEvent.date_StartTime
                                Getdate_EndTime = GetEvent.date_EndTime
                                Getstatus = GetEvent.status
                                # Getevent_pic = GetEvent.event_pic

                                print(GetEvent)
                                print("取得各資料成功")
                                person = "INSERT INTO event SET companyID = (SELECT companyID FROM companyprofile WHERE companyName = %s),eventID=%s,category = %s, eventname=%s,eventticketnumber=%s,eventprice=%s,date_created=%s,date_StartTime=%s,date_EndTime=%s,eventstatus=%s,totalOrderTicketNum=%s,remainedTicketNum=%s;"

                                val = (Getcompanycreater, GetID, Getcategory, Geteventname, Geteventticketnumber,
                                       Geteventprice, Getdate_created, Getdate_StartTime, Getdate_EndTime, Getstatus, GeteventtotalorderedTicket, GeteventRemainedTicketNum)
                                pcursor.execute(person, val)
                                p.commit()
                                eventID = "SELECT eventID FROM event WHERE eventname = %s"
                                value = (Geteventname,)
                                print(value)
                                pcursor.execute(eventID, value)
                                eventpk = pcursor.fetchall()

                                eventpk = eventpk[0][0]
                                cmpWallet = companyuserProfile.company_walletId
                                print(cmpWallet)
                                print(Web3SetActivity(str(eventpk),cmpWallet,int(Geteventticketnumber),(Geteventprice)))
                                print('活動ID:'+eventID)

                                messages.success(
                                    request, "Successfully Insert the data into event database !!")
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
                    messages.info(request, 'Event was existed!!')

            else:
                messages.success(request,  'form is not valid')
                print(eventform.errors)

        # form = EventCreateForm()
        context = {'eventform': eventform}

    return render(request, 'company/createevent.html', context)


pass

#公司更新活動
@login_required(login_url='login_user')
def updateevent(request, pk):
    event = Events.objects.get(id=pk)
    # event = Events.objects.filter(id=pk)
    updateeventform = EventCreateForm(instance=event)
    print(updateeventform)
    # messages.info(
    #     request, "Please select the starting time and ending time again!!")
    print("id值"+str(event.id))

    if request.method == "POST":
        updateeventform = EventCreateForm(
            request.POST, request.FILES, instance=event)

        if updateeventform.is_valid():
            updateeventform.save()

            try:

                p = sql.connect(host=changehost, user=changeuser,
                                        password=changepassword, database='nftticketwebsite')
                if p.is_connected():

                    # 顯示資料庫版本
                    db_Info = p.get_server_info()
                    print("資料庫版本：", db_Info)

                    pcursor = p.cursor()
                    print("連資料庫成功")
                if event:
                    companyuserProfile = CompanyProfile.objects.get(
                        companyuser=request.user)
                    Getcompanycreater = companyuserProfile.companyuser.username
                    Getcategory = event.category
                    Geteventname = event.eventname
                    # Geteventdescription = GetEvent.eventdescription
                    Geteventticketnumber = event.eventticketnumber
                    GeteventremainedTicketNum = Geteventticketnumber
                    Gettotalorderedticket = event.totalorderedTicket
                    Geteventprice = event.eventprice
                    Getdate_created = event.date_created
                    Getdate_StartTime = event.date_StartTime
                    Getdate_EndTime = event.date_EndTime
                    Getstatus = event.status
                    GetID = event.id
                    # Getevent_pic = GetEvent.event_pic

                    print(event)
                    print("取得各資料成功")
                    updateevent = "UPDATE event SET category = %s, eventname=%s,eventticketnumber=%s,eventprice=%s,\
                    date_created=%s,date_StartTime=%s,date_EndTime=%s,eventstatus=%s ,totalOrderTicketNum=%s, remainedTicketNum =%s WHERE eventID = %s;"

                    val = (Getcategory, Geteventname, Geteventticketnumber, Geteventprice,
                           Getdate_created, Getdate_StartTime, Getdate_EndTime, Getstatus, Gettotalorderedticket,GeteventremainedTicketNum, GetID)
                    pcursor.execute(updateevent, val)
                    p.commit()
                    messages.success(
                        request, "Upadate data from database succesfully")

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

    context = {"updateeventform": updateeventform}

    return render(request, 'company/updateevent.html', context)


pass

#公司刪除活動
def deleteevent(request, pk):

    deleteevent = Events.objects.get(id=pk)
    deleteevent.delete()
    messages.info(request, "Delete the data from model succeefully!!")

    try:

        p = sql.connect(host=changehost, user=changeuser,
                                        password=changepassword, database='nftticketwebsite')
        if p.is_connected():

            # 顯示資料庫版本
            db_Info = p.get_server_info()
            print("資料庫版本：", db_Info)

            pcursor = p.cursor()
            print("連資料庫成功")
            if deleteevent:

                Geteventname = deleteevent.eventname
                GetID = deleteevent.id
                # Getevent_pic = GetEvent.event_pic

                print(deleteevent)
                print("取得各資料成功")

                deleteeevent = "DELETE FROM event WHERE eventID = %s and eventname=%s ;"

                val = (GetID,Geteventname)
                pcursor.execute(deleteeevent, val)
                p.commit()
                messages.success(
                    request, "Delete data from database succesfully")

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

#傳遞createventform
def eventcreatform(request):
    eventform = EventCreateForm()
    context = {'eventform': eventform}

    return render(request, 'company/createevent.html', context)

#新增WalletID
def companyInfowallet(request):
    # if request.user.is_authenticated:
    user = request.user

    cmpwalletID = request.POST['cmpwalletid']

    companyuserProfile = CompanyProfile.objects.get(companyuser=user)
    companyuserProfile.company_walletId = cmpwalletID
    print(companyuserProfile.company_walletId)
    companyuserProfile.save()  # 寫入資料庫

    context = {'companyuserProfile': companyuserProfile}
    print(context)
    try:
        p = sql.connect(host=changehost, user=changeuser,
                                        password=changepassword, database='nftticketwebsite')
        if p.is_connected():
            # 顯示資料庫版本
            db_Info = p.get_server_info()
            print("資料庫版本：", db_Info)
            pcursor = p.cursor()
            print("連資料庫成功")
            cmpusername = companyuserProfile.companyuser.username
            person = "UPDATE companyprofile SET companyWalletAdress = %s WHERE companyName = %s;"

            val = (cmpwalletID, cmpusername)
            pcursor.execute(person, val)
            p.commit()
            messages.success(
                request, "insert wallet into database succesfully")
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

    return render(request, 'company/company.html', context)

# 待修改
#公司資產
def companyAsset(request):
    user = request.user
    companyuserProfile = CompanyProfile.objects.get(companyuser=user)
    print(companyuserProfile)
    companyAssetEvents = Events.objects.filter(
        companycreater=companyuserProfile).order_by('date_created')
    # print(companyAssetEvents)
    page_num = request.GET.get("page")
    paginator = Paginator(companyAssetEvents, 3)
    try:
        companyAssetEvents = paginator.page(page_num)
    except PageNotAnInteger:
        companyAssetEvents = paginator.page(1)
    except EmptyPage:
        companyAssetEvents = paginator.page(paginator.num_pages)

    # eventID = "SELECT eventID FROM event WHERE eventname = %s"

    # value =(Geteventname,)
    # print(value)
    # pcursor.execute(eventID,value)
    # eventpk =pcursor.fetchall()

    context = {"companyAssetEvents": companyAssetEvents}

    return render(request, 'company/companyasset.html', context)


# 待修改
# 公司銷售狀況
def salesstatus(request):
    user = request.user
    companyuserProfile = CompanyProfile.objects.get(companyuser=user)
    print(companyuserProfile)
    companyAssetEvents = Events.objects.filter(
        companycreater=companyuserProfile).order_by('date_created')
    companyAssets = companyAssetEvents.all()
    #Web3GetSellSituation (ActID)
    context = {"companyAssets": companyAssets}

    return render(request, 'company/salesstatus.html', context)

#詢問中心
def companyhelpcenter(request):

    return render(request, 'company/companyhelpcenter.html')
# ----------------------------------------------------ECommerce------------------------------------------------

#展覽頁面
def exhibition(request):
    exhibitionEvents = Events.objects.filter(
        category="exhibition", status="Not Started" or "Ongoing").order_by('date_StartTime')
    page_num = request.GET.get("page")
    paginator = Paginator(exhibitionEvents, 3)
    try:
        exhibitionEvents = paginator.page(page_num)
    except PageNotAnInteger:
        exhibitionEvents = paginator.page(1)
    except EmptyPage:
        exhibitionEvents = paginator.page(paginator.num_pages)

    # print(exhibitionEvents)
    context = {"exhibitionEvents": exhibitionEvents}

    return render(request, 'exhibition.html', context)
pass

#各個展覽細節
def exhibitionDetail(request, pk):
    # print(eachExhibition.pk)
    eachExhibition = Events.objects.get(id=pk)
    print(eachExhibition.id)
    context = {
        'eachExhibition': eachExhibition

    }
    return render(request, 'exhibitionDetail.html', context)
pass


#表演
def performance(request):
    performanceEvents = Events.objects.filter(
        category="Performance", status="Not Started" or "Ongoing").order_by('date_StartTime')
    print(performanceEvents)
    context = {"exhibitionEvents": performanceEvents}
    return render(request, 'show.html', context)

pass

#首頁
def home(request):
    AllShows = Events.objects.all()
    context={"AllShows":AllShows}


    return render(request, 'index.html',context)
pass
