from django.db import models

class EMPLOYEE(models.Model):
    emp_id = models.CharField(max_length=9)
    firstname = models.CharField(max_length=45)
    mi = models.CharField(max_length=1)
    lastname = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    address = models.CharField(max_length=100)

class STUD_PRIV(models.Model):
    priv_name = models.CharField(max_length=100)
    discount = models.FloatField(max_length=3)

class STUDENT(models.Model):
    gender_choice = (('M', 'Male'),
              ('F', 'Female'))
    stud_id = models.CharField(max_length=9)
    firstname = models.CharField(max_length=45)
    mi = models.CharField(max_length=1)
    lastname = models.CharField(max_length=45)
    gender = models.CharField(max_length=1, choices=gender_choice)
    date_of_birth = models.DateField()
    date_admitted = models.DateField()
    mother_name = models.CharField(max_length=45) 
    father_name = models.CharField(max_length=45)
    mother_occ = models.CharField(max_length=45)  # mother occupation
    father_occ = models.CharField(max_length=45)  # father occupation
    last_school_att = models.CharField(max_length=100)
    last_school_att_add = models.CharField(max_length=100)
    acad_status = models.CharField(max_length=45)
    priv = models.ForeignKey(STUD_PRIV)


class BILL_ITEM(models.Model):    
    item_name = models.CharField(max_length=45)
    amount  = models.DecimalField(max_digits=5, decimal_places=2)


class STUD_BILL_ACC(models.Model):
    stud_id = models.ForeignKey(STUDENT)
    emp_id = models.ForeignKey(EMPLOYEE)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    amount_tender = models.DecimalField(max_digits=6, decimal_places=2)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    school_year = models.CharField(max_length=9)
    year_level = models.IntegerField()
    date_received = models.DateField()


class STUD_BILL_BREAKDOWN(models.Model):
    sba_id = models.ForeignKey(STUD_BILL_ACC)
    bill_item_id = models.ManyToManyField(BILL_ITEM)
    amount = models.DecimalField(max_digits=6, decimal_places=2)

class BILL_ASSIGN(models.Model):
    bill_item_id = models.ManyToManyField(BILL_ITEM)
    school_year = models.CharField(max_length=9)
    year_level = models.IntegerField()


class ENTRANCE_FEE(models.Model):
    bill_item_id = models.ForeignKey(BILL_ITEM)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payee = models.CharField(max_length=45)
    date_recieved = models.DateField()
    emp_id = models.ManyToManyField(EMPLOYEE)
    

class SUBJECT(models.Model):
    title = models.CharField(max_length=45)
    units = models.IntegerField()


class SECTION(models.Model):
    name = models.CharField(max_length=45)
    roon_no = models.IntegerField()


class STUD_SUBJECTS(models.Model):
    subject_id = models.ManyToManyField(SUBJECT)
    stud_id = models.ForeignKey(STUDENT)
    section_id = models.ForeignKey(SECTION)
    emp_id = models.ForeignKey(EMPLOYEE)
    year_level = models.IntegerField()
    school_year = models.CharField(max_length=9)
    time_fr = models.TimeField()
    time_to = models.TimeField()
    days = models.CharField(max_length=6)


class CHARACTER_RATE(models.Model):
   
    character_choices = (('C','Cleanliness'),
                         ('CP','Courtesy and Politeness'),
                         ('HC','Helpfulness and Cooperativeness'),
                         ('I','Industriousness'),
                         ('LI','Leadership and Innitiative'),
                         ('O','Obedience'),
                         ('SC','Self Control'),
                         ('PP','Promptness and Punctuality'),
                         ('S','Sportmanship'),
                         ('TE','Thrift and Economy'),
                         ('MS','Modesty and Simplicity')
                        );

    stud_id = models.ForeignKey(STUDENT)
    rate = models.FloatField(max_length=3)
    character = models.CharField(max_length=2,choices=character_choices)
    year_level = models.IntegerField()
    school_year = models.CharField(max_length=5)
    period = models.IntegerField()
    date_rated = models.CharField(max_length=45)


class ATTENDANCE(models.Model):
    stud_id = models.ForeignKey(STUDENT)
    year_level = models.IntegerField()
    school_year = models.CharField(max_length=5)
    no_school_days = models.IntegerField()
    no_school_days_tardy = models.IntegerField()
    no_school_days_present = models.IntegerField()
    month = models.CharField(max_length=9)
    

    
    
