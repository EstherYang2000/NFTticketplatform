from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
import mysql.connector as sql
from mysql.connector import Error
from authentication.models import CompanyProfile,CustomerProfile,Events
# Create your views here.




