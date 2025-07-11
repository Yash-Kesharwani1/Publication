from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

def login(request):
    return render(request, 'login/login.html')

def registration(request):
    return render(request, 'registration/registration.html')

def save_candidate(request):
    print(request.POST)
    candidate = models.CandidateDetails(
        candidate_username = request.POST['candidate_username'],
        candidate_password = request.POST['candidate_password'],
        candidate_saltuation = request.POST['candidate_saltuation'],
        candidate_first_name = request.POST['candidate_first_name'],
        candidate_last_name = request.POST['candidate_last_name'],
        candidate_middle_name = request.POST['candidate_middle_name'],
        candidate_initials = request.POST['candidate_initials'],
        candidate_gender = request.POST['candidate_gender'],
        candidate_affiliation = request.POST['candidate_affiliation'],
        candidate_signature = request.POST['candidate_signature'],
        candidate_email = request.POST['candidate_email'],
        candidate_orcid_id = request.POST['candidate_orcid_id'],
        candidate_website_url = request.POST['candidate_website_url'],
        candidate_phone_number = request.POST['candidate_phone_number'],
        candidate_fax_number = request.POST['candidate_fax_number'],
        candidate_mailing_address = request.POST['candidate_mailing_address'],
        candidate_country = request.POST['candidate_country'],
        candidate_bio_statement = request.POST['candidate_bio_statement']
    )
    candidate.save()
    return HttpResponse("User Registered Successfully")

def all_candidate_details(request):
    candidates = models.CandidateDetails.objects.all()
    obj = {'candidates':candidates}
    return render(request, 'all_candidate_details.html', obj)

def candidate_login(request):
    candidates = models.CandidateDetails.objects.filter(
        candidate_username = request.POST['candidate_username'],
        candidate_password = request.POST['candidate_password']
    )
    if len(candidates)>0:
        return HttpResponse("User Login Successfully")
    else:
        return HttpResponse("Invalid Userlogin")
    
def edit_candidate(request):
    candidate = models.CandidateDetails.objects.get(id=request.GET['id'])
    obj = {'candidate':candidate}
    return render(request, 'edit_candidate.html',obj)

def save_edited_candidate(request):
    candidate = models.CandidateDetails.objects.get(id=request.POST['id'])
    candidate_username = request.POST['candidate_username']
    candidate.candidate_password = request.POST['candidate_password']
    candidate.candidate_saltuation = request.POST['candidate_saltuation']
    candidate.candidate_first_name = request.POST['candidate_first_name']
    candidate.candidate_last_name = request.POST['candidate_last_name']
    candidate.candidate_middle_name = request.POST['candidate_middle_name']
    candidate.candidate_initials = request.POST['candidate_initials']
    candidate.candidate_gender = request.POST['candidate_gender']
    candidate.candidate_affiliation = request.POST['candidate_affiliation']
    candidate.candidate_signature = request.POST['candidate_signature']
    candidate.candidate_email = request.POST['candidate_email']
    candidate.candidate_orcid_id = request.POST['candidate_orcid_id']
    candidate.candidate_website_url = request.POST['candidate_website_url']
    candidate.candidate_phone_number = request.POST['candidate_phone_number']
    candidate.candidate_fax_number = request.POST['candidate_fax_number']
    candidate.candidate_mailing_address = request.POST['candidate_mailing_address']
    candidate.candidate_country = request.POST['candidate_country']
    candidate.candidate_bio_statement = request.POST['candidate_bio_statement']
    candidate.save()
    return redirect('/login/all_candidate_details/')

def delete_candidate(request):
    models.CandidateDetails.objects.get(id=request.GET['id']).delete()
    return redirect('/login/all_candidate_details/')
