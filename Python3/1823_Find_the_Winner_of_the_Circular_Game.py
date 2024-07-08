class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #playerList=range(1,n+1)
        int_players=[]
        current_num_of_players=n
        for i in range(0,n):
            int_players.append(i+1)
            #print(int_players)
        current_position=0
        while current_num_of_players>1:
        #    i=1
        #    while i<k:
        #        i+=1
        #        current_position=1
            current_position=(current_position+k-1)%current_num_of_players
            ##do we need an if?
            #current_position%
            ##
            #print("current_position",current_position)
            del int_players[current_position]
            #print(int_players)
            current_num_of_players-=1
            #print("current_num_of_players",current_num_of_players)
        #print("int_players[0]",int_players[0])
        return int_players[0]




# Create an instance of the Solution class
solution = Solution()

# Call the findTheWinner method with test inputs
n = 5  # For example, number of players
k = 2  # For example, every 3rd player is eliminated
winner = solution.findTheWinner(n, k)

print(f"The winner is player: {winner}")

