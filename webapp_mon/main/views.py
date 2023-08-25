import os
import mysql.connector

from django.shortcuts import render
from .models import get_professors
#from django.http import HttpResponse
from django.db import connection
# Create your views here.

# Acceder a los secretos desde las variables de entorno
host = os.getenv('DATABASE_HOST')
usuario = os.getenv('DATABASE_USER')
database = os.getenv('DATABASE_NAME')

def index(response):
    return render(response, "main/base.html", {})


def home(response):
    return render(response, "main/login.html", {})


def llamar_procedimiento(request):
    cursor = connection.cursor()
    cursor.execute("CALL registrodb.getUniversity();")
    results = cursor.fetchall()
    return render(request, "main/consulta1.html", {'get_professors': results})