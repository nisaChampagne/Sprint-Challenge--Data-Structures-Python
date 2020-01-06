class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # not needed but up to  to preference
        elif value == self.value:
            return "Already in tree"

    def contains(self, target):
        # if target  == self.value, return it
        # go left or right based on smaller or bigger
        if self.value == target:
            return True
        if target > self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        #not needed to pass tests
        if not self:
            return False
