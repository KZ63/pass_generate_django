"""
Todo
✅記号
□パスワードの保存機能
□バックアップ取得（Excelでのダウンロード）
□レイアウト整形（bootstrap導入）
□テスト
"""
from django.shortcuts import render
import random
import string
from django.http import JsonResponse


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
