def insert(self, item):
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        parent = self._find_parent_node_recursive(item, self.root)
        
        if parent == None:
            self.root.left = BinaryTreeNode(item)
        elif parent.data > item:
            parent.left = BinaryTreeNode(item)
        elif parent.data < item:
            parent.right = BinaryTreeNode(item)
        self.size += 1
