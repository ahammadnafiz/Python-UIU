import json

data_file = 'data.txt'

def load_data():
    data = []
    try:
        with open(data_file, 'r') as file:
            for line in file:
                try:
                    entry = json.loads(line.strip())  # Use json.loads to convert the string to a dictionary
                    data.append(entry)
                except json.JSONDecodeError:
                    # Handle invalid JSON in the file
                    print(f"Warning: Skipping invalid JSON in the file: {line.strip()}")
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Info: File '{data_file}' not found.")
    return data

def save_data(data):
    with open(data_file, 'w') as file:
        for entry in data:
            try:
                file.write(json.dumps(entry) + '\n')  # Use json.dumps to convert the dictionary to a string
            except TypeError:
                # Handle non-serializable data
                print(f"Error: Unable to serialize data: {entry}")

def main():
    pass

if __name__ == '__main__':
    main()
