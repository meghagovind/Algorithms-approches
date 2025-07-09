# Problem:
# Select the maximum number of non-overlapping activities from a list.

# Greedy Approach: Always pick the activity that ends earliest.
# Algorithm Steps:
# Sort activities by finish time (earliest first).

# Select the first activity (earliest finish).

# Skip all overlapping activities.

# Repeat for the next non-overlapping one.

# Example:
# Activity	Start	End
# A	1	4
# B	3	5
# C	0	6
# D	5	7
# E	8	9
# Step-by-Step Selection:

# Sort by end time: [A(1-4), B(3-5), C(0-6), D(5-7), E(8-9)].

# Pick A (ends at 4).

# Skip B & C (overlap with A).

# Pick D (starts at 5, ends at 7).

# Pick E (starts at 8).

# Final Selection: [A, D, E] (3 activities).

def activitySelection(acts):
    acts.sort(key=lambda x : x[1])
    section = [acts[0]]
    for i in acts[1:]:
        if i[0] > section[-1][1]:
            section.append(i)
    return section

acts = [(1,4), (3,5), (0,6),(5,7),(8,9)]
print(activitySelection(acts))
    

