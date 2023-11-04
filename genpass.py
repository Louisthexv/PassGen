import csv
import random
import unicodedata

# Load a Spanish dictionary
def load_spanish_dictionary(dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

# Remove accents and unwanted characters
def sanitize(word):
    # Remove accents and unwanted characters
    word = unicodedata.normalize('NFKD', word)
    word = ''.join([c for c in word if not unicodedata.combining(c) and ord(c) < 128])
    return word

# Generate a new passphrase
def generate_passphrase(dictionaries):
    word1 = sanitize(random.choice(dictionaries))
    word2 = sanitize(random.choice(dictionaries))
    random_number = random.randint(99, 9999)
    return f"{word1}-{word2}-{random_number:04d}"

# Read the input CSV file
def read_csv_file(input_file):
    data = []
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Update the CSV data with new passwords starting from column C2
def update_csv_data(data, dictionaries):
    for row in data[1:]:
        row.append(generate_passphrase(dictionaries))

# Create a new CSV file with updated data
def create_new_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"
    spanish_dictionary_file = "spanish_dictionary.txt"

    spanish_words = [sanitize(word) for word in load_spanish_dictionary(spanish_dictionary_file)]
    data = read_csv_file(input_file)
    data[0].append("new_password")  # Add "new_password" to the header
    update_csv_data(data, spanish_words)
    create_new_csv(data, output_file)
    print(f"New passwords have been generated and saved in {output_file}.")
