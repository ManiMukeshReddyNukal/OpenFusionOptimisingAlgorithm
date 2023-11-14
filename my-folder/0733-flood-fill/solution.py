class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if len(image)==0:
            return

        dir=((1,0),(0,1),(-1,0),(0,-1))
        q=collections.deque()
        q.append((sr,sc))
        tv=image[sr][sc]
        if tv==color:
            return image
        m, n = len(image), len(image[0])
        while q:
            k,l=q.popleft()
            image[k][l]=color
            for i,j in dir:
                if 0<=k+i<len(image) and 0<= l+j< len(image[0]) and image[k+i][l+j]==tv:
                    q.append((k+i,l+j))
                    # 
        return image
