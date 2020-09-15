from django.shortcuts import render
from . import forms
from index.views import index

# Create your views here.
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form=forms.FormName(request.POST)

    if form.is_valid():
        new_contact = form.save(commit=True)
        return index(request)

    return render(request,'form2/form2.html',{'form':form})
