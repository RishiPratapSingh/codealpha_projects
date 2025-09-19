import re

def extract_emails(input_file, output_file):
    try:
        # Read the content of the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Regular expression pattern for matching email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # Find all email addresses using regex
        emails = re.findall(email_pattern, content)
        
        # Remove duplicates by converting list to a set
        unique_emails = set(emails)
        
        # Write the unique emails to the output file
        with open(output_file, 'w') as file:
            for email in unique_emails:
                file.write(email + '\n')
        
        print(f"Extraction complete! {len(unique_emails)} unique emails saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = 'sample.txt'   
output_file = 'emails.txt' 


extract_emails(input_file, output_file)
