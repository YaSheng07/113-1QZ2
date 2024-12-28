class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity  # 陣列的最大容量
        self.stack = [None] * capacity  # 初始化固定大小的陣列
        self.top = -1  # 指向堆疊的頂部索引，-1 表示空

    def IsEmpty(self):
        """檢查堆疊是否為空"""
        return self.top == -1

    def IsFull(self):
        """檢查堆疊是否已滿"""
        return self.top == self.capacity - 1

    def Push(self, item):
        """將元素推入堆疊"""
        if self.IsFull():
            raise OverflowError("堆疊已滿")
        self.top += 1
        self.stack[self.top] = item

    def Pop(self):
        """從堆疊中移除頂部元素"""
        if self.IsEmpty():
            raise IndexError("堆疊是空的")
        item = self.stack[self.top]
        self.stack[self.top] = None  # 清除位置
        self.top -= 1
        return item

    def TopItem(self):
        """取得堆疊頂部的元素"""
        if self.IsEmpty():
            raise IndexError("堆疊是空的")
        return self.stack[self.top]

# 測試範例
if __name__ == "__main__":
    stack = ArrayStack(5)  # 建立一個容量為 5 的堆疊

    print("堆疊是空的嗎?", stack.IsEmpty())

    # 推入元素
    stack.Push(10)
    stack.Push(20)
    stack.Push(30)

    print("堆疊頂部的元素:", stack.TopItem())
    print("堆疊已滿嗎?", stack.IsFull())

    # 移除元素
    print("移除的元素:", stack.Pop())
    print("移除後堆疊頂部的元素:", stack.TopItem())

    # 繼續推入直到滿
    stack.Push(40)
    stack.Push(50)
    stack.Push(60)

    print("推入更多元素後堆疊已滿嗎?", stack.IsFull())
