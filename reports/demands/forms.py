from django import forms
import datetime
import requests
from django.forms import formset_factory

class PremierReportForm(forms.Form):
    
    TYPES  = [
        ('', '--------------'),
        ('All','All'),
        ('Demand One ','Demand One'),
        ('Demand Two ','Demand Two'),
        ('Guarantor One ','Guarantor_One'),
        ('Guarantor Two','Guarantor Two'),
        ('Recall','Recall')
    ]


    demand_type = forms.ChoiceField(required=False, label='Types', choices=TYPES)
    dfrom = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }), label='From (YYYY/MM/DD)')
    dto = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                }), label='To (YYYY/MM/DD)')

# class journalEntryForm(forms.Form):
#     # get all glaccounts by type
#     main_url="https://momentumcreditltd.sandbox.mambu.com/api/glaccounts?type="""
#     access_credentials=('BACKUPTEST', 'backup123!@#123')

#     assets_url = main_url + "ASSET"
#     type_assets = requests.get(assets_url, auth=access_credentials)
#     asset_load =type_assets.json()
#     TYPE_ASSETS = []
   
#     for rw in asset_load:
#         encodedKey=rw.get('encodedKey')
#         glcode = rw.get('glCode')
#         name = rw.get('name')
#         TYPE_ASSETS.append([encodedKey, (glcode +' '+ '-'+' '+ name)])

#     liability_url=main_url + "LIABILITY"
#     type_liability = requests.get(liability_url, auth=access_credentials)
#     liability_load = type_liability.json()

#     TYPE_LIABILITY = []
#     for rw in liability_load:
#         encodedKey=rw.get('encodedKey')
#         glcode = rw.get('glCode')
#         name = rw.get('name')
#         TYPE_LIABILITY.append([encodedKey,(glcode +' '+ '-'+' '+ name)])

#     equity_url=main_url +"EQUITY"
#     type_equity = requests.get(equity_url, auth=access_credentials)
#     equity_load = type_equity.json()

#     TYPE_EQUITY = []
#     for rw in equity_load:
#         encodedKey=rw.get('encodedKey')
#         glcode = rw.get('glCode')
#         name = rw.get('name')
#         TYPE_EQUITY.append([encodedKey,(glcode +' '+ '-'+' '+ name)])


#     income_url=main_url +"INCOME"
#     type_income = requests.get(income_url, auth=access_credentials)
#     income_load = type_income.json()

#     TYPE_INCOME = []
#     for rw in income_load:
#         encodedKey=rw.get('encodedKey')
#         glcode = rw.get('glCode')
#         name = rw.get('name')
#         TYPE_INCOME.append([encodedKey,(glcode +' '+ '-'+' '+ name)])
    
#     expense_url=main_url + "EXPENSE"
#     type_expense= requests.get(expense_url, auth=access_credentials)
#     expense_load = type_expense.json()

#     TYPE_EXPENSE = []
#     for rw in expense_load:
#         encodedKey=rw.get('encodedKey')
#         glcode = rw.get('glCode')
#         name = rw.get('name')
#         TYPE_EXPENSE.append([encodedKey,(glcode +' '+ '-'+' '+ name)])

    

#     TYPE_GLACCOUNT = [('', '-------------------------------')] + TYPE_ASSETS + TYPE_LIABILITY + TYPE_EQUITY + TYPE_INCOME + TYPE_EXPENSE


#     # get all branches
#     branches_url="https://momentumcreditltd.sandbox.mambu.com/api/branches"
#     branches=requests.get(branches_url,auth=('BACKUPTEST', 'backup123!@#123'))
#     branches_load=branches.json()
#     TYPES  = []

#     for rw in branches_load:
#         # state= rw.get('state')
#         name= rw.get('name')
#         TYPES.append([str(name), str(name)])


#     TYPE_BRANCH = [('', '-------------------------------')] + TYPES


#     debit=forms.DecimalField(widget=forms.TextInput(attrs={'class' : 'debitform','placeholder': 'Ksh'}),max_digits=10, decimal_places=2,required=True, label='Debit')
#     debit_gl = forms.ChoiceField(required=True,label='', choices=TYPE_GLACCOUNT,widget=forms.Select(attrs={'class':'debit_glform'}))
#     debit_branch = forms.ChoiceField(required=True,label='',choices=TYPE_BRANCH,widget=forms.Select(attrs={'class':'debit_branch'}))
#     credit=forms.DecimalField(widget=forms.TextInput(attrs={'class' : 'creditform','placeholder': 'Ksh'}),required=True,max_digits=10, decimal_places=2, label='Credit')
#     credit_gl = forms.ChoiceField(label='',required=True,choices=TYPE_GLACCOUNT,widget=forms.Select(attrs={'class':'credit_glform'}))
#     credit_branch = forms.ChoiceField(label='',choices=TYPE_BRANCH,required=True,widget=forms.Select(attrs={'class':'credit_branch'}))
#     entryDate = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),required=True, label='Entry Date')
#     notes = forms.CharField(widget=forms.Textarea(attrs={'class' : 'notesform'}),required=True,label='Notes')


