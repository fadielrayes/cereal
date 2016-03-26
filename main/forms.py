from django. import forms 
from main.models import Cereal 

class CerealSearchForm(forms.Form):
	name = forms.CharField(required=True)
	manufacturer =forms.Charfield(required=True)

class CerealCityForm(forms.Form):
	class Meta:
		model = Cereal 
		fields = '__all__'