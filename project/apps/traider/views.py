from datetime import date, timedelta
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy

from traider.binance import *
from traider.models import Coin, Traid, Candidate, Balance
from traider.forms import ScanForm, TraidForm, EntryReasonFormSet
from django.contrib.auth.decorators import login_required

import os
import time
# pip install python-dotenv
from dotenv import load_dotenv

# needs to delete traid.attached_file from os
from django.conf import settings

# for Querysets
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def is_valid_queryparam(param):
    return param != '' and param is not None


def index(request):
    today = date.today()
    traids = Traid.objects.all().order_by('-date','-time')
    traids_count = traids.count()

    # Calculate avarage percent for lost traids
    # And lost sum
    if traids.filter(result__lte=0):
        lost_traids = traids.filter(result__lte=0)
        avg_loss_perc = '{:.3f}'.format(
            sum([i.result_percent for i in lost_traids]) \
            / lost_traids.count()
        )
        lost_sum = sum([i.result for i in lost_traids])
    else:
        lost_traids = None
        avg_loss_perc = 0
        lost_sum = 0

    # Calculate avarage percent for profitable traids
    # And profit sum
    if traids.filter(result__gte=0):
        profitable_traids = traids.filter(result__gte=0)
        avg_profit_perc = '{:.3f}'.format(
            sum([i.result_percent for i in profitable_traids]) \
            / profitable_traids.count()
        )
        profit_sum = sum([i.result for i in profitable_traids])
    else:
        profitable_traids = None
        avg_profit_perc = 0
        profit_sum = 0

    # Calculate avarage stop-loss
    if traids:
        avg_stop_loss = '{:.3f}'.format(
            sum([i.stoploss_percent for i in traids]) \
            / traids.count()
        )
    else:
        traids = None
        avg_stop_loss = 0

    candidates = Candidate.objects.all().order_by('symbol')
    balances = Balance.objects.all()[:3]

    # Calculate global result
    # global_result = lost_sum + profit_sum
    global_result = sum([i.result for i in traids.all()])

    # Calculate winrate
    winrate = '{:.1f}'.format(traids.filter(result__gte=0).count()\
                              / traids_count * 100)

    # Calculate today result
    traids_today = Traid.objects.filter(date=today)
    traids_count_today = traids_today.count()
    result_today = sum([i.result for i in traids_today.all()])

    # Calculate traid results for every n days
    earnings = []
    earning_days = []
    # The size of each step in days
    day_delta = timedelta(days=1)
    start_date = date.today() - timedelta(days = 60)
    end_date = date.today() + timedelta(days = 1)
    for n in range((end_date - start_date).days):
        day = start_date + timedelta(n)
        day_earning = int(sum([i.result for i in Traid.objects.filter(date=day)]))
        if day_earning !=0:
            earnings.append(day_earning)
            earning_days.append(str(day.strftime("%d.%m")))

    # Set pagination
    per_page = 20
    page = request.GET.get('page', 1)
    paginator = Paginator(traids, per_page)
    traids = paginator.get_page(page)

    try:
        page = abs(int(page)) or 1
    except ValueError:
        page = 1

    try:
        page = paginator.page(page)
    except (EmptyPage):
        page = paginator.page(paginator.num_pages)


    # CONSOLIDATION AND BREAKING PATTERNS DETECTION
    form = ScanForm(data=request.GET or None)

    if form.is_valid():
        scan(form.data['timeframe'])

        return redirect("/")


    context = {
        'today': today,
        'traids': traids,
        'traids_count': traids_count,
        'lost_traids': lost_traids,
        'lost_sum': lost_sum,
        'global_result': global_result,
        'winrate': winrate,
        'profitable_traids': profitable_traids,
        'profit_sum': profit_sum,
        'avg_loss_perc': avg_loss_perc,
        'avg_profit_perc': avg_profit_perc,
        'avg_stop_loss': avg_stop_loss,
        'page_item': page,
        'form': form,
        'candidates': candidates,
        'balances': balances,
        'earnings_graf': {
            'lables': earning_days,
            'data': earnings,
        },
        'traids_count_today': traids_count_today,
        'result_today': result_today,
#        'consolidating_status': consolidating_status,
#        'breaking_out_status': breaking_out_status,
    }

    return render(request, 'traider/index.html', context)


