from django.db import models

class premier_log_refined(models.Model):
    Account_id = models.CharField(max_length=32, null=True, blank=True)
    client = models.CharField(max_length=32, null=True, blank=True)
    type=models.CharField(max_length=32, null=True, blank=True)
    status = models.CharField(max_length=8)
    status_date=models.DateField(null=True, blank=True)
    date_generated = models.DateField(max_length=32,null=True, blank=True)

class entry_journals(models.Model):
    debit_amount=models.DecimalField(max_digits=10, decimal_places=2)
    debit_glaccount=models.CharField(max_length=32)
    debit_branch=models.CharField(max_length=20)
    credit_amount=models.DecimalField(max_digits=10, decimal_places=2)
    credit_glaccount=models.CharField(max_length=32)
    credit_branch=models.CharField(max_length=20)
    entry_date=models.DateField(max_length=32,null=True, blank=True)
    notes=models.CharField(max_length=200)
    
    def __str__(self):
        return self.notes

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn_number = models.CharField(max_length=13)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.name

# create gl_accounts which are activated and allowManualJournalEntries are true
class Gl_accounts(models.Model):
    encoded_key=models.CharField(max_length=255)
    glCode=models.CharField(max_length=255)
    name=models.CharField(max_length=255)

    