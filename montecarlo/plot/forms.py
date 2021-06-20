from django import forms
from django.core.exceptions import ValidationError

class PlotForm(forms.Form):
    amin = forms.FloatField(label="A-Min", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'A-min'}))
    amax = forms.FloatField(label="A-Max", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'A-max'}))
    
    def check_greater_a(self):
        amin = self.cleaned_data['amin']
        amax = self.cleaned_data['amax']
        
        if amin > amax:
            raise ValidationError('Please check your A values')
        return amin, amax
    
    bmin = forms.FloatField(label="B-Min", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'B-min'}))
    bmax = forms.FloatField(label="B-Max", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'B-max'}))
    
    def check_greater_b(self):
        bmin = self.cleaned_data['bmin']
        bmax = self.cleaned_data['bmax']
        
        if bmin > bmax:
            raise ValidationError('Please check your B values')
        return bmin, bmax
    
    cmin = forms.FloatField(label="C-Min", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'C-min'}))
    cmax = forms.FloatField(label="C-Max", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'C-max'}))
    
    def check_greater_b(self):
        cmin = self.cleaned_data['cmin']
        cmax = self.cleaned_data['cmax']
        
        if cmin > cmax:
            raise ValidationError('Please check your A values')
        return cmin, cmax
    
    dmin = forms.FloatField(label="D-Min", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'D-min'}))
    dmax = forms.FloatField(label="D-Max", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'D-max'}))
    
    def check_greater_b(self):
        dmin = self.cleaned_data['dmin']
        dmax = self.cleaned_data['dmax']
        
        if dmin > dmax:
            raise ValidationError('Please check your A values')
        return dmin, dmax
    
    emin = forms.FloatField(label="E-Min", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'E-min'}))
    emax = forms.FloatField(label="E-Max", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'E-max'}))
    
    def check_greater_b(self):
        emin = self.cleaned_data['emin']
        emax = self.cleaned_data['emax']
        
        if emin > emax:
            raise ValidationError('Please check your A values')
        return emin, emax
    
    smin = forms.FloatField(label="S-Min", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'S-min'}))
    smax = forms.FloatField(label="S-Max", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'S-max'}))
     
    def check_greater_b(self):
        smin = self.cleaned_data['smin']
        smax = self.cleaned_data['smax']
        
        if smin > smax:
            raise ValidationError('Please check your A values')
        return smin, smax
    
    z = forms.FloatField(label='Z', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Z', 'value': '1.50'}))