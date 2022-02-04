''' holds form classes for products app '''
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    '''
    A form for super users to add products
    '''
    class Meta:
        '''
        defines which class is connected to the form
        and which fields from that class to generate
        '''
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]


        placeholders = {
            'category': 'category',
            'sku': 'sku',
            'name': 'name',
            'description': 'description',
            'has_sizes': 'has_sizes',
            'price': 'price',
            'rating': 'rating',
            'image_url': 'image_url',
            'image': 'image'            
        }

        self.fields['category'].choices = friendly_names
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
