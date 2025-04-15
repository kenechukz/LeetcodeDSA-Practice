class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> indexes = new HashMap<>();
        Set<Integer> seen = new HashSet<>();
        int otherVal;
        int[] res = {0,0};

        for (int i = 0; i < nums.length; i++){
            otherVal = target - nums[i];
            if (seen.contains(otherVal)){
                res[0] = i;
                res[1] = indexes.get(otherVal);
            }

            seen.add(nums[i]);
            indexes.put(nums[i], i);
        }
        return res;   
    }
}