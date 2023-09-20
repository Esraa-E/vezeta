from django.db import models


# Create your models here.
class profile(models.Model):
    DOCTOR_IN={
        ("جلديه","جلديه"),
        ("اسنان","اسنان"),
        ("نفسي","نفسي"),
        ("اطفال حديثي الولاده","اطفال حديثي الولاده"),
        ("مخ و اعصاب","مخ و اعصاب"),
        ("نساء و توليد","نساء و توليد"),
        ("عظام","عظام"),
        ("انف و اذن","انف و اذن"),
        ("قلب و اعيه دمويه","فلب و اعيه دمويه"),
        ("امراض دم","امراض دم"),
        ("اورام","اورام"),
        ("باطنه","باطنه"),
        ("تخسيس و تغذيه","تخسيس و تغذيه"),
        ("جراحه اطفال","جراحه اطفال"),
        ("جراحه اورام","جراحه اورام"),
        ("جراحه اوعيه دمويه","جراحه اوعيه دمويه"),
        ("جراحه تجميل","جراحه تجميل"),
        ("جراحه سمنه و مناظير","جراحه سمنه و مناظير"),
        
    }
    TYPE_OF_PERSON={
        ("رجل","رجل"),
        ("انثي","انثي"),
    }
    name=models.CharField(("الاسم:"),max_length=80)
    surname=models.CharField(("اللقب:"),max_length=50)
    subtitle=models.CharField(("نبذه عنك:"),max_length=50)
    address=models.CharField(("المحافظه:"),max_length=50)
    address_details=models.CharField(("العنوان بالتفصيل:"),max_length=50)
    number_phone=models.CharField(("الهاتف:"),max_length=50)
    working_hours=models.CharField(("ساعات العمل:"),max_length=50)
    waiting_time=models.IntegerField(("مده الانتظار:"),null=True,blank=True)
    who_i=models.TextField(("من انا:"),max_length=250,null=True, blank=True)
    price=models.IntegerField(("سعر الكشق:"),blank=True,null=True)
    facebook=models.CharField(max_length=100,blank=True,null=True)
    twitter=models.CharField(max_length=100,blank=True,null=True)
    google=models.CharField(max_length=100,blank=True,null=True)
    join_new=models.DateTimeField(("وقت الانضمام:"),auto_now_add=True,blank=True,null=True)
    type_of_person=models.CharField(("النوع:"),choices=TYPE_OF_PERSON,max_length=50)
    doctor=models.CharField(("الدكتور ؟"),choices=DOCTOR_IN,max_length=50,blank=True,null=True)
    specialist_doctor=models.CharField(("متخصص في؟"),max_length=100,blank=True,null=True)
    image=models.ImageField(("الصوره الشخصيه:"),upload_to='images',blank=True,null=True)
    def __str__(self):
        return self.name





class reservation(models.Model):
    name=models.CharField(("الاسم:"),max_length=30)
    date=models.DateTimeField(("وقت الكشف"),blank=True,null=True)
    crated=models.CharField(("الدفع"),max_length=50)
    doc=models.ForeignKey(profile,related_name='docc',on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class comment(models.Model):
    post=models.ForeignKey(profile,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    