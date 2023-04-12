from django.urls import resolve
from django.test import TestCase
from .models import PassWord
from .views import index, show_passwords, create, delete, export_password
from django.http import HttpRequest
from django.template.loader import render_to_string
 
# Create your tests here.
class PassWordTestCase(TestCase):

      def setUp(self):
            obj = PassWord(service_name='Test', passWord='pass', url='https//google.com')
            obj.save()

      """オブジェクトが作成されることの検証"""
      def test_object_saved(self):
            count = PassWord.objects.count()
            self.assertEquals(count, 1)
      
      # urlテスト
      """/homeではindex関数が呼び出されることを検証"""
      def test_url_home(self):
            found = resolve('/home')
            self.assertEquals(found.func, index)
      
      """/show_passwords/ではshow_passwords関数が呼び出されることを検証"""
      def test_url_show_passwords(self):
            found = resolve('/show_passwords/')
            self.assertEquals(found.func, show_passwords)
      
      """/create/ではcreate関数が呼び出されることを検証"""
      def test_url_create(self):
            found = resolve('/create/')
            self.assertEquals(found.func, create)
      
      """/delete/1ではdelete関数が呼び出されることを検証"""
      def test_url_delete(self):
            found = resolve('/delete/1')
            self.assertEquals(found.func, delete)
      
      """/export_passwordではexport_password関数が呼び出されることを検証"""
      def test_url_export_password(self):
            found = resolve('/export_password')
            self.assertEquals(found.func, export_password)