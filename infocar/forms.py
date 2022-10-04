from  django import forms

from .models import Auto,Engine,Transmission,Complectation


class AddFormAuto(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['engine'].empty_label = 'Двигатель не выбран' # вместо прочерков в форме будет запись
        self.fields['transmission'].empty_label = 'Трансмиссия не выбрана'

    class Meta:
        model = Auto
        fields = ['firm','model','engine','volume','transmission','color','price','complectations','image'] # выбирает все поля формы , если не нужно прописываем в кортеже


class FilterAutoForm(forms.Form):
    engine = forms.ModelChoiceField(queryset=Engine.objects.all(), label='Двигатель', empty_label='не выбран')
    transmission = forms.ModelChoiceField(queryset=Transmission.objects.all(), label='Коробка', empty_label='не выбран')
# class AddFormsAuto(forms.Form):
#     firm = forms.CharField(max_length=150,label='Фирма')
#     model = forms.CharField(max_length=150,label='Модель')
#     color = forms.CharField(max_length=50,label='Цвет')
#     engine = forms.ModelChoiceField(queryset=Engine.objects.all(),label='Двигатель',empty_label= 'не выбран')
#     volume = forms.FloatField(step_size=0.1,label='Обьём')
#     transmission = forms.ModelChoiceField(queryset=Transmission.objects.all(),label='Коробка',empty_label='не выбран')
#     price = forms.IntegerField(label='Цена')