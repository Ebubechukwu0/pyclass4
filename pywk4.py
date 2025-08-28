#File Read & Write Challenge : Create a program that reads a file and writes a modified version to a new file.
#Error Handling Lab : Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.

def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Example modification: convert to uppercase

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}' or write to '{output_filename}'.")

if __name__ == "__main__":
    input_file = input("Enter the input filename: ")
    output_file = input("Enter the output filename: ")
    read_and_modify_file(input_file, output_file)
