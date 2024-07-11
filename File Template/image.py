input_file_name = 'input_image.jpg'
output_file_name = 'output_image.jpg'

def open_and_save_image(input_file, output_file):
    try:
        with open(input_file, 'rb') as in_file:
            with open(output_file, 'wb') as out_file:
                out_file.write(in_file.read())
        print(f"Info: Image successfully saved to '{output_file}'.")
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        # Handle unexpected exceptions
        print(f"Error: An unexpected error occurred while processing the image: {e}")

def main():
    # Example usage:
    # open_and_save_image(input_file_name, output_file_name)
    pass

if __name__ == '__main__':
    main()
