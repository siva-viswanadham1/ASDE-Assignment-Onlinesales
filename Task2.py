import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            
            # Read and print the header
            header = csv_reader.fieldnames
            print("Header:", header)
            
            # Read and print each row of data
            for row in csv_reader:
                print("Row:", row)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred")

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file:")
    read_csv_file(file_path)


