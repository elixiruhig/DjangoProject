from django.test import TestCase

# Create your tests here.
import re
s = 'i like #teamIndia and #kohli'
arr = re.findall(r'#(\w+)',s)

for a in arr:
    print(a)