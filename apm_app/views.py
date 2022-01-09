from django.shortcuts import render
from django.http import HttpResponse

import logging
logger = logging.getLogger('apm-elastic-python-site')


# Create your views here.

def home(request):
    return render(request, 'apm_app/home.html')

def ZeroDivisionError(request):
    x = "1/0"
    try:
        exec(x)
    except ZeroDivisionError:
        logger.error(
            'Invalid Equation',
            exc_info=True
        )
        
