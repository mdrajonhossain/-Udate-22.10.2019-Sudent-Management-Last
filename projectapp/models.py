from django.db import models
from django.contrib.auth.models import User



userr_type = (
    ('Admin', 'Admin'),
    ('Bangla', 'Bangla'),
    ('Student', 'Student')
)

# Create your models here.
class Profile_Type(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worktype')
    user_Type = models.CharField(choices=userr_type, default='student', max_length=30)

    def __str__(self):
        return self.user_Type


class studentformsave(models.Model):
        student_name = models.CharField(max_length=30)
        father_name = models.CharField(max_length=30)
        mother_name = models.CharField(max_length=30)
        phonenumber = models.CharField(max_length=30)
        dateofbirth = models.CharField(max_length=30)
        address = models.CharField(max_length=30)
        city = models.CharField(max_length=30)
        departsubject = models.CharField(max_length=30)


        def __str__(self):
            return self.student_name





class student_account(models.Model):
    studentformsave = models.OneToOneField(studentformsave, on_delete=models.CASCADE, related_name='studenaccountfile')
    Tutionfee = models.IntegerField()
    bookfree = models.IntegerField()

    @property
    def total_tk(self):
        return self.Tutionfee + self.bookfree + self.Tutionfee - self.Tutionfee - self.bookfree * self.Tutionfee

