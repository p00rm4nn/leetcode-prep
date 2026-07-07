# Hot 150 八周重启路线图

起始日期：2026-07-07  
每日时间：约 2 小时  
策略：先从栈、链表、树、图这些薄弱主线推进；数组、字符串、哈希、滑窗等已练过的内容放到后面回炉。

## 原则

- 每天只围绕一个主考点，不再把字符串、贪心、哈希混在同一天。
- 已做过的简单题不重复消耗时间，只做口述复盘或 10 分钟重写。
- 困难题允许拆成「理解题意」「画状态」「写核心函数」「完整 AC」几个阶段。
- 每周至少一天做错题和总结，不用硬凑新题数量。

## 每日时间模板

| 环节 | 时间 | 要求 |
| --- | ---: | --- |
| 回忆 | 10m | 写出昨天最重要的一个错点 |
| 知识 | 20m | 今天的数据结构维护什么状态 |
| 主线 | 70m | 独立写题，不直接看答案 |
| 加固 | 15m | 重写关键逻辑或补一题 |
| 复盘 | 5m | 写入 `daily-log` |

## Week 1｜07-07 至 07-13｜链表 + 栈收束

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 01 | 07-07 | 链表入口 | [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/), [21. 合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/), [2. 两数相加](https://leetcode.cn/problems/add-two-numbers/) | 说清楚 `slow/fast`、`dummy/cur` 的职责 |
| 02 | 07-08 | 链表删除与反转 | [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/), [92. 反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/), [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/) | 每题先画三节点变化 |
| 03 | 07-09 | 链表重排与复制 | [61. 旋转链表](https://leetcode.cn/problems/rotate-list/), [86. 分隔链表](https://leetcode.cn/problems/partition-list/), [138. 随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer/) | 理解拆链、接链、映射复制 |
| 04 | 07-10 | 链表设计 | [146. LRU 缓存](https://leetcode.cn/problems/lru-cache/) + 复盘 92/138 | 知道为什么哈希表要配双向链表 |
| 05 | 07-11 | 栈回炉 | 口述复盘 20/71/155/150；拆解 [224. 基本计算器](https://leetcode.cn/problems/basic-calculator/) | 困难题先理解状态，不强求硬 AC |
| 06 | 07-12 | 单调栈补强 | [496. 下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/), [503. 下一个更大元素 II](https://leetcode.cn/problems/next-greater-element-ii/), [739. 每日温度](https://leetcode.cn/problems/daily-temperatures/) | 明确栈里的元素为什么保持单调 |
| 07 | 07-13 | 周总结 | 重写本周最卡的 2 题；整理链表/栈模板 | 不追新题，修补漏洞 |

## Week 2｜07-14 至 07-20｜二叉树 DFS/BFS

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 08 | 07-14 | 树的递归入口 | [104. 最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/), [100. 相同的树](https://leetcode.cn/problems/same-tree/), [226. 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/), [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/) | 每个递归函数都说清返回值 |
| 09 | 07-15 | 构造二叉树 | [105. 前序中序构造树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/), [106. 中序后序构造树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | 用哈希定位根节点 |
| 10 | 07-16 | 树形改造 | [117. 填充右侧指针 II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/), [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/) | 分清遍历顺序和修改顺序 |
| 11 | 07-17 | 路径 DFS | [112. 路径总和](https://leetcode.cn/problems/path-sum/), [129. 根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/) | 维护从根到当前节点的状态 |
| 12 | 07-18 | 树上困难题 | [124. 二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/), [236. 最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) | 区分「给父节点的贡献」和「全局答案」 |
| 13 | 07-19 | 层序遍历 | [199. 右视图](https://leetcode.cn/problems/binary-tree-right-side-view/), [637. 层平均值](https://leetcode.cn/problems/average-of-levels-in-binary-tree/), [102. 层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/), [103. 锯齿层序](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) | 队列里装一层，答案按层更新 |
| 14 | 07-20 | BST | [530. 最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/), [230. 第 K 小元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/), [98. 验证 BST](https://leetcode.cn/problems/validate-binary-search-tree/) | 利用中序遍历有序性 |

## Week 3｜07-21 至 07-27｜图 + Trie

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 15 | 07-21 | 网格 DFS | [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/), [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/) | 把矩阵看成图 |
| 16 | 07-22 | 图建模 | [133. 克隆图](https://leetcode.cn/problems/clone-graph/), [399. 除法求值](https://leetcode.cn/problems/evaluate-division/) | 先建图，再遍历 |
| 17 | 07-23 | 拓扑排序 | [207. 课程表](https://leetcode.cn/problems/course-schedule/), [210. 课程表 II](https://leetcode.cn/problems/course-schedule-ii/) | 入度、邻接表、队列 |
| 18 | 07-24 | BFS 最短路 | [909. 蛇梯棋](https://leetcode.cn/problems/snakes-and-ladders/), [433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/) | BFS 的层数就是步数 |
| 19 | 07-25 | 单词接龙 | [127. 单词接龙](https://leetcode.cn/problems/word-ladder/) | 困难题拆成建邻居和 BFS |
| 20 | 07-26 | Trie | [208. 实现 Trie](https://leetcode.cn/problems/implement-trie-prefix-tree/), [211. 添加与搜索单词](https://leetcode.cn/problems/design-add-and-search-words-data-structure/) | 节点存 children 和 is_end |
| 21 | 07-27 | Trie + 回溯 | [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/) + 周总结 | Trie 不是炫技，是剪枝 |

## Week 4｜07-28 至 08-03｜回溯 + 分治

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 22 | 07-28 | 回溯入口 | [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/), [77. 组合](https://leetcode.cn/problems/combinations/) | 明确选择、路径、终止条件 |
| 23 | 07-29 | 排列与组合总和 | [46. 全排列](https://leetcode.cn/problems/permutations/), [39. 组合总和](https://leetcode.cn/problems/combination-sum/) | 分清可重复和不可重复选择 |
| 24 | 07-30 | 约束回溯 | [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/), [52. N 皇后 II](https://leetcode.cn/problems/n-queens-ii/) | 剪枝来自题目约束 |
| 25 | 07-31 | 网格回溯 | [79. 单词搜索](https://leetcode.cn/problems/word-search/) + 复盘 212 | visited 的进入和恢复 |
| 26 | 08-01 | 分治入口 | [108. 有序数组转 BST](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/), [148. 排序链表](https://leetcode.cn/problems/sort-list/) | 递归返回一个已经处理好的结构 |
| 27 | 08-02 | 分治困难 | [427. 建立四叉树](https://leetcode.cn/problems/construct-quad-tree/), [23. 合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/) | 合并多个子问题 |
| 28 | 08-03 | Kadane | [53. 最大子数组和](https://leetcode.cn/problems/maximum-subarray/), [918. 环形子数组最大和](https://leetcode.cn/problems/maximum-sum-circular-subarray/) | 状态只关心以当前位置结尾 |

## Week 5｜08-04 至 08-10｜二分 + 堆 + 位运算

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 29 | 08-04 | 二分入口 | [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/), [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/), [162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/) | 明确搜索区间含义 |
| 30 | 08-05 | 旋转数组二分 | [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/), [34. 查找首尾位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/), [153. 寻找最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) | 判断哪一侧有序 |
| 31 | 08-06 | 二分困难 | [4. 两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/) | 只要求理解切分思想 |
| 32 | 08-07 | 堆入口 | [215. 第 K 个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/), [373. 和最小的 K 对数字](https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/) | 堆维护候选集 |
| 33 | 08-08 | 堆设计 | [295. 数据流的中位数](https://leetcode.cn/problems/find-median-from-data-stream/), [502. IPO](https://leetcode.cn/problems/ipo/) | 双堆和贪心候选池 |
| 34 | 08-09 | 位运算入口 | [67. 二进制求和](https://leetcode.cn/problems/add-binary/), [190. 颠倒二进制位](https://leetcode.cn/problems/reverse-bits/), [191. 位 1 的个数](https://leetcode.cn/problems/number-of-1-bits/), [136. 只出现一次的数字](https://leetcode.cn/problems/single-number/) | 先理解二进制操作含义 |
| 35 | 08-10 | 位运算进阶 | [137. 只出现一次的数字 II](https://leetcode.cn/problems/single-number-ii/), [201. 数字范围按位与](https://leetcode.cn/problems/bitwise-and-of-numbers-range/), [9. 回文数](https://leetcode.cn/problems/palindrome-number/), [66. 加一](https://leetcode.cn/problems/plus-one/) | 从规律推代码 |

## Week 6｜08-11 至 08-17｜数学 + 动态规划

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 36 | 08-11 | 数学 | [172. 阶乘后的零](https://leetcode.cn/problems/factorial-trailing-zeroes/), [69. x 的平方根](https://leetcode.cn/problems/sqrtx/), [50. Pow(x, n)](https://leetcode.cn/problems/powx-n/) | 数学题先找性质 |
| 37 | 08-12 | 几何困难 | [149. 直线上最多的点数](https://leetcode.cn/problems/max-points-on-a-line/) + 数学复盘 | 斜率表示要避开浮点误差 |
| 38 | 08-13 | DP 入口 | [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/), [198. 打家劫舍](https://leetcode.cn/problems/house-robber/) | 定义 `dp[i]` 的含义 |
| 39 | 08-14 | DP 拆分 | [139. 单词拆分](https://leetcode.cn/problems/word-break/), [322. 零钱兑换](https://leetcode.cn/problems/coin-change/) | 选择来自哪里 |
| 40 | 08-15 | 序列 DP | [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) + DP 总结 | O(n^2) 先写清楚 |
| 41 | 08-16 | 网格 DP | [120. 三角形最小路径和](https://leetcode.cn/problems/triangle/), [64. 最小路径和](https://leetcode.cn/problems/minimum-path-sum/), [63. 不同路径 II](https://leetcode.cn/problems/unique-paths-ii/) | 状态从上或左来 |
| 42 | 08-17 | 字符串 DP | [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/), [97. 交错字符串](https://leetcode.cn/problems/interleaving-string/), [72. 编辑距离](https://leetcode.cn/problems/edit-distance/) | 二维状态表不要跳步 |

## Week 7｜08-18 至 08-24｜数组 / 字符串 / 双指针回炉

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 43 | 08-18 | 股票 + 跳跃 | [121. 买卖股票 I](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/), [122. 买卖股票 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/), [55. 跳跃游戏](https://leetcode.cn/problems/jump-game/), [45. 跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/) | 贪心维护最远或最优 |
| 44 | 08-19 | 原地数组 | [88. 合并有序数组](https://leetcode.cn/problems/merge-sorted-array/), [27. 移除元素](https://leetcode.cn/problems/remove-element/), [26. 删除重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/), [80. 删除重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/), [169. 多数元素](https://leetcode.cn/problems/majority-element/) | 慢指针代表可写位置 |
| 45 | 08-20 | 数组设计 | [189. 轮转数组](https://leetcode.cn/problems/rotate-array/), [274. H 指数](https://leetcode.cn/problems/h-index/), [380. O(1) 随机集合](https://leetcode.cn/problems/insert-delete-getrandom-o1/), [238. 除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/) | 结构设计要满足复杂度 |
| 46 | 08-21 | 贪心困难 | [134. 加油站](https://leetcode.cn/problems/gas-station/), [135. 分发糖果](https://leetcode.cn/problems/candy/), [42. 接雨水](https://leetcode.cn/problems/trapping-rain-water/) | 先找局部信息如何推出全局 |
| 47 | 08-22 | 字符串基础 | [13. 罗马数字转整数](https://leetcode.cn/problems/roman-to-integer/), [12. 整数转罗马数字](https://leetcode.cn/problems/integer-to-roman/), [58. 最后一个单词长度](https://leetcode.cn/problems/length-of-last-word/), [14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/) | 字符串扫描边界 |
| 48 | 08-23 | 字符串中等 | [151. 反转字符串中的单词](https://leetcode.cn/problems/reverse-words-in-a-string/), [6. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/), [28. 找出字符串中第一个匹配项](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/), [68. 文本左右对齐](https://leetcode.cn/problems/text-justification/) | 模拟题先定义输出格式 |
| 49 | 08-24 | 双指针 | [125. 验证回文串](https://leetcode.cn/problems/valid-palindrome/), [392. 判断子序列](https://leetcode.cn/problems/is-subsequence/), [167. 两数之和 II](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/), [11. 盛最多水](https://leetcode.cn/problems/container-with-most-water/), [15. 三数之和](https://leetcode.cn/problems/3sum/) | 每次移动指针要有理由 |

## Week 8｜08-25 至 08-31｜滑窗 / 哈希 / 矩阵 / 区间 + 模拟面试

| Day | 日期 | 主题 | 今日任务 | 目标 |
| ---: | --- | --- | --- | --- |
| 50 | 08-25 | 滑窗入口 | [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/), [3. 无重复字符最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | 先说窗口维护什么 |
| 51 | 08-26 | 滑窗困难 | [30. 串联所有单词的子串](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/), [76. 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) | 计数表和欠账表 |
| 52 | 08-27 | 哈希基础 | [383. 赎金信](https://leetcode.cn/problems/ransom-note/), [205. 同构字符串](https://leetcode.cn/problems/isomorphic-strings/), [290. 单词规律](https://leetcode.cn/problems/word-pattern/), [242. 有效异位词](https://leetcode.cn/problems/valid-anagram/), [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/) | 哈希表是状态压缩 |
| 53 | 08-28 | 哈希进阶 | [1. 两数之和](https://leetcode.cn/problems/two-sum/), [202. 快乐数](https://leetcode.cn/problems/happy-number/), [219. 存在重复元素 II](https://leetcode.cn/problems/contains-duplicate-ii/), [128. 最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/) | 查找型哈希和去重型哈希不同 |
| 54 | 08-29 | 矩阵 | [36. 有效数独](https://leetcode.cn/problems/valid-sudoku/), [54. 螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/), [48. 旋转图像](https://leetcode.cn/problems/rotate-image/) | 矩阵题先定边界 |
| 55 | 08-30 | 矩阵 + 区间 | [73. 矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/), [289. 生命游戏](https://leetcode.cn/problems/game-of-life/), [228. 汇总区间](https://leetcode.cn/problems/summary-ranges/), [56. 合并区间](https://leetcode.cn/problems/merge-intervals/) | 区间先排序再合并 |
| 56 | 08-31 | 区间 + 模拟 | [57. 插入区间](https://leetcode.cn/problems/insert-interval/), [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/) + 一场 45m 模拟面试 | 输出最终错题清单 |

