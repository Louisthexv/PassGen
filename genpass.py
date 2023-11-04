
import csv
import random
from unidecode import unidecode

# Load a Spanish dictionary
def load_spanish_dictionary(dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file]
    return words

# Remove accents from words
def remove_accents(word):
    return unidecode(word)

# Capitalize the first word
def capitalize_first_word(word):
    return word.capitalize()

# Generate a new passphrase
def generate_passphrase(dictionaries, length):
    words = [random.choice(dictionaries) for _ in range(length - 1)]
    first_word = capitalize_first_word(remove_accents(random.choice(dictionaries)))
    random_number = random.randint(1000, 9999)
    return f"{first_word}-{'-'.join(words)}-{random_number}"

# Read the input CSV file
def read_csv_file(input_file):
    data = []
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# Update the CSV data with new passwords
def update_csv_data(data, dictionaries):
    for row in data:
        row[2] = generate_passphrase(dictionaries, 4)  # Assuming the 'new_password' column is at index 2

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

    spanish_words = load_spanish_dictionary(spanish_dictionary_file)
    data = read_csv_file(input_file)
    update_csv_data(data, spanish_words)
    create_new_csv(data, output_file)
    print(f"New passwords have been generated and saved in {output_file}.")
