from django.test import TestCase
from googletrans import Translator
# Create your tests here.
class TstCase(TestCase):
    translator = Translator()
    ans = translator.translate("안녕하세요.")
    print(ans.text)