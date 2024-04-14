'''
Design a program for your university's annual sports day, where traditional paper
records are replaced by a sensor-based system to determine the winners of a 10m
race. The program should accept participants' finish times as input, with each index
representing a participant number and the value at that index representing their
finish time in seconds. The program should then identify and display the participants
who secured the first, second, and third positions. There can never be two or more
participants that finish at the same time.
'''

player_position = list(map(int, input().split()))  # Prompt the user to input the participants' finish times as a space-separated list of integers and convert it to a list

unique_player_position = list(set(player_position))  # Get the unique elements in player_position and convert them to a list
sorted_index = []  # Initialize an empty list to store the sorted indices

for i in sorted(unique_player_position):  # Iterate over the sorted unique elements in unique_player_position
    sorted_index.append(player_position.index(i))  # Find the index of each element in player_position and append it to sorted_index

print(f"First place: {sorted_index[0]}\nSecond place: {sorted_index[1]}\nThird place: {sorted_index[2]}")  # Print the first, second, and third place positions based on the sorted indices

