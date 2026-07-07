# 链表基础课

链表不是数组。链表的核心不是下标，而是「节点之间的连接」。

## 1. 一个节点是什么

在 LeetCode 里，链表节点通常长这样：

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

你先不要急着背类。只需要理解：

| 字段 | 含义 |
| --- | --- |
| `val` | 这个节点保存的值 |
| `next` | 指向下一个节点 |

所以一个链表：

```text
1 -> 2 -> 3 -> None
```

可以理解为：

```text
节点1.val = 1，节点1.next = 节点2
节点2.val = 2，节点2.next = 节点3
节点3.val = 3，节点3.next = None
```

## 2. head 是什么

`head` 不是整个数组，也不是一个下标。

`head` 是「第一个节点的引用」。

```text
head
 ↓
 1 -> 2 -> 3 -> None
```

如果链表为空：

```text
head = None
```

## 3. 如何遍历链表

链表不能写 `head[0]`、`head[1]`。

你只能一步一步走：

```python
cur = head
while cur is not None:
    # 当前节点是 cur
    cur = cur.next
```

这段代码的关键不是语法，而是状态变化：

```text
cur -> 1
cur -> 2
cur -> 3
cur -> None，停止
```

## 4. 为什么不能随便访问 next

如果 `cur` 已经是 `None`，再写：

```python
cur.next
```

就会报错。因为 `None` 不是节点，它没有 `next`。

所以链表题里经常要先判断：

```python
cur is not None
```

或者：

```python
cur.next is not None
```

## 5. 141 环形链表到底在问什么

正常链表：

```text
1 -> 2 -> 3 -> None
```

有环链表：

```text
1 -> 2 -> 3 -> 4
     ↑         ↓
     └─────────┘
```

如果一直沿着 `next` 走，有环链表永远走不到 `None`。

141 只问：

```text
这个链表会不会绕圈？
```

返回：

- 有环：`True`
- 无环：`False`

## 6. pos 是什么

题目里的 `pos` 不是函数参数。

它只是 LeetCode 后台用来构造链表的标记。

例如：

```text
head = [3, 2, 0, -4], pos = 1
```

表示尾节点 `-4` 的 `next` 指回索引 1 的节点，也就是值为 `2` 的节点。

你写函数时拿不到 `pos`，也不应该使用 `pos`。

## 7. 快慢指针为什么能判断环

设置两个指针：

- `slow`：每次走 1 步。
- `fast`：每次走 2 步。

如果没有环，`fast` 会先走到 `None`。

如果有环，它们就像在环形跑道上跑步，快的人迟早会追上慢的人。

所以 141 的判断逻辑是：

```text
fast 走到 None：无环
slow 和 fast 相遇：有环
```

## 8. 链表题的学习顺序

不要跳级。

正确顺序是：

1. 看懂节点和 `next`。
2. 会遍历链表。
3. 会判断空节点。
4. 会使用快慢指针。
5. 再学习 dummy 节点。
6. 最后再做反转、删除、合并、复制、LRU。

