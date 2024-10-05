from django import forms

from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        exclude=['roll']
        # fields=['name','roll','address']


        labels={
            'name':'Student_Name',
            'roll':'Student_Roll'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'btn-primary'}),
            # 'roll':forms.PasswordInput()
        }

        help_texts={
            'name':"Write Your Full Name"
        }

        error_message={
            'name':{'required':'Your Name Is Required'}
        }
