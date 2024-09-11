from .models import *
from django import forms
from django.forms import ModelForm

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields= '__all__'


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields= '__all__'


class PoolForm(ModelForm):
    class Meta:
        model = Pool
        fields= '__all__'



class FixtureForm(ModelForm):
    class Meta:
        model = Fixture
        fields= '__all__'