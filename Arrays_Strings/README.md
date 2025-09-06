# Arrays & Strings

## Pattern Summary
Arrays and Strings are fundamental data structures in interviews. Many problems involve **manipulating sequences** of numbers or characters efficiently.

Common patterns:
- **Two Pointer / Sliding Window** → Subarrays, substrings, max/min problems
- **Prefix Sum / Cumulative Sum** → Sum-related optimizations
- **HashMap / Frequency Counting** → Pairs, duplicates, anagrams, target sums
- **Sorting + Binary Search** → For ordered array/string problems
- **In-place Modification** → Optimize space usage

## How to Approach Problems
1. Read and understand problem carefully  
2. Identify the underlying **pattern**  
3. Consider brute-force solution first, then optimize  
4. Handle **edge cases** (empty, single element, negative numbers, repeated characters)  
5. Write **clean, commented Python code** with time/space complexity analysis  

## Example Problems
1. **Two Sum (Array)**
   - Link: https://leetcode.com/problems/two-sum/
   - Pattern: HashMap Lookup
   - Approach: Iterate once, store seen numbers in hashmap, check complement
2. **Maximum Subarray**
   - Link: https://leetcode.com/problems/maximum-subarray/
   - Pattern: Sliding Window / Kadane’s Algorithm
   - Approach: Running sum, reset if sum < 0, track max sum
3. **Valid Palindrome (String)**
   - Link: https://leetcode.com/problems/valid-palindrome/
   - Pattern: Two Pointer
   - Approach: Compare characters from both ends, skip non-alphanumeric

## Notes
- Each problem file includes:
  - Problem link
  - Pattern
  - Python solution with comments
  - Time & Space Complexity
- Focus on **recognizing patterns**, many problems are variations of these fundamentals.

