################################
# Github Repo link: https://github.com/LokeshGurung5/03230161_BIA101_CAP3
# Your Name: Lokesh Gurung
# Your Section: 'B'
# Your Student ID Number: 03230161
################################
# REFERENCES
# Links that you referred while solving 
# Remarks: None
################################
# SOLUTION
# Your Solution Score: 493333
################################

def main(): 
    file_path = r"C:\Users\DELL\Desktop\BIA101b\Cap3\161.txt" # Define the path to the text file
    
    try: # Try to open and read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        total_sum = 0 # Initialize the variable to store the total sum
        
        for line in lines: # Iterate through each line in the file
            line = line.strip() # Strip whitespace from the start and end of the line

            two_digit_number = process_line(line) # Process the line to extract numbers and calculate their sum
            
            total_sum += two_digit_number # Add the processed number to the total sum
    
        print("The total sum of from the given input file", file_path,"is", total_sum) # Print the total sum after processing all lines
    
    except FileNotFoundError: # Handle the case where the file does not exist    
        print("File not found:" ,file_path)

def process_line(line):
    # Initialize pointers to scan from both ends of the line
    left_pointer = 0
    right_pointer = len(line) - 1
    
    # Variables to hold the extracted numbers
    left_number = None
    right_number = None
    
    # Scan the line from both ends until we find digits
    while left_pointer < len(line) and right_pointer >= 0:
        if left_number is None and line[left_pointer].isdigit():
            left_number = line[left_pointer]
        else:
            left_pointer += 1
        
        if right_number is None and line[right_pointer].isdigit():
            right_number = line[right_pointer]
        else:
            right_pointer -= 1
        
        # Stop scanning once we have found numbers on both sides
        if left_number is not None and right_number is not None:
            break
    
    # Calculate and return the sum based on the found numbers
    if left_number is not None and right_number is not None:
        return int(left_number + right_number)
    elif left_number is not None:
        return int(left_number * 2)
    elif right_number is not None:
        return int(right_number * 2)
    else:
        return 0

if __name__ == "__main__": # Execute the main function if the script is run directly
    main()

