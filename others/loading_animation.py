import sys
import os
import time
def loadingAnimation(text):
    print(f"\n{text}: ", end="")
    for _ in range(3):  # Repeat 3 times for dots
        sys.stdout.write(".")
        sys.stdout.flush()  # Force the dot to appear immediately
        time.sleep(0.5)  # Wait half a second between dots
    print()  # New line after loading    
    if os.name == 'nt':
            _ = os.system('cls')
        # For Mac and Linux
    else:
        _ = os.system('clear')

