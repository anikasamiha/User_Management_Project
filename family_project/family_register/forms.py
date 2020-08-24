# from django import forms
# from .models import Address, Parent, Child
# from address.forms import AddressField


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = '__all__'


# class ParentForm(forms.ModelForm):
#     class Meta:
#         model = Parent
#         fields = '__all__'


# class ChildForm(forms.ModelForm):
    
#     class Meta:
#         model = Child
#         fields = '__all__'
################################################################################################

from django.forms import ModelForm
from django import forms
from .models import *

class ParentForm(ModelForm):
    street = forms.CharField(max_length=200, required=False)
    city = forms.CharField(max_length=200, required=False)
    state = forms.CharField(max_length=200, required=False)
    zip = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Parent
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

    def save(self, commit=True):
        parent = super(ParentForm, self).save(commit=False)
        address = Address(street=self.cleaned_data['street'],
                              city=self.cleaned_data['city'],
                          state=self.cleaned_data['state'],
                          zip=self.cleaned_data['zip'])
        address.save()
        parent.address = address
        if commit:
            parent.save()
        return parent

class ChildForm(forms.ModelForm):
    
    class Meta:
        model = Child
        fields = '__all__'
    

# class ChildForm(ModelForm):
#     address_street = forms.CharField(max_length=200, required=False)
#     address_city = forms.CharField(max_length=200, required=False)
#     address_state = forms.CharField(max_length=200, required=False)
#     address_country = forms.CharField(max_length=200, required=False)

#     class Meta:
#         model = Parent
#         fields = ['first_name', 'last_name']

#     def save(self, commit=True):
#         parent = super(ParentForm, self).save(commit=False)
#         address = Address(street=self.cleaned_data['address_street'],
#                               city=self.cleaned_data['address_city'],
#                           state=self.cleaned_data['address_state'],
#                           country=self.cleaned_data['address_country'])
#         address.save()
#         parent.address = address
#         if commit:
#             parent.save()
#         return parent