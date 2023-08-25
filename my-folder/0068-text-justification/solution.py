class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        
        while i < len(words):
            line = []
            line_width = maxWidth
            
            # Add words to the current line until it's not possible
            while i < len(words) and len(words[i]) <= line_width:
                line.append(words[i])
                line_width -= len(words[i]) + 1  # Account for the space after the word
                i += 1
            
            # Justify the line
            if i < len(words) and len(line) > 1:
                spaces_to_add = maxWidth - sum(len(word) for word in line)
                num_gaps = len(line) - 1
                spaces_between_words = [" " * (spaces_to_add // num_gaps + (j < spaces_to_add % num_gaps)) for j in range(num_gaps)]
                justified_line = "".join([word + space for word, space in zip(line, spaces_between_words)]) + line[-1]
            else:
                justified_line = " ".join(line).ljust(maxWidth)
            
            result.append(justified_line)
        
        return result

