# Arrays

## Pattern Summary
Arrays are one of the most fundamental data structures in programming and interviews.  
Many problems on arrays test your ability to manipulate sequences of numbers efficiently.  

Common patterns include:
- **Two Pointer / Sliding Window** → For subarray/subsequence problems
- **Prefix Sum / Cumulative Sum** → For sum-related optimizations
- **HashMap / Frequency Counting** → For finding pairs, duplicates, or target sums
- **Sorting + Binary Search** → For ordered array problems
- **In-place Modification** → For space optimization

## How to Approach Array Problems
1. **Understand the problem requirements** (sum, count, max/min, subarray, etc.)  
2. **Identify the pattern** (sliding window, two pointer, hashmap, etc.)  
3. **Consider brute-force first**, then optimize to O(n) or O(n log n) if possible  
4. **Think about edge cases** (empty arrays, single element, negative numbers)  
5. **Write clean code** with comments and complexity analysis  

## Example Problems
1. **Two Sum**
   - Link: https://leetcode.com/problems/two-sum/
   - Pattern: HashMap Lookup
   - Approach: Iterate once, store seen numbers in a hashmap, check for complement
2. **Maximum Subarray**
   - Link: https://leetcode.com/problems/maximum-subarray/
   - Pattern: Sliding Window / Kadane’s Algorithm
   - Approach: Keep a running sum, reset if sum < 0, track max sum
3. **Container With Most Water**
   - Link: https://leetcode.com/problems/container-with-most-water/
   - Pattern: Two Pointer
   - Approach: Move pointers inward from edges, calculate area, update max

## Notes
- Each problem in this folder includes:
  - Problem link
  - Approach summary
  - Python solution with comments
  - Time & Space Complexity
- Focus on **recognizing the patterns**; many interview questions are variations of these array patterns.

