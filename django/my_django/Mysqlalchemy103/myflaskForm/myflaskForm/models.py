# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 16:25
# @Author  : summer
# @File    : models.py
# @Software: PyCharm

from myflaskForm import db
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType



# class Book(db.Model):
#     TYPE = [
#         (1, "科幻"), (2, "历史"), (3, "言情")
#     ]
#     __tablename__ = "book"
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(32), nullable=False)
#     price = Column(Float)
#     category = Column(ChoiceType(TYPE), default=1)
#     publisher_id = Column(Integer, ForeignKey("publisher.id"))
#     # 不生成字段建立关系 方便操作
#     # 一对多
#     publisher = relationship("Publisher", backref="books")
#     # 多对多
#     tags = relationship("Tag", secondary="book2tag", backref="books")
#
#     def __repr__(self):
#         return self.title
#
#     __table_args__ = (
#         # 联合唯一
#         UniqueConstraint("id", "title", name="uni_id_title"),
#         # 联合索引
#         Index("id", "title")
#     )
#
# class Publisher(db.Model):
#     __tablename__ = "publisher"
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(32), nullable=False)
#
#     def __repr__(self):
#         return self.title


class Tag(db.Model):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)

    def __repr__(self):
        return self.title


# class Book2Tag(db.Model):
#     __tablename__ = "book2tag"
#
#     id = Column(Integer, primary_key=True)
#     book_id = Column(Integer, ForeignKey("book.id"))
#     tag_id = Column(Integer, ForeignKey("tag.id"))
#
#     def __repr__(self):
#         return self.title