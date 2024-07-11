file_name = 'demo.txt'

def load_data():
    content = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                content.append(line.strip())  # Remove newline characters
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Info: File '{file_name}' not found.")
    except Exception as e:
        # Handle unexpected exceptions
        print(f"Error: An unexpected error occurred while loading data: {e}")
    return content

def save_data(data):
    try:
        with open(file_name, 'w') as file:
            for line in data:
                file.write(f"{line}\n")
    except Exception as e:
        # Handle unexpected exceptions
        print(f"Error: An unexpected error occurred while saving data: {e}")

def main():
    pass

if __name__ == '__main__':
    main()
