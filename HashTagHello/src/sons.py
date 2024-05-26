import winsound

INITIAL_FREQUENCY = 37
FINAL_FREQUENCY = 20000
STEP_FREQUENCY = 66
BEEP_DURATION = 700

for freq in range(INITIAL_FREQUENCY, FINAL_FREQUENCY, STEP_FREQUENCY):
    winsound.Beep(freq, BEEP_DURATION)
    print(f"Frequencia tocada: {freq}Hz")
