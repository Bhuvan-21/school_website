from django.db import models

# Create your models here.
class mod(models.Model):

    school=models.CharField(unique=False,max_length=20)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    address=models.CharField(max_length=10)
    famsize=models.CharField(max_length=3)
    Pstatus=models.CharField(max_length=10)
    Medu=models.CharField(max_length=10)
    Fedu=models.CharField(max_length=10)
    Mjob=models.CharField(max_length=10)
    Fjob=models.CharField(max_length=10)
    reason=models.CharField(max_length=10)
    guardian=models.CharField(max_length=10)
    traveltime=models.CharField(max_length=1)
    stime=models.CharField(max_length=1)
    failures=models.CharField(max_length=1)
    schoolsup=models.CharField(max_length=3)
    famsup=models.CharField(max_length=3)
    paid=models.CharField(max_length=10)
    activities=models.CharField(max_length=10)
    nursery=models.CharField(max_length=10)
    higher=models.CharField(max_length=10)
    internet=models.CharField(max_length=10)
    famrel=models.CharField(max_length=10)
    rom=models.CharField(max_length=10)
    freetime=models.CharField(max_length=10)
    goout=models.CharField(max_length=10)
    dalc=models.CharField(max_length=10)
    walc=models.CharField(max_length=10)
    health=models.CharField(max_length=10)
    absences=models.CharField(max_length=10)
    g1=models.CharField(max_length=10)
    g2=models.CharField(max_length=10)

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
"""
class Products(models.Model):
    school = models.TextField()
    product_type = models.TextField()
    price = models.IntegerField()
    product_img = models.ImageField()
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

    def add_rating(self, a:int)
        self.ratings[0] += a
        self.ratings[1] += 5
"""
