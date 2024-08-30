class TreeNode:
    def __init__(self, val=None, color=None):
        self.val = val
        assert color in ['r', 'b']
        self.color = 'red' if color == 'r' else 'black'

        self.left = None
        self.right = None
        self.parent = None

    def is_black(self):
        return self.color == 'black'

    def set_black(self):
        self.color = 'black'

    def set_red(self):
        self.color = 'red'


class RedBlackTree:

    def __init__(self, val_list: None):
        self.root = None
        self.black_leaf = TreeNode(color='b')

        if type(val_list) == list:
            for n in val_list:
                assert type(n) is int:

