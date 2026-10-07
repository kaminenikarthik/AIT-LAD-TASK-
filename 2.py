def hill_climbing(signal, start):
    current = start
    while True:
        next_pos = current
        if current > 0 and signal[current - 1] > signal[next_pos]:
            next_pos = current - 1
        if current < len(signal) - 1 and signal[current + 1] > signal[next_pos]:
            next_pos = current + 1
        if next_pos == current:
            break
        current = next_pos
    return current

signal = [15, 25, 35, 60, 50, 45, 30]
start = 0
best = hill_climbing(signal, start)
print("Signal Strengths:", signal)
print("Starting Tower Index:", start)
print("Best Tower Index:", best)
print("Strongest Signal:", signal[best])
