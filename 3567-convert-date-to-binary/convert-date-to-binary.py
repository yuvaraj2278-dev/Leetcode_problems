class Solution:
    def convertDateToBinary(self, date: str) -> str:
        def to_binary(num):
            return bin(int(num))[2:]  # Remove '0b' prefix

        year, month, day = date.split("-")
        return f"{to_binary(year)}-{to_binary(month)}-{to_binary(day)}"