import itertools

def generate_combinations(characters, length, filename):
    if length <= 0:
        print("Combination length should be greater than 0.")
        return
    
    combinations = [''.join(combination) for combination in itertools.product(characters, repeat=length)]
    
    with open(filename, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')
    
    print(f"All {length}-character combinations saved to '{filename}'.")

if __name__ == "__main__":
    input_characters = input("Enter characters for combinations: ")
    combination_length = int(input("Enter combination length: "))
    output_filename = input("Enter output filename: ")
    generate_combinations(input_characters, combination_length, output_filename)
