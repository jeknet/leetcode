// https://leetcode.com/problems/replace-words/submissions/1045991000/
class TrieNode{
    private Boolean isFinal = false;
    private Map<Character, TrieNode> children = new HashMap(); 

    public void add(String root){
        addImpl(root, 0);
    }

    private void addImpl(String root, int index){
        if(index == root.length()){
            isFinal = true;
            return;
        }

        char val = root.charAt(index);
        if(children.get(val) == null){
            children.put(val, new TrieNode());
        }
        TrieNode next = children.get(val);
        next.addImpl(root, index + 1);
    }

    public String getPrefix(String word){
        return getPrefixImpl(word, 0);
    }

    private String getPrefixImpl(String word, int index){
        if(isFinal){
            return word.substring(0, index);
        }
        if(index == word.length()){
            return null;
        }
        char val = word.charAt(index);
        TrieNode next = children.get(val);
        if(next != null){
            return next.getPrefixImpl(word, index + 1);
        }
        return null;
    }
}

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        TrieNode trie = new TrieNode();
        
        dictionary.stream().forEach(word->trie.add(word));

        return Arrays.stream(sentence.split(" "))
            .map(word->{
                String prefix = trie.getPrefix(word);
                return prefix == null? word : prefix;
        }).collect(Collectors.joining(" "));
    }
}
