from typing import List

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(val) pushes the element val onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.
    
Constraints:
    - -2**31 <= val <= 2**31 - 1
    - Methods pop, top and getMin operations will always be called on non-empty stacks.
    - At most 3 * 10**4 calls will be made to push, pop, top, and getMin.
    
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''


class Solution:
    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack: List = []
        self.min: List = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_value = self.getMin()
        if min_value is None or val <= min_value:
            self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop(-1)
        if val == self.getMin():
            self.min.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1] if self.min else None


if __name__ == '__main__':
    acts = ["MinStack", "push", "push", "push", "getMin", "pop", "getMin"]


    nums = [[], [0], [1], [0], [], [], []]
    sol = None
    for i in range(len(acts)):
        act = acts[i]
        if act == 'MinStack':
            sol = Solution()
            print(f'create solution object')
        elif act == 'push':
            num = nums[i][0]
            sol.push(num)
            print(f'push {num} into solution object')

        elif act == 'pop':
            print(f'pop {sol.pop()} from solution object')

        elif act == 'top':
            print(f'get top {sol.top()} from solution object')

        elif act == 'getMin':
            print(f'get min {sol.getMin()} from solution object')
