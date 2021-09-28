
from typing import NamedTuple
from main.models import Chemical
from django.shortcuts import redirect, render

from .forms import ChemicalForm
from django.views.decorators.http import require_GET

from django.views.decorators.http import require_POST

from django.contrib import messages
from .forms import ChemicalModelForm

from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv
import io

from django.views.generic import ListView
from django.db.models import Q


#rdkitモジュール
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import rdDepictor




def list(request):
    chemicals = Chemical.objects.all()
    return render(request, 'main/list.html',{
        'chemicals':chemicals
    })


# 初期表示時に実行するビュー
def crud_new(request):
    form = ChemicalModelForm()
    return render(request, 'main/crud_new.html',{
        'form':form
    })
#ポスト時に実行するビュー
@require_POST
def crud_create(request):
    #a. フォーム経由でモデルを更新
    obj = Chemical()
    form = ChemicalModelForm(request.POST,instance=obj)
    if form.is_valid():
        form.save()
        #b. 成功メッセージを設定
        messages.add_message(request,messages.SUCCESS,'データの保存に成功しました。')
        #成功時は入力フォームにリダイレクト
        return redirect('list2')
    else:
        #失敗時は入力フォームを再表示
         return render(request, 'main/crud_new.html',{
            'form':form
        })



def list2(request):
    chemical_list = Chemical.objects.all()
    return render(request, 'main/list2.html', {
        'chemical':chemical_list
    })

def csvexport(request):
    response = HttpResponse(content_type='text/csv; charset=CP932')
    response['Content-Disposition']= 'attachment;  filename="somefilename.csv"'

    writer = csv.writer(response)
    for c in Chemical.objects.all():
        writer.writerow([c.name, c.SMILES, c.comment, c.boilingpoint, c.meltingpoint])
    return response

def csvimport(request):
    if 'csv' in request.FILES:
        data = io.TextIOWrapper(request.FILES['csv'].file, encoding='utf-8' )
        #print(data)
        csv_content= csv.reader(data)
        #print(csv_content)
        for i in csv_content:
            chemical, created = Chemical.objects.get_or_create(name= i[1])
            chemical.pk= i[0]
            chemical.name = i[1]
            chemical.SMILES = i[2]
            chemical.comment = i[3]
            chemical.boilingpoint= i[4]
            chemical.meltingpoint=i[5]
            chemical.save()
        return redirect('list2')
    else:
        return redirect('list2')


class ChemicalList(ListView):
    

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        
        if q_word is not None:
            object_list = Chemical.objects.filter(
                name=q_word
            )
            
            if object_list.exists():
                for c in object_list:
                    smiles = c.SMILES
                    named = c.name
                mol = Chem.MolFromSmiles(smiles)
                Draw.MolToFile(mol,f'main/static/image/{named}.png' )
                return object_list
            else:
                return Chemical.objects.none()
        else:
           
            return Chemical.objects.none() 


#トップページ
def top(request):
    return render(request, 'main/toppage.html')

import numpy as np 
from sklearn import datasets 
from sklearn.svm import SVR 
from sklearn.metrics import mean_squared_error, explained_variance_score 
from sklearn.utils import shuffle 


def test(request):
    
    
    return render(request, 'main/boston.html')

@require_POST
def test2(request):
    data = datasets.load_boston() 
    X, y = shuffle(data.data, data.target, random_state=7) 

    num_training = int(0.8 * len(X)) 
    X_train, y_train = X[:num_training], y[:num_training] 
    X_test, y_test = X[num_training:], y[num_training:] 

    sv_regressor = SVR(kernel='linear', C=1.0, epsilon=0.1) 
    sv_regressor.fit(X_train, y_train) 

    y_test_pred = sv_regressor.predict(X_test) 
    mse = mean_squared_error(y_test, y_test_pred) 
    evs = explained_variance_score(y_test, y_test_pred) 
    test_data=request.POST.getlist("office")
    price = sv_regressor.predict([test_data])[0]
    context={'price':price}
    
    return render(request, 'main/boston_result.html', context)