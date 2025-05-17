import pandas as pd
import os

def create_dataset():
    # Create data
    data = {
        'id': [1, 2, 3, 4, 5, 6, 7],
        'name': ['John', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Save to CSV
    df.to_csv('data/data.csv', index=False)
    print(f"Dataset created and saved to data/data.csv")
    print("Dataset preview:")
    print(df)

if __name__ == "__main__":
    create_dataset()
