import re
import csv
md_file_path = "evadb-venv\content\All.md"
# Read the content of the MD file
with open(md_file_path, "r", encoding="utf-8") as md_file:
    markdown_content = md_file.read()
# Define a modified table_pattern to capture the 2nd and 3rd items
table_pattern = r"\|([^|]+)\|([^|]+)\|([^|]+)\|[^|]*\|[^|]*\|[^|]*\|"
# Find all matches in the Markdown content
table_matches = re.findall(table_pattern, markdown_content)
# Create a list of pairs containing the 2nd and 3rd items
data = [(match[1].strip(), match[2].strip()) for match in table_matches]
# Filter out rows where either English or Chinese is missing
filtered_data = [(english, chinese) for english, chinese in data if english and chinese]
# Specify the CSV file path
csv_file = 'output.csv'
# Write the filtered data to a CSV file with 'utf-8' encoding
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the header row
    csv_writer.writerow(['English', 'Chinese'])
    # Write the filtered data rows
    for row in filtered_data:
        csv_writer.writerow(row)