class EntryJournalForm(forms.Form):
    main_url="https://momentumcreditltd.sandbox.mambu.com/api/glaccounts?type="""
    access_credentials=('BACKUPTEST', 'backup123!@#123')

    assets_url = main_url + "ASSET"
    type_assets = requests.get(assets_url, auth=access_credentials)
    asset_load =type_assets.json()
    TYPE_ASSETS = []
   
    for rw in asset_load:
        encodedKey=rw.get('encodedKey')
        glcode = rw.get('glCode')
        name = rw.get('name')
        TYPE_ASSETS.append([encodedKey, (glcode +' '+ '-'+' '+ name)])

    liability_url=main_url + "LIABILITY"
    type_liability = requests.get(liability_url, auth=access_credentials)
    liability_load = type_liability.json()

    TYPE_LIABILITY = []
    for rw in liability_load:
        encodedKey=rw.get('encodedKey')
        glcode = rw.get('glCode')
        name = rw.get('name')
        TYPE_LIABILITY.append([encodedKey,(glcode +' '+ '-'+' '+ name)])

    equity_url=main_url +"EQUITY"
    type_equity = requests.get(equity_url, auth=access_credentials)
    equity_load = type_equity.json()

    TYPE_EQUITY = []
    for rw in equity_load:
        encodedKey=rw.get('encodedKey')
        glcode = rw.get('glCode')
        name = rw.get('name')
        TYPE_EQUITY.append([encodedKey,(glcode +' '+ '-'+' '+ name)])


    income_url=main_url +"INCOME"
    type_income = requests.get(income_url, auth=access_credentials)
    income_load = type_income.json()

    TYPE_INCOME = []
    for rw in income_load:
        encodedKey=rw.get('encodedKey')
        glcode = rw.get('glCode')
        name = rw.get('name')
        TYPE_INCOME.append([encodedKey,(glcode +' '+ '-'+' '+ name)])
    
    expense_url=main_url + "EXPENSE"
    type_expense= requests.get(expense_url, auth=access_credentials)
    expense_load = type_expense.json()

    TYPE_EXPENSE = []
    for rw in expense_load:
        encodedKey=rw.get('encodedKey')
        glcode = rw.get('glCode')
        name = rw.get('name')
        TYPE_EXPENSE.append([encodedKey,(glcode +' '+ '-'+' '+ name)])

    

    TYPE_GLACCOUNT = [('', '-------------------------------')] + TYPE_ASSETS + TYPE_LIABILITY + TYPE_EQUITY + TYPE_INCOME + TYPE_EXPENSE


    # get all branches
    branches_url="https://momentumcreditltd.sandbox.mambu.com/api/branches"
    branches=requests.get(branches_url,auth=('BACKUPTEST', 'backup123!@#123'))
    branches_load=branches.json()
    TYPES  = []

    for rw in branches_load:
        # state= rw.get('state')
        name= rw.get('name')
        TYPES.append([str(name), str(name)])


    TYPE_BRANCH = [('', '-------------------------------')] + TYPES


    debit=forms.DecimalField(widget=forms.TextInput(attrs={'class' : 'debitform','placeholder': 'Ksh'}),max_digits=10, decimal_places=2,required=True, label='Debit')
    debit_gl = forms.ChoiceField(required=True,label='', choices=TYPE_GLACCOUNT,widget=forms.Select(attrs={'class':'debit_glform'}))
    debit_branch = forms.ChoiceField(required=True,label='',choices=TYPE_BRANCH,widget=forms.Select(attrs={'class':'debit_branch'}))
    credit=forms.DecimalField(widget=forms.TextInput(attrs={'class' : 'creditform','placeholder': 'Ksh'}),required=True,max_digits=10, decimal_places=2, label='Credit')
    credit_gl = forms.ChoiceField(label='',required=True,choices=TYPE_GLACCOUNT,widget=forms.Select(attrs={'class':'credit_glform'}))
    credit_branch = forms.ChoiceField(label='',choices=TYPE_BRANCH,required=True,widget=forms.Select(attrs={'class':'credit_branch'}))
    entryDate = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),required=True, label='Entry Date')
    notes = forms.CharField(widget=forms.Textarea(attrs={'class' : 'notesform'}),required=True,label='Notes')

EntryJournalFormset= formset_factory(EntryJournalForm, extra=1)




class BookForm(forms.Form):
    name = forms.CharField(
        label='Book Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    )
BookFormset = formset_factory(BookForm, extra=1)