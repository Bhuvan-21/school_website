from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class mod(models.Model):

    school=models.CharField(unique=False,max_length=20)
    gender=models.CharField(max_length=10,choices=(('M','Male'),('F','Female')))
    age=models.IntegerField()
    address=models.CharField(max_length=10,choices=(('U','Urban'),('R','Rural')))
    famsize=models.CharField(max_length=3,choices=(('LE3','Less than 3'),('GT3','Greater than 3')))
    Pstatus=models.CharField(max_length=10,choices=(('T','Together'),('A','Apart')))
    Medu=models.CharField(max_length=10,choices=(('0','None'),('1','primary education'),('2','5th to 9th grade'),('3','secondary education'),('4','higher education')))
    Fedu=models.CharField(max_length=10,choices=(('0','None'),('1','primary education'),('2','5th to 9th grade'),('3','secondary education'),('4','higher education')))
    Mjob=models.CharField(max_length=10,choices=(('at_home','at_home'),('health','health'),('civil-services','civil-services'),('teacher','teacher'),('other','other')))
    Fjob=models.CharField(max_length=10,choices=(('at_home','at_home'),('health','health'),('civil-services','civil-services'),('teacher','teacher'),('other','other')))
    reason=models.CharField(max_length=10,choices=(('home','home'),('reputation','reputation'),('course','course'),('other','other')))
    guardian=models.CharField(max_length=10,choices=(('mother','mother'),('father','father'),('legal-guardian','legal-guardian')))
    traveltime=models.CharField(max_length=10,choices=(('0','<15min'),('1','15 to 30 min.'),('2','30 min. to 1 hour'),('3','>1 hour')))
    stime=models.CharField(max_length=10,choices=(('0','<120min'),('1','120 to 180 min.'),('2','300 min. to 10 hours'),('3','>10 hours')))
    failures=models.CharField(max_length=1)
    schoolsup=models.CharField(max_length=3,choices=(('no','NO'),('yes','Yes')))
    famsup=models.CharField(max_length=3,choices=(('no','NO'),('yes','Yes')))
    paid=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    activities=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    nursery=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    higher=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    internet=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    famrel=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    rom=models.CharField(max_length=10,choices=(('no','NO'),('yes','Yes')))
    freetime=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    goout=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    dalc=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    walc=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    health=models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)])
    absences=models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)])
    g1=models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    g2=models.IntegerField(default=1,validators=[MaxValueValidator(20), MinValueValidator(1)])
    def get_school(self):
        return self.school
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    def get_famsize(self):
        return self.famsize
    def get_pstatus(self):
        return self.Pstatus
    def get_address(self):
        return self.address
    def get_medu(self):
        return self.Medu
    def get_fedu(self):
        return self.Fedu
    def get_mjob(self):
        return self.Mjob
    def get_fjob(self):
        return self.Fjob
    def get_reason(self):
        return self.reason
    def get_guardian(self):
        return self.guardian
    def get_traveltime(self):
        return self.traveltime
    def get_stime(self):
        return self.stime
    def get_failure(self):
        return self.failures
    def get_schoolsup(self):
        return self.schoolsup
    def get_famsup(self):
        return self.famsup
    def get_paid(self):
        return self.paid
    def get_activities(self):
        return self.activities
    def get_nursery(self):
        return self.nursery
    def get_higher(self):
        return self.higher
    def get_internet(self):
        return self.internet
    def get_famrel(self):
        return self.famrel
    def get_freetime(self):
        return self.freetime
    def get_goout(self):
        return self.goout
    def get_dalc(self):
        return self.dalc
    def get_walc(self):
        return self.walc
    def get_health(self):
        return self.health
    def get_absences(self):
        return self.absences
    def get_g1(self):
        return self.g1
    def get_g2(self):
        return self.g2
    def get_rom(self):
        return self.rom

class Products(models.Model):
    school = models.TextField()
    product_type = models.TextField()
    price = models.IntegerField()
    #product_img = models.ImageField()                  
    size = models.TextField()                  #None for non wearables 
    nos = models.IntegerField()
    ratings = [models.IntegerField(), models.IntegerField()]

    def get_price(self):
        return self.price

    def check_stock(self):
        return (self.nos>0)

    def bought(self):
        self.nos -= 1
        pass

    def get_rating(self):
        return self.ratings[0]/self.ratings[1]

    def add_rating(self, a:int):
        self.ratings[0] += a
        self.ratings[1] += 5
        pass
