from django import forms

class EncodeMessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Message to Encode')
