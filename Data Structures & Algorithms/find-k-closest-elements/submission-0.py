class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        window = []
        l = 0

        for r in range(len(arr)):
            if r < k:
                window.append(arr[r])
                continue
            
            # Compare the current element at r with the first element of the current window
            if abs(arr[r] - x) < abs(arr[l] - x):
                window.pop(0)
                window.append(arr[r])
                l = l + 1
            elif arr[r] >= x: # Optimization: since arr is sorted, we can stop early
                break

        return window
