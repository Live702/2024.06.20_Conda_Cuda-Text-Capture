# Check if Python is installed
import sys
print(sys.version)

# Check if Anaconda is installed
try:
    import conda
    print("Conda is installed.")
except ImportError:
    print("Conda is not installed.")
