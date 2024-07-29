import csv


def filter_csv(input_file, output_file):
    # Open the input CSV file for reading
    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Get the fieldnames from the input file
        fieldnames = reader.fieldnames

        # Open the output CSV file for writing
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # Write the header to the output file
            writer.writeheader()

            # Iterate through each row in the input file
            for row in reader:
                # Check if 'URL' contains '.fr' or '.uk'
                if '.uk' not in row['URL']:
                    # Write the row to the output file if it does not contain '.fr' or '.uk'
                    writer.writerow(row)


if __name__ == "__main__":
    # Specify input and output file paths
    input_csv = 'moodle_status.csv'  # Replace with the path to your input CSV file
    output_csv = 'filtered_moodle_status.csv'  # Replace with the path to your output CSV file

    filter_csv(input_csv, output_csv)
    print(f"Filtered data saved to {output_csv}")
