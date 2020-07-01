from django.db import models

# Create your models here.
class Student(models.Model):
    adm_no = models.IntegerField()
    first_name = models.TextField(max_length = 20)
    last_name = models.TextField(max_length = 20)
<<<<<<< HEAD
    subject = models.TextField(max_length = 20)
||||||| 85ae26b
    subject = models.TextField(max_lentgh = 20)
=======
>>>>>>> 60508e0dfed4954e81f744afb41457e374eea37d
    working_days = models.IntegerField()
    present_days = models.IntegerField()
    half_days = models.IntegerField()
    absent_days = models.IntegerField()
<<<<<<< HEAD
||||||| 85ae26b
    
=======
    marks_eng_mt = models.IntegerField()
    marks_eng_ft = models.IntegerField()
    marks_math_mt = models.IntegerField()
    marks_math_ft = models.IntegerField()
    marks_sci_mt = models.IntegerField()
    marks_sci_ft = models.IntegerField()
    marks_sst_mt = models.IntegerField()
    marks_sst_ft = models.IntegerField()
    marks_hin_mt = models.IntegerField()
    marks_hin_ft = models.IntegerField()

    def get_adm_no(self):
        return self.adm_no

    def get_first_name(self):
        return self.first_name 

    def get_last_name(self):
        return self.last_name

    def get_working_days(self):
        return self.working_days

    def get_present_days(self):
        return self.present_days
    
    def get_half_days(self):
        return self.half_days

    def get_absent_days(self):
        return self.absent_days

    def get_marks_eng_mt(self):
        return self.marks_eng_mt

    def get_marks_eng_ft(self):
        return self.marks_eng_ft

    def get_marks_math_mt(self):
        return self.marks_math_mt

    def get_marks_math_ft(self):
        return self.marks_math_ft

    def get_marks_hin_mt(self):
        return self.marks_hin_mt

    def get_marks_hin_ft(self):
        return self.marks_hin_ft

    def get_marks_sci_mt(self):
        return self.marks_sci_mt

    def get_marks_sci_ft(self):
        return self.marks_sci_ft

    def get_marks_sst_mt(self):
        return self.marks_sst_mt

    def get_marks_sst_ft(self):
        return self.marks_sst_ft

    
>>>>>>> 60508e0dfed4954e81f744afb41457e374eea37d
