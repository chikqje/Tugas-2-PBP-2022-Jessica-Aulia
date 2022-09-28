from django import forms

# membuat form class
class CreateTaskForm(forms.Form):
    judul_task = forms.CharField(label='Judul', max_length=100)
    deskripsi_task= forms.CharField(label='deskripsi', max_length=100)