class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flower_count = 0  # Keep track of flowers we can plant
        length = len(flowerbed)
        
        for i in range(length):
            # Check if the current plot is empty
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty or at boundaries
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == length - 1 or flowerbed[i + 1] == 0)
                
                # If both left and right are empty, plant a flower
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    flower_count += 1
                    
                   
                  
        return flower_count >= n
