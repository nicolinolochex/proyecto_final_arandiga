from django import forms
from .models import TrabajaConNosotros, Contact, VehiculosClientes



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter a valid email address'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }
        error_messages = {
            'name': {'required': 'Please enter your name.'},
            'email': {'required': 'Please enter your email.'},
            'phone': {'required': 'Please enter your phone number.'},
            'message': {'required': 'Please enter your message.'},
        }

class VehiculosClientesForm(forms.ModelForm):
    class Meta:
        model = VehiculosClientes
        fields = ['unidad', 'modelo', 'kilometraje', 'precio_usd', 'foto']
        widgets = {
            'unidad': forms.TextInput(attrs={'placeholder': '(e.g., Ferrari Enzo)'}),
            'modelo': forms.NumberInput(attrs={'placeholder': ' (e.g., 2020)'}),
            'kilometraje': forms.NumberInput(attrs={'placeholder': 'Enter Km (e.g., 50000)'}),
            'precio_usd': forms.NumberInput(attrs={'placeholder': 'Enter price in USD'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file', 'accept': 'image/*'}),
        }
        error_messages = {
            'unidad': {'required': 'Please enter the vehicle unit.'},
            'modelo': {'required': 'Please enter the model year of the vehicle.'},
            'kilometraje': {'required': 'Please enter the mileage of the vehicle.'},
            'precio_usd': {'required': 'Please enter the price of the vehicle in USD.'},
            'foto': {'required': 'Please upload a photo of the vehicle.'},
        }

class TrabajaConNosotrosForm(forms.ModelForm):
    class Meta:
        model = TrabajaConNosotros
        fields = ['nombre', 'apellido', 'email', 'telefono', 'curriculum']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'curriculum': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        error_messages = {
            'nombre': {'required': 'Please enter your first name.'},
            'apellido': {'required': 'Please enter your last name.'},
            'email': {'required': 'Please enter a valid email address.'},
            'telefono': {'required': 'Please enter your phone number.'},
            'curriculum': {'required': 'Please upload your curriculum.'},
        }

class BuscaVehiculoForm(forms.Form):
    unidad = forms.CharField(max_length=50, required=False, label="Modelo (Ej. Ferrari Enzo)")
    modelo = forms.CharField(max_length=100, required=False, label="Año")
