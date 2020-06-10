import codecademylib
import numpy as np
calories_stats = np.genfromtxt('cereal.csv', delimiter=",")
average_calories = np.mean(calories_stats)
print(average_calories)
calorie_stats_sorted = np.sort(calories_stats)
print(calorie_stats_sorted)
median_calories = np.median(calorie_stats_sorted)
print(median_calories)
print(np.percentile(calories_stats, 4))
nth_percentile = 4
more_calories = np.mean(calories_stats > 60)
print(more_calories)
calorie_std = np.std(calories_stats)
print(calorie_std)
print(len(calories_stats))