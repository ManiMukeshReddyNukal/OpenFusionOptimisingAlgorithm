class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates); // Sort the candidates to handle duplicates
        backtrack(result, new ArrayList<>(), candidates, target, 0);
        return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> currentCombination, int[] candidates, int remainingTarget, int startIndex) {
        if (remainingTarget == 0) {
            result.add(new ArrayList<>(currentCombination)); // Found a valid combination
            return;
        }

        for (int i = startIndex; i < candidates.length; i++) {
            // Skip duplicates
            if (i > startIndex && candidates[i] == candidates[i - 1]) {
                continue;
            }

            // If the current candidate exceeds the remaining target, no need to proceed further
            if (candidates[i] > remainingTarget) {
                break;
            }

            currentCombination.add(candidates[i]);
            backtrack(result, currentCombination, candidates, remainingTarget - candidates[i], i + 1);
            currentCombination.remove(currentCombination.size() - 1); // Backtrack
        }
    }
}

