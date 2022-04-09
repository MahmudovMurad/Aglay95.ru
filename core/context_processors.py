from core.form import SubscribeForm
from core.models import Subscriber


def subscribe(request):
    form = SubscribeForm(request.POST or None)
    if request.method == "POST" :
        if  form.is_valid():
            form.save()
    return {'subscriber_form' : form}
