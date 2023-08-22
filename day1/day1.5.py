'''
列表
列表由一系列按特定顺序排列的元素组成。
你可以创建包含字母表中所有字母，数字0-9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，
其中的元素之间可以没有任何关系。

在Python中，用方括号[]来表示列表，并用逗号来分隔其中的元素。
'''
qingshan =['wuhu','123','qifei']
print(qingshan);

'''
访问列表元素
列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉pyhon即可。
要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内
'''
qingsan = ['草木有本心','何求美人折','落霞与孤鹜齐飞','秋水共长天一色']
print(qingsan[0])
print(qingsan[1])
print(qingsan[2])
print(qingsan[3])

'''
在python中，第一个列表元素的索引为0，而不是1
第二个列表元素为1。根据这种简单的计数方式，要访问列表的任何元素，都可将其位置减一，并将其
结果作为索引。
python为访问最后一个列表元素提供了一种特殊语法。
通过将索引指定为-1，可让python返回最后以恶搞列表元素.
这种语法也可适用于其他负数索引，
'''
print(qingsan[-1])
print(qingsan[-2])
print(qingsan[-3])
print(qingsan[-4])

'''
可以像使用其他变量一样使用列表中的各个值。
'''

message = 'qingshan:'+qingsan[0]+','+qingsan[1]+'。'
print(message)

'''
你创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。
例如：你创建一个游戏，要求玩家射杀从天而降的外星人；
为此，可在开始时将一些外星人存储在列表中，然后每当有外星人被射杀时，都将其从列表中删除
而每次有新的外星人出现在屏幕上时，都将其添加到列表中。
在整个游戏运行期间，外星人列表的长度将不断变化
'''

'''
修改列表元素
修改列表元素的语法与访问列表元素的语法类似。
要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
'''
#例
axs = ['落红不是无情物','化作春泥更护花']
print(axs[0])
axs[0] = '醉后不知天在水'
axs[1] = '满船清梦压星河'
print(axs[0]+','+axs[1])

'''
在列表中添加元素
1.在列表末尾添加元素
使用append()方法可以将新的元素添加到列表末尾，并且不影响列表的其他元素
也可以创建一个空列表，再使用一系列的append（）语句添加元素
列表中元素的顺序与你加如的顺序一致
'''
axs.append('那时那日此门中')
print(axs)
a1 = []
a1.append('那时那日此门中')
a1.append('桃花树下初相逢')
print(a1)

'''
在列表中插入元素
使用方法insert()可在列表的任何位置添加新元素。
为此，你需要指定新元素的索引和值
'''
a2 = ['1','2','3']
print(a2)
a2.insert(0,'4')
print(a2)

'''
从列表中删除元素
1.使用del方法删除元素
如果知道要删除的元素在列表中的位置，可使用del语句。
del可以删除任何位置处的列表元素，条件是知道其索引。
'''
a3 = ['1','2','3']
print(a3)
del a3[0]
print(a3)

'''
使用pop()删除元素
使用pop删除后可以继续使用该值，但是列表中不可见
pop也可根据索引删除特定的值
'''
a4 = ['1','2','3']
b1 = a4.pop()
b2 = a4.pop(0)
b3 = a4.pop(0)
print(a4)
print(b1)
print(b2)
print(b3)

'''
remove函数可以根据值来删除,但是只能删除一个，如果值在列表中多次出现就需要循环
'''
a5 = ['1','2','3']
a5.remove('1')
print(a5)

'''
列表排序
sort（）函数可以将列表按照首字母排序
可以在括号里增加reverse=True使列表按照字母相反排序
sort的排序是永久性改变的
'''

a6 = ['dog','ogp','jdg','abf']
a6.sort()
print(a6)
a7 = ['dog','ogp','jdg','abf']
a7.sort(reverse=True)
print(a7)

'''
sorted()函数可以对列表进行临时排序
'''
a8 = ['dog','ogp','jdg','abf']
print(sorted(a8,reverse=True)) #传递reverse=True可以使列表按照与字母顺序相反的顺序排列
print(a8)

'''
倒着打印列表
要反转列表元素的顺序，可使用方法reverse（）
reverse只是反转列表元素的顺序
'''
a9 = ['dog','ogp','jdg','abf']
a9.reverse()
print(a9)
'''
函数len（）可以获取列表的长度
'''
a10 = ['dog','ogp','jdg','abf']
print(len(a10))

'''
使用for循环遍历整个列表
title的作用是使元素第一位变为大写
\n表示换行
'''
w1s = ['a','e','s','c','v']
for w1 in w1s:
    print(w1.title()+" wuhu")
    print("qsxff"+"\n")
print('这行代码会在for循环后执行一次')

'''
使用函数range()可以生成一系列的数字
可以使用range创建一个数字列表
创建列表时也可以进行运算
min:最小值
max：最大值
sum：求和
'''
for i in range(1,5):    #range指挥打印1，2，3，4不会打印5
    print(i)
numbers = list(range(1,5))
print(numbers)
n1 = list(range(2,11,2))       #这行代码表示从2开始打印，每次+2，再等于或大于11时停止
print(n1)
n2 = []
for i in range(1,11):
    q = i**2
    n2.append(q)
print(n2)
print(min(n2))
print(max(n2))
print(sum(n2))
'''
列表解析
前面的生成列表需要三四行代码，接下来只需一行就能生成上面的列表
'''
n3 = [i**2 for i in range(1,11)]
#使用这样的语法需要先指定一个列表名，然后指定一个放扩号，之后定义一个表达式
#接下来写for循环，在这行代码中，i**2即为表达式
print(n3)

'''
切片：要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
与函数range（）一样，python在到达你指定的第二个索引前面的元素后停止。
要输出列表的前三个元素，需要指定索引0-3，这将输出分别为0，1，2的元素
不指定第一个索引时，python将从列表开头开始提取
不指定最后一个索引时，python将在最后一个元素处结束
也可用负数，当前面为负数时即为倒数元素，当后面为负数时为正数元素
'''
n4 = ['a','w','s','f','c']
print(n4[0:3])
print(n4[:2])
print(n4[2:])
print(n4[-3:])
'''
遍历切片
如果要遍历列表的部分元素，可在for循环中使用切片
'''
for i in n4[0:3]:
    print(i.title())
n14 = n4[0:3]
n14.append('v')
print(n14)
'''
列表非常适合用于存储在程序运行期间可能变化的数据集。
列表是可以修改的
元组是不可修改的
Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
元组看起来犹如列表，但使用圆括号而不是放括号来标识。
定义元组后，可以使用索引来访问其元素。
'''

c1 = (2,5)
print(c1[0])
print(c1[1])
#遍历元组
for i in c1:
    print(i)
c1 = (3,4)
for i in c1:
    print(i)