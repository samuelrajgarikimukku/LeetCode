class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Method - 1
        # for i in range(len(image)):
        #     image[i] = image[i][::-1]
        # for i in range(len(image)):
        #     for j in range(len(image[0])):
        #         image[i][j] = 1 - image[i][j]
        # return image
        
        #  Method - 2
        for i in range(len(image)):
            image[i] = [1-x for x in image[i][::-1]]
        return image