class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        String[] charactersOfS = s.split("");
        String[] charactersOfT = t.split("");

        ArrayList<String> charsS = new ArrayList<>();
        ArrayList<String> charsT = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            charsS.add(charactersOfS[i]);
            charsT.add(charactersOfT[i]);
        }

        for (int i = 0; i < charsS.size(); i++) {
            if (!charsT.contains(charsS.get(i))) {
                return false;
            }
            else {
                charsT.remove(charsS.get(i));
            }
        }
        return true;
    }
}
