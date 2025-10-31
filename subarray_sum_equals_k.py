"""
Problem: Find the number of sub-arrays with sum equal to k
Approach: Use the prefix sum + hash-map technique for O(n) time
Time complexity: O(n)
Space complexity: O(n)
Author: Anushka Kumari Agrawal
"""

def subarray_sum_equals_k(nums, k):
    if nums is None:
        raise ValueError("Input array cannot be None")
    count = 0
    prefix_sum = 0
    freq = {0: 1}  # prefix sum 0 occurs once

    for num in nums:
        prefix_sum += num
        # if prefix_sum − k occurred before, add its count to result
        if (prefix_sum - k) in freq:
            count += freq[prefix_sum - k]
        # update freq of current prefix_sum
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count

def main():
    # Example test cases
    print("Test1:", subarray_sum_equals_k([1, 1, 1], 2))          # expected output: 2
    print("Test2:", subarray_sum_equals_k([1, 2, 3], 3))          # expected output: 2 ( [1,2], [3] )
    print("Test3:", subarray_sum_equals_k([3,4,7,2,-3,1,4,2], 7)) # expected output: 4

if __name__ == "__main__":
    main()
