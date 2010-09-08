from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django import forms

interests = ["New Tech","Activism","Radio","Lockpicking","Crypto","Privacy","Ethics","Telephones","Social Engineering",
             "Hackerspaces","Hardware Hacking", "Nostalgia", "Communities", "Science", "Government", "Network Security",
             "Malicious Software", "Pen Testing", "Web", "Niche Hacks", "Media"]

class ProfileForm(forms.Form):
    handle = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    userpic = forms.FileField(label="Choose Userpic:")
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=[['M','Male'],['F','Female'],['O','Other']])
    age = forms.IntegerField(required=False)
    home_loc = forms.CharField(label="Home Location")
    interests = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                        choices=zip(range(len(interests)),interests))

def profile(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            return HttpResponseRedirect('/profile/')
    else:
        form = ProfileForm( initial={} )
    return render_to_response('profile_edit.html', 
                              RequestContext(request,{'form': form}))
