"""
全排列和子集问题
"""

# 全排列【1,2,3】,[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
res = []
def all_sorted(nums):
    track = []
    backtrack(nums, track)
    return res

def backtrack(nums, track):
    """
    // 路径：记录在 track 中
    // 选择列表：nums 中不存在于 track 的那些元素
    // 结束条件：nums 中的元素全都在 track 中出现
    """
    if len(track) == len(nums):
        # 结束条件
        res.append(track.copy())
        return
    for i in range(len(nums)):
        # 排除不合法的选择
        if nums[i] in track:
            continue
        # 做选择
        track.append(nums[i])
        # 进入下一选择
        backtrack(nums, track)
        # 撤销选择
        track.pop()

a = [1,2,3]
print(all_sorted(a))
