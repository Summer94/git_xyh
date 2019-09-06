# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 19:35
# @Author  : summer
# @File    : my_paginatons.py
# @Software: PyCharm


class Pagination():
    def __init__(self, current_page, total_count, per_page=10, show_page=9):
        """

        :param current_page: 当前的页数
        :param total_count:  总共的数据的数量(条数)
        :param per_page: 每页显示多少条数据
        :param show_page: 每次显示多少页
        """
        # 获取当前页数
        try:
            # 当输入的值不是数字的时候，当前页默认为1
            current_page = int(current_page)
        except Exception as e:
            current_page = 1
        # 不能是负数
        if current_page < 1:
            current_page = 1

        # 每页显示10条数据
        self.per_page = per_page
        # 计算有多少页
        total_page, more = divmod(total_count, per_page)
        # 如果有余数，那么页数加一
        if more:
            total_page += 1
        self.total_page = total_page
        # 如果访问的页码数超过了总页码数，默认展示最后一页
        current_page = total_page if current_page > total_page else current_page
        self.current_page = current_page
        # 每次显示多少页
        self.show_page = show_page
        # 显示页数的一半的页数
        self.show_half_page = self.show_page // 2
        # 如果总页数小于显示页数
        if self.total_page < self.show_page:
            self.show_page = self.total_page

    # 数据切片的开始位置
    @property
    def start(self):
        return self.per_page * (self.current_page - 1)

    # 数据切片的结束位置
    @property
    def stop(self):
        return self.per_page * self.current_page

    # 定义一个返回HTML代码的方法
    def page_html(self):
        # 显示页数
        # 如果显示的总页码小于要显示的页码
        if self.current_page > self.total_page:
            show_page_start = 1
            show_page_stop = self.per_page
        # 防止左边页面溢出
        elif self.current_page <= self.show_half_page:
            show_page_start = 1
            show_page_stop = self.show_page
        # 防止右边页面溢出
        elif self.current_page + self.show_half_page > self.total_page:
            show_page_stop = self.total_page
            show_page_start = self.total_page - self.show_page + 1
        else:
            # 显示页数的开始
            show_page_start = self.current_page - self.show_half_page
            # 显示页数的结束
            show_page_stop = self.current_page + self.show_half_page
        # 生成html代码
        page_html_list = []
        # 代码的前缀
        page_html_list.append('<nav aria-label="Page navigation"><ul class="pagination">')
        # 添加首页
        page_html_list.append('<li><a href="/publisher/?page=1">首页</a></li>')
        # 添加上一页
        if self.current_page - 1 < 1:  # 已经到头啦，不让点上一页啦
            page_html_list.append(
                '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            page_html_list.append(
                '<li><a href="/publisher/?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.current_page - 1))
        for i in range(show_page_start, show_page_stop + 1):
            if i == self.current_page:
                a = '<li class="active"><a href="/publisher/?page={0}">{0}</a></li>'.format(i)
            else:
                a = '<li><a href="/publisher/?page={0}">{0}</a></li>'.format(i)
            page_html_list.append(a)
        # 添加下一页
        if self.current_page + 1 > self.total_page:
            page_html_list.append(
                '<li class="disabled"><a href="" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            page_html_list.append(
                '<li><a href="/publisher/?page={}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.current_page + 1))

        # 添加尾页
        page_html_list.append('<li><a href="/publisher/?page={}">尾页</a></li>'.format(self.total_page))
        # 给代码增加后缀
        page_html_list.append('</ul></nav>')
        page_html = "".join(page_html_list)
        return page_html
