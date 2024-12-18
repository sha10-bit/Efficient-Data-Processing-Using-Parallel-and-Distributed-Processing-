from generate_csv import generate_csv_files
from serial_processing import serial_processing
from parallel_processing import parallel_processing

def main():
    # Generate CSV files
    generate_csv_files()

    print("\n=== Serial Processing ===")
    serial_results = serial_processing()
    for result in serial_results:
        print(result)

    print("\n=== Parallel Processing ===")
    parallel_results = parallel_processing()
    for result in parallel_results:
        print(result)

if __name__ == "__main__":
    main()
