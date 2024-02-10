def word_count(text):
    words = text.split()
    return len(words)

def main():
    try:
        input_user = input("Enter a sentence or paragraph: ")

        if not input_user.strip():
            raise ValueError("Empty input!!! Please enter some text.")

        count = word_count(input_user)
        print("Word count:", count)
    
    except Exception as e:
        print("An error occurred:", e)
        main()

if __name__ == "__main__":
    main()
