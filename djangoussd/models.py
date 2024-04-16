from django.db import models


class Users(models.Model):
    image_url = models.ImageField(upload_to='images/', null=True)
    firstname = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False, null=True)
    number = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    vercode = models.CharField(max_length=250, blank=True, null=True)
    contactperson = models.CharField(max_length=250, blank=True, null=True)
    compregno = models.CharField(max_length=250, blank=True, null=True)
    compkrapin = models.CharField(max_length=250, blank=True, null=True)
    accounttype = models.CharField(max_length=250, default='individual')
    idorpassport = models.CharField(max_length=250, blank=True, null=True)
    idnumber = models.CharField(max_length=250, blank=True, null=True)
    idfrontimg = models.ImageField(upload_to='images/', null=True)
    idbackimg = models.ImageField(upload_to='images/', null=True)
    incorporationcert = models.ImageField(upload_to='images/', null=True)
    bussinessnumber = models.ImageField(upload_to='images/', null=True)
    krapin = models.ImageField(upload_to='images/', null=True)
    companydoc1 = models.ImageField(upload_to='images/', null=True)
    companydoc2 = models.ImageField(upload_to='images/', null=True)
    companydoc3 = models.ImageField(upload_to='images/', null=True)
    companydoc4 = models.ImageField(upload_to='images/', null=True)
    companydoc5 = models.ImageField(upload_to='images/', null=True)
    companydoc6 = models.ImageField(upload_to='images/', null=True)
    companydoc7 = models.ImageField(upload_to='images/', null=True)
    companydoc8 = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Recipients(models.Model):
    firstname = models.CharField(max_length=30, blank=False, null=False)
    lastname = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField()
    useremail = models.EmailField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Transactions(models.Model):
    name = models.CharField(max_length=230, blank=False, null=False)
    sendername = models.CharField(max_length=230, blank=False, null=False)
    description = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(null=True)
    senderemail = models.EmailField(null=True, blank=True)
    recipientemail = models.EmailField(null=True)
    status = models.CharField(max_length=230, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=230, blank=False, null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Notifications(models.Model):
    notification = models.CharField(max_length=260, blank=True, null=True)
    url = models.CharField(max_length=30, blank=False, null=False)
    useremail = models.EmailField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=230, blank=False, null=True)
    recipientemail = models.EmailField(null=True)
    senderemail = models.EmailField(null=True)
    amount = models.CharField(max_length=30, blank=False, null=True)
    status = models.CharField(max_length=200, default='unread')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Card(models.Model):
    useremail = models.CharField(max_length=260, blank=False, null=False)
    cardnumber = models.CharField(max_length=260, blank=False, null=False)
    cardholder = models.CharField(max_length=260, blank=False, null=False)
    year = models.CharField(max_length=260, blank=False, null=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
