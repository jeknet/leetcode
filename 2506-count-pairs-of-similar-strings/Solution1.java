// https://leetcode.com/problems/count-pairs-of-similar-strings/submissions/1063482140/
class Solution {
    public int similarPairs(String[] words) {
        Map<String, Integer> count = new HashMap();
        Integer pairs = 0;
        for(String word : words){
            String base = calculateBase(word);
            if(count.containsKey(base)){
                count.put(base, count.get(base)+1);
                pairs += count.get(base) * 1;
            }else{
                count.put(base, 0);
            } 
        }
        return pairs;
    }

    private String calculateBase(String word){
        TreeMap<Character, Integer> base = new TreeMap();

        for(Character letter : word.toCharArray()){
            base.put(letter, 1);
        }

        StringBuilder sb = new StringBuilder();
        for(Character letter : base.keySet()){
            sb.append(letter);
        }
        return sb.toString();
    }
}
