# 列表推导式
x = [1,2,3,4,5,6,7,8,9]
print([i*10 for i in x if i%2==0])

#==========(1)树=======================================
# 树的构造
def tree(root_label, branches=[]):
    '''构造函数tree():定义树的结构'''
    for branch in branches:
        assert is_tree(branch),'分支必须是树'
    return [root_label]+list(branches)  
'''一开始看到这里和后面一部分的时候,如果输入的branches是列表的话,以为用了list()之后
    会给branches再套一层[],然后感觉示例给的输出不对。现在尝试了加和不加list,发现输出的结果是一致的.
    再比如这个例子:list([[1],[1]]),输出的结果是[[1], [1]],和list里的一样.也就是说如果里面是列表的话,保持不变.
    list()可以把一个可迭代器变成一个列表.''' 

# 树的结构的选择
def label(tree):
    '''选择器label():选择树的根节点'''
    return tree[0]

def branches(tree):
    '''选择器branches():选择树的分支'''
    return tree[1:]

# 树的结构的判定
def is_tree(tree):
    '''判断输入是否是树（是否是结构良好的树）'''
    if type(tree) != list or len(tree) < 1:  # 输入类型为列表且长度大于等于1
        return False
    for branch in branches(tree):   # 检查输入的tree的所有分支是否是树，使用递归
        if is_tree(branch)==False:   # 或者 if not is_tree(branch):   
            return False
    return True

def is_leaf(tree):
    '''判断一个树是否是叶子节点:如果没有分支就是叶子节点'''
    return not branches(tree) 
'''本来以为会报错,因为觉得如果列表只有一个元素,那tree[1:]可能会因为超出索引而报错.尝试运行后发现没有报错.
a = [1] , a[1:]会输出空列表[](对应的bool型是False),而直接选择1号索引,a[1]会报错.'''

# 树的操作

## 树递归
def fib_tree(n):
    if n == 0 or n == 1:   # Base case:n为0或1时,递归调用停止
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1) # 左右分支:斐波那契数列原理,左右分支分别为斐波那契数列中前两位组成
        fib_n = label(left)+label(right)           # 第n位斐波那契数列值为左右分支根节点值的和
        return tree(fib_n, [left,right])

def count_leaves(tree):  # 计算tree的叶子树
    if is_leaf(tree):    # base case
        return 1
    else:
        branch_count = [count_leaves(branch) for branch in branches]  # 用列表推导式+递归,计算每个分支所含叶子树
        return sum(branch_count)
    
## 分割树 -- 1.7recursion.py 分割数
def partition_tree(n,m):
    '''返回将n分割成不超过m的若干正整数之和的分割数
    左分支:partition_tree(n-m,m),表示将n分割出一块m后,剩下的部分继续用不超过m的数分割
    右分支:partition_tree(n,m-1),表示不直接将n分割出一块m,而是将n用不超过m-1的数分割,为后续在左分支分割出一块m-1做铺垫
    叶子节点判断该次分割是否成功,成功则为True,反之
    根节点表示本次不超过的数 m '''
    if n==0:
        return tree(True)    # 这里别忘了加tree().不是返回True值,而是返回列表,元素为True
    elif n<0 or m==0:
        return tree(False)
    left = partition_tree(n-m,m)
    right = partition_tree(n,m-1)   # 二叉树
    return tree(m,[left,right])

def print_parts(tree,partition=[]):
    '''用分割树打印每一种分割方式
    画树的图更好理解,往左走将根节点算入分割部分(partition),当走到True时,说明正好把n分割至0,输出分割方式,走到False说明不能恰好分割;
    往右走用只将m变小(减1)'''
    if is_leaf(tree):   
        if label(tree):   # 是叶子节点并且叶子节点的值为True(即分割成功)
            print(' + '.join(partition))   # 格式化输出:将partition中的元素用'+'连接起来
    else:
        left,right = branches(tree)   # 二叉树
        m = str(label(tree))     # 这里要加str,join只能把字符串连接起来
        print_parts(left,partition+[m])  # 因为左分支将n分割出一块m出来,因此partition要加[m],在递归调用终点要打印出来
        print_parts(right,partition)     # 右分支只是为之后用更小的m-1来尝试分割n做铺垫(该右分支之后的左分支),因此这里partition不加[m]

print_parts(partition_tree(6,4))

