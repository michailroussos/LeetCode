class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        total_waiting_time=0
        busy_until=-1
        current_time=0
        
        for customer in customers:
            current_time=customer[0]
            order_duration=customer[1]
            if busy_until<current_time:
                total_waiting_time=total_waiting_time+order_duration
                busy_until= current_time+order_duration
            else:
                total_waiting_time=total_waiting_time+ busy_until-current_time + order_duration
                busy_until= busy_until+order_duration

        return total_waiting_time/len(customers)



        



# Create an instance of the Solution class
solution = Solution()

# Call the averageWaitingTime method with test input
customers = [[1,2],[2,5],[4,3]]
time = solution.averageWaitingTime(customers)

print(f"The average waiting time is : {time}")
