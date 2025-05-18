class Solution:
    def decodeString(self, s: str) -> str:


        # "3[a12[bc]]"

        # "3"

        st = []

        for i in range(len(s)):

            if s[i] != "]":
                st.append(s[i])

            else:

                substr = ""

                while st and st[-1] != "[":
                    substr = st.pop() + substr

                st.pop()

                k = ""

                while st and st[-1].isdigit():
                    k = st.pop() + k

                st.append(substr * int(k))

        return "".join(st)

                



        