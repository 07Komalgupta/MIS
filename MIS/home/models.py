from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, RESTRICT, SET_DEFAULT, SET_NULL
from django.db.models.fields.related import ForeignKey
# Create your models here.

BRANCH_CHOICES = [
        ('05', 'Uttam Nagar'),
        ('06', 'East Azad Nagar'),
        ('07', 'Pitampura'),
        ('08', 'Kalka Ji'),
        ('09', 'Badarpur'),
        ('10', 'Dilshad Garden'),
    ]

GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]

STREAM = [
    ('arts', 'Arts'),
    ('commerce', 'Commerce'),
    ('science', 'Science'),
    ('humanities', 'Humanities')
]

CITY = [
        ('newdelhi', 'New Delhi'),
      
    ]
                                             
class LoginUser(models.Model):
    CHOICE = [
        ('admin', 'Admin'),
        ('counselor', 'Counselor'),
        ('centerhead', 'Centerhead'),
        ('trainer', 'Trainer'),
    ]
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  
    branch = models.CharField(max_length=255, choices= BRANCH_CHOICES)
    role = models.CharField(max_length=20, choices=CHOICE)

    def __str__(self):
        return self.user.first_name


class Course(models.Model):
    CLASS_MODE = [
    ('online', 'online'),
    ('offline', 'offline'),
    ('weekend', 'weekend'),
]
    courseid = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=120)
    fee = models.IntegerField()
    duration = models.CharField(max_length=120)
    hours = models.IntegerField()
    class_mode = models.CharField(max_length=120, choices=CLASS_MODE)
    description = models.CharField(max_length=120)
    course_exam = models.CharField(max_length=120)
    main_content = models.CharField(max_length=120)
    upgradation = models.CharField(max_length=120)
    prerequisites = models.CharField(max_length=120)
    category = models.CharField(max_length=120)
    seats = models.IntegerField()
    is_active = models.CharField(max_length=120) 
    is_composite = models.CharField(max_length=120)
    no_of_exam = models.IntegerField()
        
    
class Module(models.Model):
    moduleid = models.CharField(max_length=120, unique=True)
    name = models.CharField(max_length=120)
    duration = models.CharField(max_length=50)
    course = ForeignKey(Course, on_delete=models.CASCADE)


class Batch(models.Model):
    branch = models.CharField(max_length=120, choices=BRANCH_CHOICES)
    name = models.CharField(max_length=120)
    member = models.ForeignKey(LoginUser, on_delete=RESTRICT)
    course = models.ForeignKey(Course, on_delete=RESTRICT)
    module = models.ForeignKey(Module, on_delete=RESTRICT)
    time = models.TimeField()
    days = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    remarks = models.CharField(max_length=155)
    is_active = models.BooleanField()
    examid = models.CharField(max_length=20)


class Student(models.Model):
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    reg_no = models.CharField(max_length=30, unique=True)
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    fathername = models.CharField(max_length=120)
    mothername = models.CharField(max_length=120) 
    fatherocc = models.CharField(max_length=120)
    add1 = models.CharField(max_length=150)
    add2 = models.CharField(max_length=120) 
    city  = models.CharField(max_length=120)
    pincode = models.IntegerField()
    contact1 = models.IntegerField()
    contact2 = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateField()
    stream = models.CharField(max_length=10, choices=STREAM)
    sch_location = models.CharField(max_length=120)
    school = models.CharField(max_length=120)
    adm_date = models.DateField()
    course = models.ForeignKey(Course, on_delete= RESTRICT)
    batch = models.ForeignKey(Batch, on_delete= RESTRICT, related_name='primarybatch')
    batch1 = models.ForeignKey(Batch, blank=True, null= True, on_delete= RESTRICT, related_name='secondarybatch')
    totalfee = models.IntegerField()
    adm_fee = models.IntegerField()
    inst = models.IntegerField()
    inst_amt = models.IntegerField()
    inst_date = models.DateField()
    counselor = models.ForeignKey(LoginUser, on_delete=RESTRICT)
    status = models.CharField(max_length=20)

class Fee(models.Model):
    # student = models.ForeignKey(Student, on_delete=RESTRICT)
    pass
