import java.util.ArrayList;
import java.util.List;
 
class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
 
        int len = 0;
        int start = 0;
        int i = 0;
        for (; i < words.length; i++) {
            if (len + i - start + words[i].length() <= maxWidth) {
                len += words[i].length();
                continue;
            }
            result.add(compileText(maxWidth - len, start, i, words).toString());
            start = i;
            len = words[i].length();
        }
 
        int n = maxWidth - len - (i - start - 1);
        StringBuilder sb = compileText(i - start - 1, start, i, words);
        for (int j = 0; j < n; j++) {
            sb.append(" ");
        }
 
        result.add(sb.toString());
 
        return result;
    }
 
    public StringBuilder compileText(int maxSpace, int start, int end, String[] words) {
        StringBuilder sb = new StringBuilder();
        int space = maxSpace;
        for (int i = start; i < end; i++) {
            sb.append(words[i]);
 
            space = maxSpace;
            int n = end - i - 1;
            if (n > 1) {
                space = (int) Math.ceil((double) maxSpace / (double) n);
            }
 
            for (int j = 0; j < space; j++) {
                sb.append(" ");
            }
 
            maxSpace -= space;
        }
 
        return sb;
    }
}
