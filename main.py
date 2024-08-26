import pandas as pd

def check_data_size(input_file):
    """
    Checks the size of the data and allows the user to reduce it.
    
    Parameters:
    - input_file: str, path to the input CSV file
    """
    # Load the data
    df = pd.read_csv(input_file)
    
    # Get the number of rows
    num_rows = len(df)
    print(f"The dataset contains {num_rows} rows.")
    
    # Ask the user how many rows they want to keep
    while True:
        try:
            target_rows = int(input(f"Enter the number of rows you want to reduce the data to (max {num_rows}): "))
            if target_rows <= 0 or target_rows > num_rows:
                print(f"Please enter a number between 1 and {num_rows}.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Sample the data to the desired number of rows
    if target_rows < num_rows:
        df = df.sample(n=target_rows, random_state=42)
    
    # Generate output file name
    output_file = input_file.replace(".csv", "1.csv")
    
    # Save the reduced data
    df.to_csv(output_file, index=False)
    print(f"Data reduced to {target_rows} rows and saved to {output_file}")

# Path to your specific file
input_file = 'C:/Users/Moussa/Downloads/Pump-and-Dump-Detection-on-Cryptocurrency-master/Pump-and-Dump-Detection-on-Cryptocurrency-master/TargetCoinPrediction/FeatGeneration/feature/train_sample.csv'

# Call the function with the path to your file
check_data_size(input_file)
