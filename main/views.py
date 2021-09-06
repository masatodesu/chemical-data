
from main.models import Chemical
from django.shortcuts import redirect, render

from .forms import ChemicalForm
from django.views.decorators.http import require_GET

from django.views.decorators.http import require_POST

from django.contrib import messages
from .forms import ChemicalModelForm

from django.http import HttpResponseRedirect
from django.http import HttpResponse
import csv, io

def index(request):
    context ={
        'msg':'Hello World'
    }

    return render(request, 'main/index.html', context)


def list(request):
    chemicals = Chemical.objects.all()
    return render(request, 'main/list.html',{
        'chemicals':chemicals
    })



def form_input(request):
    #a. フォームオブジェクトを生成
    form = ChemicalForm()
    return render(request, 'main/form_input.html',{
        'form':form
    })

#a. HTTP POSTでのみ実行されるビュー関数
@require_POST
def form_process(request):
    #b. ポストデータを紐付け
    form = ChemicalForm(request.POST)
    #c. 入力値を検証
    if form.is_valid():
        # 正しければ結果を表示
        return render(request,'main/form_process.html',{
            'form':form
        })
    else:
        # 誤りがあればフォームを再描画
        return render(request,'main/form_input.html',{
            'form':form
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
        print(data)
        csv_content= csv.reader(data)
        print(csv_content)
        for i in csv_content:
            chemical, created = Chemical.objects.get_or_create(name= i[1], SMILES= i[2], comment=i[3], boilingpoint=i[4], meltingpoint=i[5])
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