def remove_candidates(request):
    Candidate.objects.all().delete()
    return redirect("/")


def statistic(request):
    screenshots = Screenshot.objects.all().distinct().order_by('-traid__result_percent')[:3]

    traids = Traid.objects.all()
    traids_count = traids.count()
    winrate = '{:.1f}'.format(traids.filter(result__gte=0).count()\
                              / traids_count * 100)

    # Calculate global result
    # global_result = lost_sum + profit_sum
    global_result = sum([i.result for i in traids.all()])

    # Calculate profit record
    profit_record = Traid.objects.all().order_by('-result')[0]
    profit_percent_record = Traid.objects.all().order_by('-result_percent')[0]

    # Calculate loss record
    try:
        loss_record = Traid.objects.filter(result__lte=0).order_by('result')[0]
    except:
        loss_record = False

    try:
        loss_percent_record = Traid.objects.filter(result__lte=0).order_by('result_percent')[0]
    except:
        loss_percent_record = False

    # Calculate avarage percent for lost traids
    if traids.filter(result__lte=0):
        lost_traids = traids.filter(result__lte=0)
        avg_loss_perc = '{:.3f}'.format(
            sum([i.result_percent for i in lost_traids]) \
            / lost_traids.count()
        )
        lost_sum = sum([i.result for i in lost_traids])
    else:
        lost_traids = None
        avg_loss_perc = 0
        lost_sum = 0

    # Calculate avarage percent for profitable traids
    if traids.filter(result__gte=0):
        profitable_traids = traids.filter(result__gte=0)
        avg_profit_perc = '{:.3f}'.format(
            sum([i.result_percent for i in profitable_traids]) \
            / profitable_traids.count()
        )
        profit_sum = sum([i.result for i in profitable_traids])
    else:
        profitable_traids = None
        avg_profit_perc = 0
        profit_sum = 0

    # Calculate avarage stop-loss
    if traids:
        avg_stop_loss = '{:.3f}'.format(
            sum([i.stoploss_percent for i in traids]) \
            / traids.count()
        )
    else:
        traids = None
        avg_stop_loss = 0

    template = 'traider/statistic.html'
    context = {
        'traids_count': traids_count,
        'global_result': global_result,
        'winrate': winrate,
        'profit_record': profit_record,
        'profit_percent_record': profit_percent_record,
        'loss_record': loss_record,
        'loss_percent_record': loss_percent_record,
        'avg_profit_perc': avg_profit_perc,
        'avg_loss_perc': avg_loss_perc,
        'avg_stop_loss': avg_stop_loss,
        'screenshots': screenshots,
    }
    return render(request, template, context)


def traid(request, id):
    traid = Traid.objects.get(id=id)

    template = 'traider/traid.html'
    context = {
        'traid': traid,
    }
    return render(request, template, context)


def traid_add(request):
    form = TraidForm(request.POST or None)
    formset = EntryReasonFormSet(request.POST or None, instance=form.instance)

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect("/")

    template = 'traider/traid-add.html'

    context = {
        'form': form,
        'formset': formset,
    }

    return render(request, template, context)


def traid_update(request, id):
    traid = Traid.objects.get(id=id)
    form = TraidForm(request.POST, instance=traid)
    formset = EntryReasonFormSet(request.POST or None, instance=form.instance)

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        return redirect("/%d" % traid.id)
    else:
        form = TraidForm(instance=traid)
        formset = EntryReasonFormSet(request.POST or None, instance=form.instance)


    template = 'traider/traid-update.html'

    context = {
        'traid': traid,
        'form': form,
        'formset': formset,
    }

    return render(request, template, context)


def traid_del(request, id):
    traid = Traid.objects.get(id=id)

    if request.method == 'POST':
        os.remove('%s/%s' % (settings.MEDIA_ROOT, traid.attached_file))
        traid.delete()
        return redirect('/')

    template = "traider/traid-del.html"
    context = {
        'traid': traid,
    }
    return render(request, template, context)


def balances(request):
    balances = Balance.objects.all()

    template = "traider/balances.html"
    context = {
        'balances': balances,
    }
    return render(request, template, context)
