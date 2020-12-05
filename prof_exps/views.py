from django.shortcuts import render, get_object_or_404
from .models import Prof_Exp

def home(request): 
    prof_exps = Prof_Exp.objects
    return render(request, 'prof_exps/home.html', {'prof_exps' : prof_exps})

def prof_exp_detail(request): 
    prof_exp_detail = Prof_Exp.objects
    return render(request, 'prof_exps/prof_exp_detail.html', {'prof_exps': prof_exp_detail})     