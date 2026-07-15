class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # 1. Sort the candidates to handle duplicates easily
        candidates.sort()
        
        def backtrack(start_idx, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            if remaining_target < 0:
                return
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining_target:
                    break
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, remaining_target - candidates[i])
                current_combination.pop()
                
        backtrack(0, [], target)
        return result