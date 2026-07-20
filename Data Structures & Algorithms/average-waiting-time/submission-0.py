class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # wait time = end time - arrive time for customer i
        # end time = start cook time + prepare time
        # wait time = max(prev end time, arrive time) + prepare time - arrive time
        n = len(customers)
        total = 0
        prev_end = None

        for arrive, prepare in customers:
            if not prev_end:
                prev_end = arrive + prepare
                total += prepare
                continue
            end = max(prev_end, arrive) + prepare
            wait = end - arrive
            total += wait
            prev_end = end
        return total / n
        