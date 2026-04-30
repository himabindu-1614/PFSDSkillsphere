from django import forms
from .models import Certificate


class CertificateForm(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = [
            'title',
            'issuer',
            'category',
            'issue_date',
            'expiry_date',
            'certificate_file'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder':'Certificate Title'}
            ),

            'issuer': forms.TextInput(
                attrs={'placeholder':'Organization'}
            ),

            'category': forms.Select(choices=[
                ('Cloud Computing','Cloud Computing'),
                ('Artificial Intelligence','Artificial Intelligence'),
                ('Machine Learning','Machine Learning'),
                ('Data Science','Data Science'),
                ('Cyber Security','Cyber Security'),
                ('Blockchain','Blockchain'),
                ('Web Development','Web Development'),
                ('AWS','AWS'),
                ('DevOps','DevOps'),
            ]),

            'issue_date': forms.DateInput(
                attrs={'type':'date'}
            ),

            'expiry_date': forms.DateInput(
                attrs={'type':'date'}
            ),
        }