from django.test import TestCase

# Create your tests here.

import os
from app01 import models

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day86_vue.settings")
    import django
    django.setup()
    obj = models.Author.objects.first()
    print(obj)


