from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
import re

from numpy import mod
from .forms import PlotForm
from .utils import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PlotForm(data=request.POST)
        if form.is_valid():
            amin = int(request.POST['amin'])
            amax = int(request.POST['amax'])
            bmin = int(request.POST['bmin'])
            bmax = int(request.POST['bmax'])
            cmin = int(request.POST['cmin'])
            cmax = int(request.POST['cmax'])
            dmin = int(request.POST['dmin'])
            dmax = int(request.POST['dmax'])
            emin = int(request.POST['emin'])
            emax = int(request.POST['emax'])
            smin = int(request.POST['smin'])
            smax = int(request.POST['smax'])
            z = float(request.POST['z'])
            df_random = generate_random_df(amin, amax, bmin, bmax, cmin, cmax, dmin, dmax, emin, emax, smin, smax)
            #print(df_random)
            df = generate_r(df_random)
            print(df)
            
            p99 = percentile_99(df['R'])
            p90 = percentile_90(df['R'])
            p50 = percentile_50(df['R'])
            p10 = percentile_10(df['R'])
            # mode = df_mode(df['R'])
            mean = df_mean(df['R'])
            median = df_median(df['R'])
            # histogram = plt.hist(df['R'], bins=10, alpha=0.8)
            # plt.savefig('/home/agus/Codigo/Django/Xoxo/statistics/montecarlo/plot/static/histogram/histogram.png')
            histogram = plot_histogram(df['R'])
            plt.savefig('/home/agus/Codigo/Django/Xoxo/statistics/montecarlo/plot/static/histogram/histogram.png')
            
            
            context = {
                'results': {
                    'p99': p99,
                    'p90': p90,
                    'p50': p50,
                    'p10': p10,
                    'mean': mean,
                    'median': median,
                    'histogram': histogram
                }
            }
          
            return render(request, "plot/form.html", context)
    else:
        form = PlotForm()
    return render(request,"plot/form.html", {'form': form})


def operations(request):
    path = str(request.get_full_path)
    values = re.split('&', path)
    for v in values:
        print(v)
    return render(request, "plot/background.html")

"""
    if request.method == 'GET':
        print(request.method)
        print(request.GET.get('amin', None))
        
        amin = request.GET.get('amin', None)
        amax = request.GET.get('amax', None)
        bmin = request.GET.get('bmin', None)
        bmax = request.GET.get('bmax', None)
        cmin = request.GET.get('cmin', None)
        cmax = request.GET.get('cmax', None)
        dmin = request.GET.get('dmin', None)
        dmax = request.GET.get('dmax', None)
        emin = request.GET.get('emin', None)
        emax = request.GET.get('emax', None)
        smin = request.GET.get('smin', None)
        smax = request.GET.get('smax', None)
        z = request.GET.get('z', None)
        
        context = {
            'amin': amin,
            'amax': amax,
            'bmin': bmin,
            'bmax': bmax,
            'cmin': cmin,
            'cmax': cmax,
            'dmin': dmin,
            'dmax': dmax,
            'emin': emin,
            'emax': emax,
            'smin': smin,
            'smax': smax,
            'z': z
        }
        return render(request,"plot/form.html", context)
"""