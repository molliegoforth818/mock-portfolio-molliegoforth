from django.shortcuts import render, get_object_or_404
from .models import Prof_Exp

def home(request): 
    prof_exps = Prof_Exp.objects
    return render(request, 'prof_exps/home.html', {'prof_exps' : prof_exps})

def detail(request, prof_exp_id): 
    prof_exp_detail = get_object_or_404(Prof_Exp, pk=prof_exp_id)
    return render(request, 'prof_exps/detail.html', {'prof_exp': prof_exp_detail})     