"""
Todo
✅記号
✅パスワードの保存機能
✅一覧表示
✅バックアップ取得（Excelでのダウンロード）
✅ログイン機能
- ✅画面の実装
- ✅パスワードのハッシュ化
✅削除機能
□レイアウト整形（bootstrap導入）
□テスト
"""
from django.shortcuts import render
import random
import string
import csv, urllib, datetime
from django.http import JsonResponse
from .forms import PassWordForm
from .models import PassWord
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import AccountForm, AddAccountForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == 'POST':
        Id = request.POST.get('userid')
        Pass = request.POST.get('password')

        user = authenticate(username = Id, password = Pass)
        print(user)
        if user:
            if user.is_active:
                print('active')
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('アカウントが有効ではありません。')
        else:
            return HttpResponse('ログインIDまたはパスワードが間違っています。')
    else:
        return render(request, 'generate_app/Login.html')

@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login'))

# Create your views here.
@login_required
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
        # form.user_id = request.user.id
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'generate_app/index.html')
    else:
        form = PassWordForm()
        return render(request, 'generate_app/pass_apply.html', {'form': form})

# パスワード一覧表示
@login_required
def show_passwords(request):
    passwords = PassWord.objects.all()
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

@login_required
def delete(request, id):
    delete_target = PassWord.objects.filter(id=id)
    try:
        delete_target.delete()
        return HttpResponseRedirect(reverse('show_passwords'))
    except Exception as e:
        print(e)


class AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
            "AccountCreate": False,
            "account_form": AccountForm(),
            "add_account_form": AddAccountForm(),
        }
    
    def get(self, request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request, "generate_app/register.html", context=self.params)
    
    def post(self, request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            account = self.params["account_form"].save()
            account.set_password(account.password)
            account.save()

            add_account = self.params["add_account_form"].save(commit=False)
            add_account.user = account

            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']
            
            add_account.save()

            self.params["AccountCreate"] = True
        else:
            print(self.params["account_form"].errors)
        
        return render(request, "generate_app/register.html", context=self.params)