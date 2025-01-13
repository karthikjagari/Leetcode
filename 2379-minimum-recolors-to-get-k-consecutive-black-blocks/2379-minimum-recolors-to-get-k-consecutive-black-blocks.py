class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
        # code for the current_white_count:
        current_white_count = 0  # Start with no white blocks counted
        for i in range(k):  # Loop through the first 'k' characters
            if blocks[i] == 'W':  # Check if the current block is white
                current_white_count += 1  # If yes, increase the count
        
        # minimum operations with the count of white blocks
        # in the first window, This is the starting point.
        min_operations = current_white_count
        
        #  a sliding window to move through the string and adjust counts.
        # The window will start at index 0 and slide to the right until the end of the string.
        for i in range(k, len(blocks)):
            # Remove the effect of the block that is sliding out of the window
            if blocks[i - k] == 'W':  # If the block that is leaving is white
                current_white_count -= 1  # Reduce the count of white blocks
            
            # Add the effect of the new block that is sliding into the window
            if blocks[i] == 'W':  # If the block that is entering is white
                current_white_count += 1  # Increase the count of white blocks
            
            # minimum operations to keep track of the smallest number of white blocks
            min_operations = min(min_operations, current_white_count)
        
        #  which represents the least recolors needed.
        return min_operations
