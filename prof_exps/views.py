from django.shortcuts import render, get_object_or_404
from .models import Prof_Exp, Education, About_Me

def home(request): 
    prof_exps = Prof_Exp.objects
    return render(request, 'prof_exps/home.html', {'prof_exps' : prof_exps})

def prof_exp_detail(request): 
    prof_exp_detail = Prof_Exp.objects
    return render(request, 'prof_exps/prof_exp_detail.html', {'prof_exps': prof_exp_detail})     

def education_detail(request): 
    education_detail =  get_object_or_404(Education)
    return render(request, 'education/education_detail.html', {'education': education_detail})     

def about_me_detail(request): 
    about_me_detail = get_object_or_404(About_Me)
    return render(request, 'about_me/about_me_detail.html', {'about_me': about_me_detail})     