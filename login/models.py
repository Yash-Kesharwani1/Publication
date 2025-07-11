from django.db import models

# Create your models here.
class CandidateDetails(models.Model):
    candidate_username = models.CharField(max_length=30)
    candidate_password = models.CharField(max_length=30)
    candidate_saltuation = models.CharField(max_length=7, default='')
    candidate_first_name = models.CharField(max_length=30)
    candidate_middle_name = models.CharField(max_length=30, default='')
    candidate_last_name = models.CharField(max_length=30)
    candidate_initials = models.CharField(max_length=10, default='')
    candidate_gender = models.CharField(max_length=20, default='Prefer not to say')
    candidate_affiliation = models.CharField(max_length=100, default='')
    candidate_signature = models.CharField(max_length=30, default='')
    candidate_email = models.EmailField()
    candidate_orcid_id = models.CharField(default='')
    candidate_website_url = models.CharField(default='')
    candidate_phone_number = models.CharField(max_length=15)
    candidate_fax_number = models.CharField(default='')
    candidate_mailing_address = models.CharField(default='')
    candidate_country = models.CharField()
    candidate_bio_statement = models.TextField(default='')