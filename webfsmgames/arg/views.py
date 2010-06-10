# encoding: utf-8
"""ARG!"""
import pycassa
from django.shortcuts import render_to_response
from webfsmgames.arg.models import *



def index(request):
    client = pycassa.connect(['10.0.1.82:9160'])
    keyspace = 'HOPE2008'
    usersFamily = pycassa.ColumnFamily(client, keyspace, 'Users',super=True)
    users = usersFamily.get_range()
    
    return render_to_response("arg/index.html", {"users": users})