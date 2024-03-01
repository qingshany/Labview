'''
元组
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组/tuple使用小括号(),列表list使用方括号[].
元组创建很简单，只需要在括号中添加元素，并且使用逗号隔开即可。
'''

#tuple实例
tup1 = ('chrome','list','str','int','dict','1','2.98')
tup2 = (1,2,3,4,5)
tup3 = "a","b","c","d"         #不需要括号也可以
print(type(tup3));
print(type(tup2));
print(type(tup1));

tup_kong = ();     #创建空元组

'''
元组中只包含一个元素时，需要是元素后面假逗号，否则括号会被当作运算符使用；
'''

typ1 = (50);
print(type(typ1));
typ2 = (50,);
print(type(typ2));
'''
元组与字符串类似，下标索引从0开始，可以进行截取，组合等操作。
访问元组中的值可以使用下标索引取值
'''


tup_suoyin = ('list','tupe','dict','1','2.3')
print(tup_suoyin[0]);
print(tup_suoyin[1]);
print(tup_suoyin[2]);
print(tup_suoyin[3]);
print(tup_suoyin[4]);
print(tup_suoyin[-5]);
print(tup_suoyin[-4]);
print(tup_suoyin[-3]);
print(tup_suoyin[-2]);
print(tup_suoyin[-1]);
print(tup_suoyin[1:5]);
print(tup_suoyin[2:5]);
print(tup_suoyin[-5:-2]);
print(tup_suoyin[-3:-1]);
print(tup_suoyin[-5:]);

'''
元组中的元素时不允许修改的，但我们可以对元组进行链接组合
'''

tup_lianjie1=(1,2,3)
tup_lianjie2=('a','c','v')

#tup_lianjie1[0]=100     这样对元组进行修改是非法的

tup_lianjie3 = tup_lianjie1 + tup_lianjie2
print(tup_lianjie3)


'''
元组中的元素值是不允许删除的，但是我们可以使用del语句来删除整个元组
'''

tup_del = ('1','a','r','sdf')
print(tup_del)
del tup_del
#print(tup_del)

'''
元组内置函数
len           计算元素个数
max           返回元组中的最大值
min           返回元组中的最小值
tuple         强制转换为元组
'''
list1 = [1,2,3,4]
tup_hanshu = ('1','2','3')
print(len(tup_hanshu))
print(max(tup_hanshu))
print(min(tup_hanshu))
print(tuple(list1))

'''
元组运算符
元组之间可以使用 + += * 进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组
'''

tup_jia1 = (1,2,3)
tup_jia2 = (4,5,6)
tup_jia3 = tup_jia1 + tup_jia2
print(tup_jia3);
print(id(tup_jia1))   # 此处与下面所指向的内存地址不一样
#id函数   返回所指向参数的内存地址
tup_jia1 += tup_jia2
print(tup_jia1)
print(id(tup_jia1))

tup_cheng = tup_jia1 * 4
print(tup_cheng);

if 3 in tup_jia1:
    print("Ture")
else:
    print('Flase')


for x in tup_jia1:
    print(x, end=" ")


'''
关于元组的不可变指的是元组所指向的内存中的内容不可变
'''