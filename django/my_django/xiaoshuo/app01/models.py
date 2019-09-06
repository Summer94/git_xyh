from django.db import models

# Create your models here.

#小说分类排行榜
#如 都市，修真，玄幻，武侠，历史
class NovelRanking(models.Model):
    name = models.CharField(max_length=64, verbose_name='分类名称')
    pic = models.CharField(max_length=128, verbose_name='图片地址')


#作者
class Author(models.Model):
    name = models.CharField(max_length=64, verbose_name='作者姓名')


#小说
class Novel(models.Model):
    name = models.CharField(max_length=64, verbose_name='小说书名')
    author = models.ForeignKey(to='Author',verbose_name='作者', related_name='novels')
    pic = models.CharField(max_length=128, verbose_name='小说封面地址')
    introduction = models.CharField(max_length=128, verbose_name='小说简介')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='小说创建日期')
    update_time = models.DateTimeField(auto_now=True, verbose_name='小说更新日期')
    class Meta:
        unique_together = ('name', 'author') #小说名与作者联合唯一，即不能重复写入同一个作者的同一本书

#小说的章节与具体内容
class NovelChapter(models.Model):
    name = models.CharField(max_length=64, verbose_name='小说章节名称')
    novel = models.ForeignKey(to='Novel', related_name='chapters', verbose_name='相关联的小说')
    contain = models.TextField(verbose_name='章节内容')





