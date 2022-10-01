```
from collections import defaultdict
class Solution:
def majorityElement(self, nums: List[int]) -> int:
hashmap = defaultdict(int)
for i in nums:
#if i not in hashmap:
hashmap[i] += 1
print(hashmap)
for key in hashmap:
if hashmap[key] >= len(nums)/2:
return key
else:
i += 1
```