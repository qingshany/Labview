'''
程序的流程控制使用if语句
'''
#if语句，简单实例：
ShouJ = ['vivo','huawei','xiaomi','iphone','sanxing',]     #创建一个列表
for shouj in ShouJ:                       #循环遍历列表
    if shouj == 'huawei':                 #是否等于华为
        print(shouj.upper())              #等于的话全部大写输出
    else:                                  #其他的则只有首字母大写
        print(shouj.title())

'''
每条if语句的核心都是一个值为True或Flase的表达式。
这种表达式被称为条件测试。
python根据条件测试的值为True还是Flase来决定是否执行if语句中的代码。
如果条件测试的值为True，python就执行紧跟在if语句后面的代码；如果为Flase，python就忽略这些代码
1.可以使用and检查多个条件，只有多个条件都为TRUE时才会执行if中的代码
2.可以使用or检查多个条件，只要有一个条件满足就可通过，只有全部为flase的时候测试才会fail
3.可以使用in来检查某个值是否在某个列表内
4.可以使用not in 来检查某个值是否不在某个列表内
'''
iteam = ['li','qingshan','wuhu']
for i in iteam:
    if 'qingshan' in iteam:
        print("芜湖~！")
    if 'cool' not in iteam:
        print("啧！")


for i in range(3):
    a = 9
    print(a)

'''
布尔表达式：它不过是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为True，要么为False。
布尔值通常用于记录条件，如用户是否可以编辑网站的特定内容：
在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式。
'''


'''
简单的if语句
最简单的if语句只有一个测试和一个操作：
if  条件语句：
    do   something
在第一行中，可以包含任何条件测试，而在紧跟在测试后面的缩进代码块里，可执行任何操作

if-else：
在条件测试通过了时执行一个操作，没有通过时执行另一个操作。
在这种情况可以使用if，else语句
'''

arge = 14
if arge >=15:
    print(1)
else:
    print(2)


'''
if-elif-else
这个格式用来处理多个条件测试
如果if不符合则判断elif的条件，如果elif不符合则判断else的条件
if和else在一个条件测试中只能分别存在一个，但是elif可以存在多个
Python并不要求if-elif结构后面必须有else代码块。在有些情况下，else代码块很有用；而
在其他一些情况下，使用一条elif语句来处理特定的情形更清晰：
else是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行，
这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif代码块来
代替else代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。
'''

arge1 =  19
if arge1 < 19:
    print(1)
elif arge1 >= 19  and arge1 < 60:
    print(2)
elif arge1 >=60 and arge1 <90:
    print(3)
else:
    print(4)


'''
if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，
Python就跳过余下的测试。这种行为很好，效率很高，让你能够测试一个特定的条件。
然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含elif和else
代码块的简单if语句。在可能有多个条件为True，且你需要在每个条件为True时都采取相应措施
时，适合使用这种方法。
'''
tang = ['杜甫','李白','李商隐']
if '杜甫' in tang:
    print(1)
if '李白' in tang:
    print(2)
if '李商隐' in tang:
    print(3)
print("盛唐")

if '杜甫' in tang:
    if '李白' in tang:
        if '李商隐' in tang:
            print('盛唐')



k = ['1','2','3','李白'];
if k:
    print(1)
else:
    print(2)

for i in k:
    if i in tang:
        print(1)
    else:
        print(2)
