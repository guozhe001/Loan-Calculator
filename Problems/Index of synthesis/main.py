the_index_of_synthesis = float(input())

# Analytic — less than 2
#
# Synthetic — from 2 to 3 (inclusively)
#
# Polysynthetic — more than 3

if the_index_of_synthesis < 2:
    print("Analytic")
elif the_index_of_synthesis > 3:
    print("Polysynthetic")
else:
    print("Synthetic")
