date1="2020-01-15"
date2 = "2019-12-31"

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split('-')
        # Base case
        if date1<1979 or date1 >2100:
            return 0


