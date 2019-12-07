from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``modified_at`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CollegeUser(TimeStampedModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=15, null=True, blank=True)
    dob = models.DateField()
    
    def __str__(self):
        return "{}-{}".format(self.first_name, self.email)


class UserProfile(TimeStampedModel):
    user = models.OneToOneField(CollegeUser, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=15)
    geo_code = models.CharField(max_length=150)
    
    def __str__(self):
        return "{}-{}".format(self.user.first_name, self.user.email)
    

class Student(TimeStampedModel):
    user = models.OneToOneField(CollegeUser, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)
    percentage = models.FloatField()
    department = models.CharField(max_length=20)
    
    def __str__(self):
        return "{}-{}-{}".format(self.reg_no, self.user.first_name, self.user.email)
