'''
集合 set
集合是一个无序的不重复元素序列
集合中的元素不回重复，并且可以进行交集，并集，差集等常见的集合操作
可以使用大括号{}创建集合，元素之间用逗号，分隔，也可以用set()函数创建集合
创建格式    
a1 = {val1,val2,...}
set(value)
'''

set1 = {1,2,3,4,5}
set2 = set([9,8,7,6])


#创建一个空集合必须用set（），不能用{}，因为{}是用来创建字典的

set_shili = {'ab','cd','ab','cd'};
print(set_shili)      #去重

if 'ab' in set_shili:
    print('T');
else:
    print('F');
if 'ae' in set_shili:
        print('T')
else:
        print('F')

set_1 = set('alkmxinnaa')
set_2 = set('alkuyex')
print(set_1);
print(set_1-set_2);   #集合set_1中包含但是集合set_2中不包含的元素
print(set_1 | set_2);    #并集    集合set_1  set_2中的所有元素
print(set_1 & set_2);   #交集     集合set_1  set_2中共有的元素
print(set_1 ^ set_2);   #差集     集合set_1  set_2中独有的元素

a = {x for x in 'asdfgvhj' if x not in 'asd'};
print(a)

'''
集合添加元素
    1.格式  ：     a.add(x)
将元素x添加到集合a中，如果元素已经存在，则不进行任何操作
2.    q.update(x)       参数可以是列表，元组，字典等
'''

set_add = set('axscd')
set_add.add('xs')
set_add.add('x')
print(set_add);
set_add.update([1,2],[3,4]);
print(set_add)
set_add.update({5,6})
print(set_add)

'''
集合删除元素
1.s.remove(x)         将x从集合s中删除，如果元素不存在，则会报错
2.s.discard(x)         将x从集合s中删除，元素不存在也不会报错
3.s.pop(x)            随机删除集合中的一个元素。    set中的pop方法会对集合进行无序的排列，然后将这个无序排列的集合的左面第一个元素删除
'''

set_shanchu = set('abcd');
set_shanchu.remove('a')
#set_shanchu.remove('q')   会报错
print(set_shanchu);
set_shanchu.discard('c')
set_shanchu.discard('q')           #不会报错
print(set_shanchu);
x = set_shanchu.pop()
print(x)

'''
计算集合中元素个数
len（s)
'''
set_len = set('1dsada3')
print(len(set_len))
'''
清空集合
s.clear()
'''
set_clear = set('qwer')
set_clear.clear()
print(set_clear)


if x in set_clear:
    print(True)
else:
    print(False)

'''
集合内置元素
set.add()    添加元素
set.clear()   清空集合中的所有元素
set.copy()   拷贝一个集合
set.difference()   返回多个集合的差集
set.difference_update()  	移除两个集合中都存在的元素
set.discard()  删除集合中指定的元素
set.intersection()   返回集合的交集
set.intersection_update()   返回集合中的交集
set.isdisjoint()     判断两个集合是否包含相同的元素
set.issubset()     判断集合的所有元素是否都包含在指定集合中
set.issuperset()       判断集合的所有元素是否都包含在指定集合中
set.pop()      随机删除一个集合中的元素
set.remove    删除指定的元素
set.symmetric_difference()    返回两个集合中不重复的元素，移除两个集合中都存在的元素
set.symmetric_difference_update()    一处当前集合中在另一个集合中存在的元素，并将另一个集合中不同的元素插入到当前集合中
set.union()     返回两个集合的并集
set.update()    添加元素
len（set）   计算集合元素个数
'''