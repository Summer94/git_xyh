# 引用计数主  标记清除和分代回收 辅助
# Python对象和引用是分离的

a = [1, 2, 3]
b = a
c = [a, 6]
del b
# 引用计数
from sys import getrefcount
print(getrefcount(a))
# python内部维护一个对象的时候会维护一个引用计数
# 当引用计数为0的时候就表示是垃圾 要清楚
d = [1,2,3]
f = [4,5,6]
d.append(f)
f.append(d)
# 循环引用是引用计数一个bug
# 标记清除
# 把全局变量 标记成根节点
# 找到所有可达对象 不可达就是垃圾
# 标记清除的效率问题
# 分代回收
# 0代 年轻的一代 链表
# 域值（700， 10， 10）
# 0代被触发回收之后没有被回收的对象放入1代
# 0代被回收10次的时候触发1代回收
# 1代没有被回收对象放入2代
# 1代触发10次的时候触发2代回收












