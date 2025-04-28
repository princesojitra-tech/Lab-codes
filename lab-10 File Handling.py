
# 01. Write a program to create a csv file that we can directly open in MS-Excel.

import csv
import os

def create_csv(filename):
    data = [
        ["Name", "Age", "City"],
        ["DHRUV", 18, "RAJKOT"],
        ["Rushi", 18, "Bhuj"],
        ["Dhruv", 12 , "Jamjodhpur"],
        ["Jaydev", 6 , "Jamnagar"]
    ]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print(f"CSV file '{os.path.basename(filename)}' created successfully!")

create_csv("24BCP209_LabDay10/output_10.01.csv")


# 02. Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, name of student, marks of three subjects. Also calculate total. Display the dictionary data on the monitor.

import csv

def read_csv_to_dict_and_update(filename):
    students = []

    # Read the data and calculate Total
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames + ['Total']  # Add 'Total' to the existing headers

        for row in reader:
            row['Maths'] = int(row['Maths'])
            row['Chemistry'] = int(row['Chemistry'])
            row['Physics'] = int(row['Physics'])

            total = row['Maths'] + row['Chemistry'] + row['Physics']
            row['Total'] = total

            students.append(row)

    # Write updated data back to the CSV file with the new 'Total' column
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    # Display the updated data
    for student in students:
        print(student)

print("\n")
read_csv_to_dict_and_update("24BCP209_LabDay10\Student-Data.csv")
print("\n")


# 03. Accept contact details from the user and create a vcard that we can directly store in our mobile.

import os

def create_vcard():

    # # To input specific path
    # folder_path = input("Enter the folder path where you want to save the vCard(s): ").strip()
    # # Create folder if it doesn't exist
    # if not os.path.exists(folder_path):
    #     os.makedirs(folder_path)
    #     print(f"📁 Folder '{folder_path}' created.")

    while True:
        print("\nEnter contact details:\n")
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email Address: ")
        address = input("Address: ")
        organization = input("Organization (optional): ")

        vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{full_name}
TEL;TYPE=CELL:{phone_number}
EMAIL:{email}
ADR;TYPE=HOME:;;{address}
ORG:{organization}
END:VCARD
"""

        filename = full_name.replace(" ", "_").lower() + ".vcf"
        # filepath = os.path.join(folder_path, filename)
        filepath = os.path.join("24BCP209_LabDay10/", filename)

        with open(filepath, "w") as file:
            file.write(vcard_content)

        print(f"\n✅ vCard saved as '{filepath}'. You can now transfer it to your phone and import it into your contacts.")

        another = input("\nDo you want to create another vCard? (Y/N): ").strip().upper()
        if another != 'Y':
            print("\n👋 Program terminated.")
            break

create_vcard()


# 04. Create a specific subdirectory and copy one file from another subdirectory to this newly created subdirectory

import os
import shutil

# Define source and destination paths
source_file = "/path/to/source_directory/filename.txt"
destination_dir = "/path/to/target_directory/new_folder"

# Create the new subdirectory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Copy the file
shutil.copy(source_file, destination_dir)
print("✅ File Copied!")


# 05. Write a program to copy contents of one file to another. While doing so, replace all lowercase characters into uppercase characters.

def copy_and_convert_to_upper(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        
        # Convert lowercase characters to uppercase
        upper_content = content.upper()

        with open(destination_file, 'w') as dest:
            dest.write(upper_content)

        print(f"✅ Contents copied from '{source_file}' to '{destination_file}' with lowercase converted to uppercase.")

    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


source = "24BCP209_LabDay10/test_10.05.txt"
destination = "24BCP209_LabDay10/output_10.05.txt"
copy_and_convert_to_upper(source, destination)

# 06. Write a program that merges lines alternatively from two files and writes the results to new file. If one file has less number of lines than the other,  the remaining lines from the larger file should be simply copied into the target file.

def merge_alternate_lines(file1_path, file2_path, output_path):
    def get_sentences(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            # Split by '.' and remove any trailing empty strings
            sentences = [s.strip() + '.' for s in content.split('.') if s.strip()]
        return sentences

    sentences1 = get_sentences(file1_path)
    sentences2 = get_sentences(file2_path)

    max_len = max(len(sentences1), len(sentences2))

    with open(output_path, 'w') as out:
        for i in range(max_len):
            if i < len(sentences1):
                out.write(sentences1[i] + ' ')
            if i < len(sentences2):
                out.write(sentences2[i] + ' ')

    print(f"✅ Merged sentences written to '{output_path}'.")

# Example usage
file1 = '24BCP209_LabDay10/test_10.05.txt'
file2 = '24BCP209_LabDay10/test_10.08.txt'
output_file = '24BCP209_LabDay10/output_10.06.txt'

merge_alternate_lines(file1, file2, output_file)


#7
""" 07.	If an Employee object contains following details:
empcode, empname, Date of Joining, Salary
Write a program to serialize and deserialize this data."""

import json

employee = {
    "empcode": "S597",
    "empname": "Nikunj Joshi",
    "Date of Joining": "01-09-2022",
    "Salary": 55000.00
}

# --- Serialization ---  (Convert dictionary to JSON and save to a file)
with open("24BCP209_LabDay10/employee.json", "w") as file:
    json.dump(employee, file)
print("Employee data serialized and saved to employee.json\n")

# --- Deserialization ---  (Read JSON from the file and convert back to dictionary)
with open("24BCP209_LabDay10/employee.json", "r") as file:
    loaded_employee = json.load(file)
print("Employee data deserialized:")
print(loaded_employee)

# 08. Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and replacing each one of them with a blank space.

def remove_articles(input_file, output_file):

    words_to_remove = {'a', 'an', 'the'}

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = line.split()
            new_line = ' '.join('' if word.lower() in words_to_remove else word for word in words)
            # Replace multiple spaces with single space and strip
            outfile.write(' '.join(new_line.split()) + '\n')
    print(f"✅ Program exicuted!")       

remove_articles('24BCP209_LabDay10/test_10.08.txt', '24BCP209_LabDay10/output_10.08.txt')


