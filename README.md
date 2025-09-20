 <!-- 
 <h1>JWipe - Disk Sanitization</h1>

 ### [YouTube Demonstration](https://youtu.be/7eJexJVCqJo)

<h2>Description</h2>
Project consists of a simple PowerShell script that walks the user through "zeroing out" (wiping) any drives that are connected to the system. The utility allows you to select the target disk and choose the number of passes that are performed. The PowerShell script will configure a diskpart script file based on the user's selections and then launch Diskpart to perform the disk sanitization.
<br />


<h2>Languages and Utilities Used</h2>

- <b>PowerShell</b> 
- <b>Diskpart</b>

<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/62TgaWL.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select the disk:  <br/>
<img src="https://i.imgur.com/tcTyMUE.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Enter the number of passes: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>
--!> 
<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0001-two-sum) |
| [0011-container-with-most-water](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0011-container-with-most-water) |
| [0057-insert-interval](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0057-insert-interval) |
| [0088-merge-sorted-array](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0088-merge-sorted-array) |
| [0213-house-robber-ii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0213-house-robber-ii) |
| [0216-combination-sum-iii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0216-combination-sum-iii) |
| [0238-product-of-array-except-self](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0238-product-of-array-except-self) |
| [0283-move-zeroes](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0283-move-zeroes) |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
| [0435-non-overlapping-intervals](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0435-non-overlapping-intervals) |
| [1004-max-consecutive-ones-iii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1004-max-consecutive-ones-iii) |
| [1397-search-suggestions-system](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1397-search-suggestions-system) |
| [1493-longest-subarray-of-1s-after-deleting-one-element](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1493-longest-subarray-of-1s-after-deleting-one-element) |
| [1679-max-number-of-k-sum-pairs](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1679-max-number-of-k-sum-pairs) |
## String
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0003-longest-substring-without-repeating-characters) |
| [0043-multiply-strings](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0043-multiply-strings) |
| [0151-reverse-words-in-a-string](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0151-reverse-words-in-a-string) |
| [0208-implement-trie-prefix-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0208-implement-trie-prefix-tree) |
| [0345-reverse-vowels-of-a-string](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0345-reverse-vowels-of-a-string) |
| [0392-is-subsequence](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0392-is-subsequence) |
| [0443-string-compression](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0443-string-compression) |
| [1071-greatest-common-divisor-of-strings](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1071-greatest-common-divisor-of-strings) |
| [1250-longest-common-subsequence](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1250-longest-common-subsequence) |
| [1397-search-suggestions-system](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1397-search-suggestions-system) |
| [1423-maximum-number-of-occurrences-of-a-substring](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1423-maximum-number-of-occurrences-of-a-substring) |
| [1768-merge-strings-alternately](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1768-merge-strings-alternately) |
| [2185-counting-words-with-a-given-prefix](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/2185-counting-words-with-a-given-prefix) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0001-two-sum) |
| [0128-longest-consecutive-sequence](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0128-longest-consecutive-sequence) |
| [0208-implement-trie-prefix-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0208-implement-trie-prefix-tree) |
| [0238-product-of-array-except-self](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0238-product-of-array-except-self) |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
| [1423-maximum-number-of-occurrences-of-a-substring](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1423-maximum-number-of-occurrences-of-a-substring) |
## Stack
|  |
| ------- |
| [0150-evaluate-reverse-polish-notation](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0150-evaluate-reverse-polish-notation) |
| [0155-min-stack](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0155-min-stack) |
| [0394-decode-string](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0394-decode-string) |
| [0937-online-stock-span](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0937-online-stock-span) |
## Two Pointer
|  |
| ------- |
| [0011-container-with-most-water](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0011-container-with-most-water) |
| [0345-reverse-vowels-of-a-string](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0345-reverse-vowels-of-a-string) |
| [0392-is-subsequence](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0392-is-subsequence) |
| [1004-max-consecutive-ones-iii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1004-max-consecutive-ones-iii) |
| [1493-longest-subarray-of-1s-after-deleting-one-element](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1493-longest-subarray-of-1s-after-deleting-one-element) |
| [1679-max-number-of-k-sum-pairs](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1679-max-number-of-k-sum-pairs) |
## Binary Tree
|  |
| ------- |
| [0102-binary-tree-level-order-traversal](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0102-binary-tree-level-order-traversal) |
| [0104-maximum-depth-of-binary-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0104-maximum-depth-of-binary-tree) |
| [0437-path-sum-iii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0437-path-sum-iii) |
| [0450-delete-node-in-a-bst](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0450-delete-node-in-a-bst) |
| [1448-count-good-nodes-in-binary-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1448-count-good-nodes-in-binary-tree) |
## Tree
|  |
| ------- |
| [0102-binary-tree-level-order-traversal](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0102-binary-tree-level-order-traversal) |
| [0104-maximum-depth-of-binary-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0104-maximum-depth-of-binary-tree) |
| [0437-path-sum-iii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0437-path-sum-iii) |
| [0450-delete-node-in-a-bst](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0450-delete-node-in-a-bst) |
| [1448-count-good-nodes-in-binary-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1448-count-good-nodes-in-binary-tree) |
## Heap / Priority Queue
|  |
| ------- |
| [0215-kth-largest-element-in-an-array](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0215-kth-largest-element-in-an-array) |
## Math / Simulation
|  |
| ------- |
| [0043-multiply-strings](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0043-multiply-strings) |
| [0046-permutations](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0046-permutations) |
| [0062-unique-paths](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0062-unique-paths) |
## Sliding Window
|  |
| ------- |
| [0003-longest-substring-without-repeating-characters](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0003-longest-substring-without-repeating-characters) |
| [1004-max-consecutive-ones-iii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1004-max-consecutive-ones-iii) |
| [1423-maximum-number-of-occurrences-of-a-substring](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1423-maximum-number-of-occurrences-of-a-substring) |
| [1456-maximum-number-of-vowels-in-a-substring-of-given-length](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1456-maximum-number-of-vowels-in-a-substring-of-given-length) |
## Greedy / Subsequence
|  |
| ------- |
| [0334-increasing-triplet-subsequence](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0334-increasing-triplet-subsequence) |
| [0435-non-overlapping-intervals](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0435-non-overlapping-intervals) |
## Linked List
|  |
| ------- |
| [0206-reverse-linked-list](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0206-reverse-linked-list) |
| [0876-middle-of-the-linked-list](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0876-middle-of-the-linked-list) |
| [1290-convert-binary-number-in-a-linked-list-to-integer](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1290-convert-binary-number-in-a-linked-list-to-integer) |
| [2095-delete-the-middle-node-of-a-linked-list](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/2095-delete-the-middle-node-of-a-linked-list) |
| [2130-maximum-twin-sum-of-a-linked-list](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/2130-maximum-twin-sum-of-a-linked-list) |
## Binary Search
|  |
| ------- |
| [0162-find-peak-element](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0162-find-peak-element) |
| [0700-search-in-a-binary-search-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0700-search-in-a-binary-search-tree) |
| [1397-search-suggestions-system](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1397-search-suggestions-system) |
## Miscellaneous
|  |
| ------- |
| [0374-guess-number-higher-or-lower](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0374-guess-number-higher-or-lower) |
| [0605-can-place-flowers](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0605-can-place-flowers) |
| [0872-leaf-similar-trees](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/0872-leaf-similar-trees) |
| [1431-kids-with-the-greatest-number-of-candies](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/1431-kids-with-the-greatest-number-of-candies) |
| [2300-successful-pairs-of-spells-and-potions](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/2300-successful-pairs-of-spells-and-potions) |
| [2390-removing-stars-from-a-string](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/main/2390-removing-stars-from-a-string) |
## Dynamic Programming
|  |
| ------- |
| [0062-unique-paths](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0062-unique-paths) |
| [0213-house-robber-ii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0213-house-robber-ii) |
| [0435-non-overlapping-intervals](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0435-non-overlapping-intervals) |
| [1250-longest-common-subsequence](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1250-longest-common-subsequence) |
## Combinatorics
|  |
| ------- |
| [0062-unique-paths](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0062-unique-paths) |
## Binary Search Tree
|  |
| ------- |
| [0450-delete-node-in-a-bst](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0450-delete-node-in-a-bst) |
## Backtracking
|  |
| ------- |
| [0216-combination-sum-iii](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0216-combination-sum-iii) |
## Design
|  |
| ------- |
| [0208-implement-trie-prefix-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0208-implement-trie-prefix-tree) |
| [0937-online-stock-span](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0937-online-stock-span) |
## Trie
|  |
| ------- |
| [0208-implement-trie-prefix-tree](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0208-implement-trie-prefix-tree) |
| [1397-search-suggestions-system](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1397-search-suggestions-system) |
## Sorting
|  |
| ------- |
| [0088-merge-sorted-array](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0088-merge-sorted-array) |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
| [0435-non-overlapping-intervals](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0435-non-overlapping-intervals) |
| [1397-search-suggestions-system](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1397-search-suggestions-system) |
## Heap (Priority Queue)
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
| [1397-search-suggestions-system](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/1397-search-suggestions-system) |
## Monotonic Stack
|  |
| ------- |
| [0937-online-stock-span](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0937-online-stock-span) |
## Data Stream
|  |
| ------- |
| [0937-online-stock-span](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0937-online-stock-span) |
## Two Pointers
|  |
| ------- |
| [0088-merge-sorted-array](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0088-merge-sorted-array) |
## Divide and Conquer
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
## Bucket Sort
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
## Counting
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
## Quickselect
|  |
| ------- |
| [0347-top-k-frequent-elements](https://github.com/kenechukz/LeetcodeDSA-Practice/tree/master/0347-top-k-frequent-elements) |
<!---LeetCode Topics End-->
