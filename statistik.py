import statistics

# Mittelwert einer Liste
probe1 = [5, 2, 4, 17]
print("Arithmetischer Mittelwert:", statistics.mean(probe1))
print("Harmonischer Mittelwert:", statistics.harmonic_mean(probe1))
print()

# Median
print("Median:", statistics.median(probe1))
probe2 = [5, 2, 4, 17, 3]
print("Median:", statistics.median(probe2))
print()

# Unterer Median
print("Unterer Median:", statistics.median_low(probe1))
print("Unterer Median:", statistics.median_low(probe2))
print()

# Oberer Median
print("Oberer Median:", statistics.median_high(probe1))
print("Oberer Median:", statistics.median_high(probe2))
print()

# Tupel, Werte eines Dictionary
probe3 = (5, 2, 4, 17)
print("aus Tupel:", statistics.mean(probe3))
probe4 = {'D':5, 'NL':2, 'CH':4, 'F':17}
print("aus Dictionary:", statistics.mean(probe4.values()))
