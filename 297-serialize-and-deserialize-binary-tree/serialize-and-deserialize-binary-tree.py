# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        array = []
        def dfs(root):
            if root is None:
                array.append('null')
                return None
            
            array.append(str(root.val))  # Convert to string
            dfs(root.left)
            dfs(root.right)
        
            return root.val
        
        dfs(root)
        return '[' + ','.join(array) + ']'  # Return formatted string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
  
        data = data[1:-1].split(',') 
        data = [None if x == 'null' else int(x) for x in data]  
        data = iter(data)
        
        def helper():
            # Get the next value in the serialized data
            try:
                value = next(data)
            except StopIteration:
                return None
          
            if value is None:
                return None
            
          
            node = TreeNode(value)
            
            node.left = helper() 
            node.right = helper() 
            
            return node
        
        return helper()