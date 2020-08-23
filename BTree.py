from binarytree import build
class BTree:
    def __init__(self, nodes):
        self.binary_Tree = build(nodes)

    def process(self):
        print('Binary tree from list: \n', self.binary_Tree)

        print('\n List from Binary tree', self.binary_Tree.values)
