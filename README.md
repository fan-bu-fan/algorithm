# algorithm
Kmp
# 寻找最大公共前缀
def qianzuibiao(pattern):
    
    prefix = [0]
    # 设置一个指针先指向第一个元素所在的索引
    length = 0
    # 从第二个元素开始添加它的最大公共前缀
    i =1
    while(i<len(pattern)):
        if pattern[length] == pattern[i]:
            # 当元素相同的时候 length指针和索引指针i 同时向后移
            length +=1
            i +=1
            prefix.append(length)
        # 当 当前元素和 i指向的元素不一样的时候 不能直接把当前元素的最大公共前缀设为0 应该往前遍历
        # 遍历到和它前一个元素相同的那个位置
        else:
            if length >0:
                length = prefix[length-1]
            else:
                prefix.append(0)
                i+=1
    return prefix
# 将 prefix 表格往右推一位并且将第一位补位-1
def move(prefix):
    prefix =[-1]+prefix[:-1]
    return prefix

# 利用 text pattren 和prefix 进行匹配 prefix 的表的作用就是帮我们重新定位指针j 所在的位置
def match(text,pattern,prefix):
    # i 指针指向text
    # j 指针指向pattern
    i = 0
    j = 0
    while(i<len(text)):
        # 当指针指向的两个元素相互匹配的时候 i+1，j+1 指针都后移
        if text[i] == pattern[j]:
            i +=1
            j +=1
        else:
            # 当指针不匹配的时候我没就要重新定位j
            j = prefix[j]
            # 当第0 个元素都比较完之后还不匹配的话 就两个指针同时往后移动
            if j == -1:
                i +=1
                j +=1
        if j==len(pattern):
            # 说明 有匹配成功的
            print("在位置{}匹配成功".format(i-len(pattern)))
            j = prefix[j-1]

pattern ="ababc"
print(prefix)
# [0, 0, 1, 2, 0]
prefix=qianzuibiao(pattern)

prefix = move(prefix)

print(prefix)
# [-1, 0, 0, 1, 2]

text ="abaacababcababc"
match(text,pattern,prefix)

#在位置5匹配成功
#在位置10匹配成功
