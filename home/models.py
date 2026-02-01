from django.db import models

# Create your models here.
class GmServices(models.Model):
    services_name = models.CharField(max_length=100)
    services_period = models.IntegerField(blank=False)
    services_fess = models.IntegerField(blank=False)
    def __str__(self) -> str:
        return f"{self.services_fess}"

class NewService(models.Model):
    name = models.CharField(max_length=100)
    fees = models.IntegerField(blank=False)
    duration = models.IntegerField(blank=False)
    def __str__(self) -> str:
        return f"{self.name} -INR{self.fees} - {self.duration} days"
    
class Person(models.Model):
    adhar = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40,blank=False)
    gender = models.CharField(max_length=30,blank=False)
    avatar = models.ImageField(upload_to='avatars/')
    def __str__(self) -> str:
        return f"{self.name} - {self.adhar}"
    
class Family(models.Model):
    Family_lead = models.OneToOneField(Person,on_delete=models.CASCADE,related_name='Mukhiya')
    members = models.ManyToManyField(Person,related_name='families')
    def __str__(self) -> str:
        return str(self.Family_lead)
    
class Applicant(models.Model):
    name = models.CharField(max_length=40, blank=False)
    mobile = models.IntegerField(unique=True)  # Unique constraint instead of primary_key
    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=40, blank=False)
    email_add = models.CharField(max_length=40, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.age}"
     
    
class CandidateDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    title = models.CharField(max_length=200)  # Job Title
    department = models.CharField(max_length=100)  # Job Department
    vacancies = models.IntegerField()  # Number of Vacancies
    description = models.TextField()  # Job Description (Optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Created Time

    def __str__(self):
        return self.title