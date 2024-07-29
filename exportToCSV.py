import csv
import os

def write_results_to_csv(results, csv_file):
    # Delete the CSV file if it exists
    if os.path.exists(csv_file):
        os.remove(csv_file)

    # Extract headers
    headers = ['URL', 'PAGETITLE', 'STATUSCODE', 'EMAIL']

    # Write to CSV file
    # with open(csv_file, 'a', newline='', encoding='utf-8') as file: # append
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        # for result in results:
        #     writer.writerow([result['URL'], result['PAGETITLE'], result['STATUSCODE'], result['EMAIL']])
        for result in results:
            # Ensure all entries are strings and correctly encoded
            writer.writerow([
                result.get('URL', ''),
                result.get('PAGETITLE', ''),
                result.get('STATUSCODE', ''),
                result.get('EMAIL', '')
            ])

if __name__ == "__main__":
    # for tests
    results = [
        {'URL': 'https://example.com', 'PAGETITLE': 'Example Ü', 'STATUSCODE': 200, 'EMAIL': 'example@example.com'},
        {'URL': 'https://example.de', 'PAGETITLE': 'Beispiel Ä', 'STATUSCODE': 200, 'EMAIL': 'beispiel@example.de'}
    ]
    csv_file = 'moodle_status.csv'
    write_results_to_csv(results, csv_file)
    print(f"Test entries written into {csv_file}")