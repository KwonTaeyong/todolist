from django import forms


class TodoCreateForm(forms.Form):
    name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': '해야할일',
            }
        )
    )

    description = forms.CharField(
        max_length=200,
        widget=forms.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': '할일에 대한 디테일',
            }
        )
    )

    date_deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'id': 'datepicker',
                'placeholder': 'YYYY-MM-DD',
            }
        )
    )

    images = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
                'class': 'file-input',
            }
        ), required=False,
    )

    files = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
                'class': 'file-input',
            }
        ), required=False,
    )
