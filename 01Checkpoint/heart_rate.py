"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

persons_age = int(input("what is your age? "))


max_heart_beat = 220 - persons_age

maximum = max_heart_beat * 0.85

minimum = max_heart_beat * 0.65

print(f"Since you are {persons_age} you should keep your heart rate between {minimum} bpm and {maximum} bpm when exercising")
