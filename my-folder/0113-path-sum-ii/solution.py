class Solution(object):
    def recursive(self,node,remainingSum,pathNode,pathList):
        if not node:
            return 
        pathNode.append(node.val)
        if node.val==remainingSum and not node.left and not node.right:
            pathList.append(list(pathNode))
        else:
            self.recursive(node.left,remainingSum - node.val, pathNode,pathList)
            self.recursive(node.right,remainingSum - node.val, pathNode,pathList)
        pathNode.pop()
    def pathSum(self, root, targetSum):
        pathList=[]
        self.recursive(root,targetSum,[],pathList)
        return pathList
