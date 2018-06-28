from monitor.models import AlertSetting
from django import forms

class SettingsForm(forms.ModelForm):
    class Meta:
        model = AlertSetting
        fields = ('sensor','label','alert', 'lowerlimit', 'upperlimit','slider')
        widgets = {
            'sensor': forms.TextInput(attrs={'readonly':'readonly'}),
            'label': forms.TextInput(attrs={'readonly':'readonly'})
        }
