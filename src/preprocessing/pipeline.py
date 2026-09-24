from . import *

def main():

    df = load_data(INPUT_DIR)

    cleaned_data = clean_data(df)

    return cleaned_data

if __name__ == "__main__":
    main()
