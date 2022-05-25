from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product,Mobile

from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.views.decorators.csrf import csrf_exempt

import logging
import json


# Create your views here.

# home() - take request argument
# return what the user wants to see
# views always return a httpresponse or an exception

# function based view
def home(request):
    context = {
        'mobiles': Mobile.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'product/home.html', context)


# class based view
class ProductListView(ListView):
    model = Mobile
    template_name = 'product/home.html'  # look for 'blog/post_list.html' <app>/<model>_<viewtype>.html bydefuault
    context_object_name = 'mobiles'
    #ordering = ['-date_posted']  # order by newest at the top
    # ordering = ['date_posted']


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

    # expect blog/post_detail.html
    # in detailed view the context will be passed as object

