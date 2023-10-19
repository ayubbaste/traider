from django import forms
from django.forms import inlineformset_factory, ModelForm, HiddenInput, BaseFormSet, BaseInlineFormSet, ValidationError
from django.conf import settings

from traider.models import Coin, Traid, Reason, EntryReason

# https://github.com/yourlabs/django-autocomplete-light
# https://django-autocomplete-light.readthedocs.io/en/
from dal import autocomplete
from django.utils.html import format_html

# custom bootstrap Data & Time picker fields
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput


# custom bootstrap Data & Time picker fields
class DatePickerInput(DatePickerInput):
    format = '%d.%m.%Y'


class DateTimePickerInput(DateTimePickerInput):
    format = '%d.%m.%Y %H:%M'


TF_CHOICES = (
    ('5min', '5min'),
    ('15min', '15min'),
    ('30min', '30min'),
    ('1h', '1h'),
    ('4h', '4h'),
)

class ScanForm(forms.Form):
    timeframe = forms.ChoiceField(
        choices=TF_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}),
        required=True)


class TraidForm(forms.ModelForm):
    sell_perc_min = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    sell_perc_max = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Traid
        fields = ('coin', 'note')

        widgets = {
           'coin': forms.Select(attrs={'class':'form-control'}),
            # custom bootstrap Data & Time picker fields
#            'start_time': DateTimePickerInput(
#                attrs={'class': 'form-control',
#                       'placeholder': 'Entry'}
#            ),
#            'end_time': DateTimePickerInput(
#                attrs={'class': 'form-control',
#                       'placeholder': 'Exit'}
#            ),
            'note': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Note',
                       'rows': 4,
                       }
            ),
        }


    def __init__(self, *args, **kwargs):
        super(TraidForm, self).__init__(*args, **kwargs)
        self.fields['coin'].empty_label = "Coin"


class ReasonForm(ModelForm):
    class Meta:
        model = Reason
        fields = ('name', 'note',)


class EntryReasonForm(ModelForm):
    class Meta:
        model = EntryReason
        fields = ('reason',)

        widgets = {
            'reason': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reason'].empty_label = "Choose"


EntryReasonFormSet = inlineformset_factory(
    Traid, EntryReason, form=EntryReasonForm,
    fields=['reason'],
    extra=1, can_delete=True,)

