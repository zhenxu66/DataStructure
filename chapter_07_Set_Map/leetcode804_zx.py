class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        lookup = [".-", "-...", "-.-.", "-..", ".", "..-.",
                  "--.", "....", "..", ".---", "-.-", ".-..",
                  "--", "-.", "---", ".--.", "--.-", ".-.", "...",
                  "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        # ord(char) return unicode number
        # python set automatic remove duplicates
        s = [''.join([lookup[ord(c) - ord('a')] for c in word]) for word in words]
        return len(set(s))

if __name__ == '__main__':

    minStack = Solution();
    print(minStack.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]));
