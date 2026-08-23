class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string = encoded_string + "228" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split("228")
        if "" in decoded_strs:
            decoded_strs.remove("")

        return decoded_strs