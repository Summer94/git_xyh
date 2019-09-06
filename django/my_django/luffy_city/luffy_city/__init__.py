from django.db.models.signals import pre_delete

def f1():
    print("在执行删除前打印")

pre_delete.connect(f1)