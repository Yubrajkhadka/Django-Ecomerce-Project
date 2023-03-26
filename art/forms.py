from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Contact,Category,Product
from django import forms
from captcha.fields import CaptchaField
from django.core.validators import RegexValidator
from django.core.validators import  MinLengthValidator,EmailValidator
from .models import ORDER_STATUS



class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter username'}))
    firstname = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter firstname'}), validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='First name must contain only alphabet letters.',
                code='invalid_first_name'
            )])
    lastname = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter lastname'}),validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='Last name must contain only alphabet letters.',
                code='invalid_first_name'
            )])
    email = forms.CharField(widget = forms.EmailInput(attrs= {'class':'form-control my-2','placeholder':'Enter email'}),  validators=[
        EmailValidator(message='Enter a valid email address.'),])
    password1 = forms.CharField(widget = forms.PasswordInput(attrs= {'class': 'form-control my-2',
            'placeholder': 'Enter Password ',
            'title': 'Password must be at least 8 characters long and contain at least one uppercase letter, one digit, and one special character.'}), 
                                                                      
         validators=[
            MinLengthValidator(8, message='Password must be at least 8 characters long.'),
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$',
                message='Password must contain at least one uppercase letter, one digit, and one special character.',
                code='invalid_password'
            )
        ])
    password2 = forms.CharField(widget = forms.PasswordInput(attrs= {'class':'form-control my-2','placeholder':'Confirm password','title':'Reenter Password'}),  validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$',
                message='Password must contain at least one uppercase letter, one digit, and one special character.',
                code='invalid_password'
            )
        ])
   


    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','password1','password2']



    
class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter Full Name'}))
    email = forms.CharField(widget = forms.EmailInput(attrs= {'class':'form-control my-2','placeholder':'Enter Email','style': 'text-transform: lowercase;'}))
    number = forms.CharField(widget = forms.NumberInput(attrs= {'class':'form-control my-2','placeholder':'Enter Contact Number'}))
    subject = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Message'}))
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['fullname','email','subject','message']

class AddCategory(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter Category'}))
    slug = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2'}))

    class Meta:
        model = Category
        fields = ['name','slug']

    def save(self, commit=True):
        category = super().save(commit=False)
        if commit:
            category.save()
        return category

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['quantity']
        widgets = {
           
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5}),
            'price': forms.TextInput(attrs={'type': 'number', 'step': '0.01'}),
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'quantity': forms.NumberInput(attrs={'min': 1}),
        }

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        return product



        