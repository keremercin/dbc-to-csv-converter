import cantools
import pandas as pd

def process_dbc(dbc_file_path, output_csv_path):
    # Load the DBC file
    db = cantools.database.load_file(dbc_file_path)

    # Create a list to store messages and signals
    messages_sigs = []

    # Loop through each message and signal in the DBC file
    for message in db.messages:
        for signal in message.signals:
            messages_sigs.append({
                'Message Name': message.name,
                'Message ID': message.frame_id,
                'Signal Name': signal.name,
                'Signal Start Bit': signal.start,
                'Signal Length': signal.length,
                'Signal Scale': signal.scale,
                'Signal Offset': signal.offset,
                'Signal Minimum': signal.minimum,
                'Signal Maximum': signal.maximum,
                'Signal Unit': signal.unit
            })

    # Create a DataFrame
    df = pd.DataFrame(messages_sigs)

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv_path, index=False)

    print(f"DBC data has been successfully saved to {output_csv_path}")

if __name__ == "__main__":
    dbc_file_path = "path/to/your/dbc_file.dbc"  # Change this to the path of your DBC file
    output_csv_path = "path/to/your/output_file.csv"  # Change this to the path where you want to save the CSV file
    process_dbc(dbc_file_path, output_csv_path)
