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

def _find_node_iterative(self, item):
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if item == node.data:
                return node
            elif item < node.data:
                node = node.left
            elif item > node.data:
                node = node.right
        # Not found
        return None