## 二叉树
def right_binarize(tree):    
    '''根据tree构造一个右分叉的二叉树'''
    if isinstance(tree, int) or len(tree) == 1: # Fixbug:isinstance(对象,类型)用于检查一个对象是否属于某个类型.在or的情况下,如果前面的结果为True,则后面的判断不会运行.原代码的问题是会取到类型为int的数判断是否是叶子节点，而is_leaf需要branches()的tree[1:],int类型没有切片.
        return tree
    if len(tree)>2:  # 这里二叉树的列表长度是2
        tree = [tree[0],tree[1:]]
    return [right_binarize(b) for b in tree]

print(right_binarize([1, 2, 3, 4, 5, 6, 7]))

#========(2)链表=====================================
empty = 'empty'

# 构造链表

# 首先判断链表
def is_link(s):
    return s == empty or (len(s)==2 or is_link(s[1]))

# 构造链表
def link(first, rest):
    assert is_link(rest), 'rest 必须是一个链表'
    return [first, rest]

# 定义选择器
def first(s):
    assert is_link(s),'s必须是一个链表'
    assert s!=empty, '空链表没有第一个元素'  # 容易拉下
    return s[0]

def rest(s):
    assert is_link(s),'s必须是一个链表'
    assert s!=empty, '空链表没有剩余元素'    # 容易拉下
    return s[1]


# 序列抽象的条件------长度和元素选择

## 长度
def len_link(s):
    '''返回链表s的长度'''
    assert is_link(s)
    total = 0
    while s!=empty:
        s,total=rest(s),total+1
    return total

## 元素选择
def getitem_link(s,i):    # getitem的含义是get item,表示用索引或键获取某个元素
    '''返回链表s中的第i个元素'''
    assert is_link(s)
    while i>0:
        s,i=rest(s),i-1
    return first(s)

## 长度---用递归实现
def len_link_recursive(s):
    if s==empty:
        return 0
    else:
        return 1+len_link_recursive(rest(s))
    

## 元素选择---用递归实现
def getitem_link_recursive(s,i):
    if i==0:
        return first(s)
    else:
        return getitem_link_recursive(rest(s),i-1)

# 序列操作------延长\应用\过滤\连接
def extend_link(s,t):
    '''递归实现:将链表t以链表的格式延长链表s'''
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s),extend_link(rest(s),t))

def apply_to_all_link(f,s):
    '''递归实现:链表s的所有元素(注意除empty外,empty只是为了完整链表结构,不算元素)应用函数f,即map的功能
    实现方法与extend_link类似,使用递归直到s的empty终止,每次操作都对first(s)应用函数f'''
    assert is_link(s)
    if s == empty:
        return empty
    else:
        return link(f(first(s)),apply_to_all_link(f,rest(s)))

def keep_if_link(f,s):
    '''递归实现:只过滤出链表s中满足函数f(函数返回True或False)的元素,以链表的形式输出,即filter的功能'''
    assert is_link(s)
    if s == empty:
        return empty
    else:
        if f(first(s)) == False:                    
            return keep_if_link(f,rest(s))   # 若s的第一个元素不满足f,则跳过
        else:
            return link(first(s),keep_if_link(f,rest(s)))

def join_link(s,separator):
    '''递归实现:将链表s中的元素,以separator为分隔符连接'''
    assert is_link(s)
    if s == empty:
        return ''   # 到达递归终止位置时,返回空串
    else:                  
        if rest(s) == empty:      # 这里也可以用教材中的elif
            return str(first(s))
        else:
            return str(first(s))+separator+join_link(rest(s),separator)


# 链表--递归构造--分割数
def partitions(n,m):
    '''返回一个包含 n 的分割方案的链表，其中每个正整数不超过 m
    第一层每个元素都是一个链表,除最后一个empty外,其他元素都是一个方案
    自己对照着代码,以(6,4)为例写了一遍过程,勉强能够理解
    但是要自己想出并写出这段代码还比较难'''
    if n == 0:
        return link(empty,empty)
    elif n<0 or m==0:
        return empty
    else:
        using_m = partitions(n-m,m)
        with_m = apply_to_all_link(lambda s:link(m,s),using_m)
        without_m = partitions(n,m-1)
        return extend_link(with_m,without_m)

def print_partitions(n,m):
    '''将每种方案打印下来,由于最外层链表的元素都是一个方案,
    因此只要对每个元素用join_link就可以实现
    我的实现代码如下'''
    part_link = partitions(n,m)
    f = lambda s:print(join_link(s,separator=' + '))
    apply_to_all_link(f,part_link)

# 教材上打印分割方案的代码如下:
def print_partitions_reference(n, m):
    lists = partitions(n, m)
    strings = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(strings, "\n"))


