from django.shortcuts import render
from .forms import EncodeMessageForm
from .utils import encode_message

def encode_message_view(request):
    if request.method == 'POST':
        form = EncodeMessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            encoded_message = encode_message(message)
            return render(request, 'mains/result.html', {'encoded_message': encoded_message})
    else:
        form = EncodeMessageForm()

    return render(request, 'mains/encode_message.html', {'form': form})
