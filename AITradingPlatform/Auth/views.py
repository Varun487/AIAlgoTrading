from django.shortcuts import render
import json
import sys
from datetime import datetime
from os import environ
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth

from django.contrib import messages
import pandas as pd
import pandas_datareader.data as web
from django.db.models import Max, Min, Sum
from django.http import JsonResponse
from django.utils.timezone import make_aware
from pandas_datareader._utils import RemoteDataError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExampleAuthModel





@api_view(['POST', ])
def login_auth(req):
    req_body = json.loads(req.body)

    res = {'status': 'invalid request, please check the documentation for this request here'}
    # checking validation

    valid_username = 'username' in req_body and type(req_body['username']) == str
    valid_password = 'password' in req_body and type(req_body['password']) == str

    if not valid_username and valid_password:
        return JsonResponse(res)

    username = req_body['username']
    print(username)
    password = req_body['password']
    print(password)
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(req, user)
        res['status'] = "you have successfully logged in"
        return JsonResponse(res)


    else:
        res['status'] = "invalid credentials"
    return JsonResponse(res)
