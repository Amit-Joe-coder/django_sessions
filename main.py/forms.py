class bf_form(forms.Form):
    bname=forms.CharField()

class gf_form(forms.Form):
    gname=forms.CharField()

class age_form(forms.Form):
    age=forms.IntegerField()
