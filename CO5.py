# Probability values

P_Good = 0.7
P_HighRating_given_Good = 0.9
P_HighRating = 0.8

# Bayes Rule

P_Good_given_HighRating = (
    P_HighRating_given_Good * P_Good
) / P_HighRating

print("Probability Product is Good:")
print(P_Good_given_HighRating)