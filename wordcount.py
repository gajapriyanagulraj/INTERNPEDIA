import string

def count_words(text):
    
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator).lower()
    words = clean_text.split() 
    return len(words)

def get_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def word_count_tool():
    while True:
        print("\nWord Count Tool")
        print("1. Enter text manually")
        print("2. Load text from file")
        print("3. Exit")

        choice = input("Choose an option for count (1/2/3): ")

        if choice == "1":
           
            user_input = input("\nEnter the text: ")
            if user_input.strip():
                word_count = count_words(user_input)
                print(f"Word Count: {word_count}")
            else:
                print("Error: No text entered.")
        
        elif choice == "2":
            
            file_path = input("\nEnter file path: ")
            text = get_text_from_file(file_path)
            if text:
                word_count = count_words(text)
                print(f"Word Count: {word_count}")
            else:
                print("Error: No content to process.")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

word_count_tool()

