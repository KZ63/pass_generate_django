"""
Todo
✅記号
✅パスワードの保存機能
✅一覧表示
✅バックアップ取得（Excelでのダウンロード）
□レイアウト整形（bootstrap導入）
□テスト
□ログイン機能
"""
from django.shortcuts import render
import random
import string
import csv, urllib, datetime
from django.http import JsonResponse
from .forms import PassWordForm
from .models import PassWord
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'generate_app/index.html')


# パスワード生成_v1
# 数字8桁
def generate(request):
    password_list = []
    digit = int(request.POST.get('digit'))
    word = request.POST.get('word')
    chars = ''
    if 'upper' in word:
        chars += string.ascii_letters
    if 'number' in word:
        chars += string.digits
    if 'signal' in word:
        chars += string.punctuation
    for i in range(0, 10):
        password = ''.join([random.choice(chars) for i in range(digit)])
        password_list.append(password)
    return JsonResponse({
        "password_list": password_list
    })

# パスワード登録
def create(request):
    if request.method == 'POST':
        form = PassWordForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'generate_app/index.html')
    else:
        form = PassWordForm()
        return render(request, 'generate_app/pass_apply.html', {'form': form})

# パスワード一覧表示
def show_passwords(request):
    passwords = PassWord.objects.all()
    print(passwords)
    return render(request, 'generate_app/show_passwords.html', {'passwords': passwords})

# パスワード一覧エクスポート
def export_password(request):
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    export_datetime = datetime.datetime.now()
    str_export_datetime = export_datetime.strftime('%Y%m%d%H%M')
    f = 'パスワード一覧_' + str_export_datetime + '.csv'
    file_name = urllib.parse.quote((f).encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(file_name)
    writer = csv.writer(response)
    password_list = PassWord.objects.all()
    for password in password_list:
        writer.writerow([password.service_name, password.passWord, password.url])
    return response