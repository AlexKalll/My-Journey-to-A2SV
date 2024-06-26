class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {c: i for i, c in enumerate(s)}
        result = []
        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
