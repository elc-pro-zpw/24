import itertools,math
class Node:
	def __init__(self,left=None,right=None,operator=None):
		self.left = str(left)
		self.right = str(right)
		self.operator = str(operator)

	def operate(self): #左边或者右边可能是Node类对象，要想可以eval运算，就得让每个节点实例类就是一个表达式，所以改写__repr__方法
		return eval(self.left+self.operator+self.right)

	def __repr__(self): #改写__repr__方法后，每个节点本身结果就是一个表达式
		return '('+self.left+self.operator+self.right+')'
	__str__ = __repr__


def buildAllTree(trees):
	if len(trees)==1:
		return trees
	else:
		tree_list = []
		for i in range(1,len(trees)):
			left_array = trees[:i]
			right_array = trees[i:]
			left_trees = buildAllTree(left_array)
			right_trees = buildAllTree(right_array)
			for left in left_trees:
				for right in right_trees:
					tree_list.extend(buildTree(left,right))
		return tree_list

def buildTree(left,right):
	treelist = []
	treelist.append(Node(left,right,'*'))
	treelist.append(Node(left,right,'+'))
	treelist.append(Node(left,right,'-'))
	if right != 0:
		treelist.append(Node(left,right,'/'))
	return treelist

def get_result(array):
	trees = itertools.permutations(array)#排列组合数组生成所有可能的组合
	for tree in trees:
		results = buildAllTree(tree)
		for i in results:
			try:
				result = i.operate()
			except ZeroDivisionError:
				pass
			if math.isclose(result,24,rel_tol=1e-10):#设定一个误差
				return repr(i) + ' => 24'
	return 'Dont found'


if __name__ == '__main__':
	print(get_result([1,5,7,10]))
