from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class mod(models.Model):

    school=models.CharField(unique=False,max_length=20)
    gender=models.CharField(max_length=10,choices=(('M','Male'),('F','Female')))
    age=models.IntegerField()
    address=models.CharField(max_length=10,choices=(('U','Urban'),('R','Rural')))
    familysize=models.CharField(max_length=3,choices=(('LE3','Less than 3'),('GT3','Greater than 3')))
    Parentalstatus=models.CharField(max_length=10,choices=(('T','Together'),('A','Apart')))
    Mothereducation=models.CharField(max_length=10,choices=(('0','None'),('1','primary education'),('2','5th to 9th grade'),('3','secondary education'),('4','higher education')))
    Fathereducation=models.CharField(max_length=10,choices=(('0','None'),('1','primary education'),('2','5th to 9th grade'),('3','secondary education'),('4','higher education')))
    Motherjob=models.CharField(max_length=10,choices=(('at_home','at_home'),('health','health'),('civil-services','civil-services'),('teacher','teacher'),('other','other')))
    Fatherjob=models.CharField(max_length=10,choices=(('at_home','at_home'),('health','health'),('civil-services','civil-services'),('teacher','teacher'),('other','other')))
    reasontojoinschool=models.CharField(max_length=10,choices=(('home','home'),('reputation','reputation'),('course','course'),('other','other')))
    guardian=models.CharField(max_length=10,choices=(('mother','mother'),('father','father'),('legal-guardian','legal-guardian')))
    traveltime=models.CharField(max_length=10,choices=(('0','<15min'),('1','15 to 30 min.'),('2','30 min. to 1 hour'),('3','>1 hour')))
    studytime=models.CharField(max_length=10,choices=(('0','<120min'),('1','120 to 180 min.'),('2','300 min. to 10 hours'),('3','>10 hours')))
    failures=models.CharField(max_length=1)
    schoolsupport=models.CharField(max_length=3,choices=(('no','NO'),('yes','Yes')))
    familysupport=models.CharField(max_length=3,choices=(('no','NO'),('yes','Yes')))
    paidsupport=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    activities=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    nursery=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    highereducation=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    internet=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    familyrelations=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    romanticrelationship=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    freetime=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    goout=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    dailyalcohol=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    weekendalcohol=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    health=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    absences=models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)])
    g1=models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    g2=models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    target=models.IntegerField()
    def get_school(self):
        return self.school
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    def get_famsize(self):
        return self.familysize
    def get_pstatus(self):
        return self.Parentalstatus
    def get_address(self):
        return self.address
    def get_medu(self):
        return self.Mothereducation
    def get_fedu(self):
        return self.Fathereducation
    def get_mjob(self):
        return self.Motherjob
    def get_fjob(self):
        return self.Fatherjob
    def get_reason(self):
        return self.reasontojoinschool
    def get_guardian(self):
        return self.guardian
    def get_traveltime(self):
        return self.traveltime
    def get_stime(self):
        return self.studytime
    def get_failure(self):
        return self.failures
    def get_schoolsup(self):
        return self.schoolsupport
    def get_famsup(self):
        return self.familysupport
    def get_paid(self):
        return self.paid
    def get_activities(self):
        return self.activities
    def get_nursery(self):
        return self.nursery
    def get_higher(self):
        return self.highereducation
    def get_internet(self):
        return self.internet
    def get_famrel(self):
        return self.familyrelations
    def get_freetime(self):
        return self.freetime
    def get_goout(self):
        return self.goout
    def get_dalc(self):
        return self.dailyalcohol
    def get_walc(self):
        return self.weekendalcohol
    def get_health(self):
        return self.health
    def get_absences(self):
        return self.absences
    def get_g1(self):
        return self.g1
    def get_g2(self):
        return self.g2
    def get_rom(self):
        return self.romanticrealtionship
    def get_target(self):
        return self.target
