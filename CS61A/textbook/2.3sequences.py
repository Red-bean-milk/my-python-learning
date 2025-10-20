# 列表推导式
x = [1,2,3,4,5,6,7,8,9]
print([i*10 for i in x if i%2==0])

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
def right_binarize(tree):    # 这里有个bug我今天还没改出来,可恶
    '''根据tree构造一个右分叉的二叉树'''
    if is_leaf(tree):
        return tree
    if len(tree)>2:  # 这里二叉树的列表长度是2
        tree = [tree[0],tree[1:]]
    return [tree[0],right_binarize(tree[1])]

print(right_binarize([1, 2, 3, 4, 5, 6, 7]))