class Solution {
    public boolean pali(String s,int left,int right){
        while (left < right) {
            if (s.charAt(left) != s.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }
    public String longestPalindrome(String s) {

        int len=s.length();
        String ans = "";
        for(int i=0;i< len; i++){
            for(int j= i ;j<len; j++){
                if (pali(s, i, j)) {
                    if (j - i + 1 > ans.length()) {
                        ans = s.substring(i, j + 1);
                    }
                }
            }
        }
        return ans;
    }
}