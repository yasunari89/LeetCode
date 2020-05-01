# Array
## Two Pointers
sortされた配列から重複する要素をcopy配列を作成せずに消す問題 (in-place algorithm)。

iとjの2つのindexで要素を比較し上書きするのがポイントである。

この問題では入力配列を上書きして重複なしの配列サイズをreturnする。つまり、`input_array[:unduplicated_size]`とすれば重複なし配列が出てくる。

## Simple One Pass
[Simple One Pass](122_maxprofit_2.png)

## Rotate Array
`nums = [1,2,3,4,5,6,7], k = 3`があったときにk回右に要素をスライドさせることで
```
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```
とする問題。何も考えずに
```python
for i in range(k):
    for j in range(len(nums)):
        # some processes...
```
とすると時間計算量がO(n*k)となり良くなるので、k回後のnumsを考察することが重要。すると
```python
for i in range(n):
    temp[(i+k)%n] = nums[i]
nums[:] = temp
```
O(n)で済むことがわかる。