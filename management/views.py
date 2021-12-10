from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import clockIn, clockOut
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ClockInForm, ClockOutForm


# Create your ``views here.

class UserDetailPage(View):
    template = "management/user_detail_page.html"
    User = get_user_model()

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('username')
        user = get_object_or_404(self.User, username=slug)
        return user

    def get_query_set(self, *args, **kwargs):
        teacher = self.get_object()
        clock_ins = clockIn.objects.filter(teacher=teacher).order_by('created')
        return clock_ins

    def get(self, request, *args, **kwargs):
        page_number = self.request.GET.get('page')
        query = self.get_query_set()
        paginator = Paginator(query, 10)
        try:
            clock_ins = paginator.get_page(query)
        except PageNotAnInteger:
            clock_ins = paginator.page(1)
        except EmptyPage:
            clock_ins = paginator.page(paginator.num_pages)
        context = {
            'clock_in': clock_ins,
            'paginator': paginator

        }
        #first = clock_ins.object_list[0]
        #print(type(first.created))
        return render(request, self.template, context)


class ClockinDetail(View):
    template = 'management/clock_in_detail.html'

    def get_queryset(self, *args, **kwargs):
        clock_in = self.get_object()
        clock_out = clockOut.objects.filter(clock_in = clock_in)
        return clock_out

    def get_object(self, *args, **kwargs):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        date = self.kwargs.get('date')
        hours = self.kwargs.get('hour')
        minutes = self.kwargs.get('minute')
        seconds = self.kwargs.get('second')
        date_time = datetime.datetime(year=year, month=month, day=date, hour=hours, minute=minutes, second=seconds)
        clock_in = get_object_or_404(clockIn, created=date_time)
        return clock_in
        
    def get(self, request, *args, **kwargs):
        form = ClockOutForm()
        context ={
            'clock_in': self.get_object(),
            'form' : form,
            'clock_out': self.get_queryset()
        }
        return render(self.request, self.template, context)

    def post(self, request, *args, **kwargs):
        form = ClockOutForm(data=request.POST)
        if form.is_valid():
            clock_out = form.save(commit=False)
            clock_out.clock_in = self.get_object()
            clock_out.save()
            return HttpResponseRedirect(reverse('userdetail', kwargs={'username': self.request.user.username}))    
        
        return render(self.request, self.template)


class ClockInCreatePage(View):
    template = 'management/clockincreatepage.html'

    def get_object(self, *args, **kwargs):
        user = self.request.user
        return user 

    def get(self, *args, **kwargs ):
        form = ClockInForm()
        context = {
            'form': form
        }
        return render(self.request, self.template, context)

    def post(self, *args, **kwargs):
        form = ClockInForm(data=self.request.POST)
        context={
            form: 'form'
        }
        if form.is_valid():
            new_clock = form.save(commit=False)
            new_clock.teacher = self.get_object()
            new_clock.save()
            return HttpResponseRedirect(reverse('userdetail', kwargs={'username': self.request.user.username}))
        return render(self.request, self.template, context)

 