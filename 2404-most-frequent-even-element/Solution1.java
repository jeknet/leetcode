// https://leetcode.com/problems/most-frequent-even-element/submissions/1060095137/
class Solution {
    public int mostFrequentEven(int[] nums) {
        Map<Integer, Integer> evens = new HashMap();
        int max = 0;

        for(int num : nums){
            if(num%2 == 0){
                evens.put(num, evens.getOrDefault(num,0)+1);
            }
        } 

        PriorityQueue<Integer> queue = new PriorityQueue();
        for(Integer number : evens.keySet()){
            if(evens.get(number) > max){
                max = evens.get(number);
                queue.clear();
                queue.add(number);
            }else if(evens.get(number) == max){
                queue.add(number);
            }
        }

        return queue.size() > 0? queue.poll() : -1;
    }
}
