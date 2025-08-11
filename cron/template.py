import csv
import requests
import json
from typing import Optional, Tuple, Dict, Any
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# example configuration
example_URL = "http://example.com/api/dataset"
SESSION_COOKIE = "1f1bce53-aaaa-bbbb-cccc-7467a28b6af4"
DATABASE_ID = 12

def get_example_data(a1: str) -> Tuple[Optional[str], Optional[str], Optional[int]]:
    """
    Call example API to get a1,a2,a3 for a given a1.
    Returns tuple of (a1,a2,a3) or (None, None, None) if no data found.
    """
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8,ja;q=0.7,ko;q=0.6,zh;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'DNT': '1',
        'Origin': 'http://example.com',
        'Pragma': 'no-cache',
        'Referer': 'http://example.com/question',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }
    
    cookies = {
        'example.SESSION': SESSION_COOKIE
    }
    
    # Prepare the query with the specific a1
    query = f"select a1,a2,a3 from table where id = '{a1}';"
    
    payload = {
        "type": "native",
        "native": {
            "query": query,
            "template-tags": {}
        },
        "database": DATABASE_ID,
        "parameters": []
    }
    
    try:
        response = requests.post(
            example_URL,
            headers=headers,
            cookies=cookies,
            json=payload,
            verify=False,  # --insecure flag equivalent, disable for internal network
            timeout=15  # Reduced timeout for faster failure detection in multithreaded environment
        )
        response.raise_for_a3()
        
        data = response.json()
        
        # Check if we have data rows
        if data.get('data', {}).get('rows') and len(data['data']['rows']) > 0:
            # Extract the first row data
            row_data = data['data']['rows'][0]
            a1 = row_data[0] if len(row_data) > 0 else None
            a3 = row_data[1] if len(row_data) > 1 else None
            a2 = row_data[2] if len(row_data) > 2 else None
            
            return a1, a2, a3
        else:
            # No data found
            return None, None, None
            
    except requests.exceptions.RequestException as e:
        print(f"Error calling API for a1 {a1}: {e}")
        return None, None, None
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Error parsing response for a1 {a1}: {e}")
        return None, None, None

def process_row(row_data: Tuple[int, Dict[str, str]]) -> Dict[str, Any]:
    """
    Process a single row by calling the example API.
    Returns the row data with additional columns.
    """
    row_index, row = row_data
    a1 = row['a1']
    
    # Get data from example API
    a1, a2, a3 = get_example_data(a1)
    
    # Add new columns to the row
    result_row = row.copy()
    result_row['a1'] = a1
    result_row['a2'] = a2
    result_row['a3'] = a3
    result_row['_row_index'] = row_index  # Keep track of original order
    
    # Sleep to avoid overwhelming the API
    time.sleep(0.1)
    
    return result_row

def process_csv_file(input_file: str, output_file: str, max_workers: int = 10):
    """
    Process the input CSV file and create output CSV with additional columns using multithreading.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path to output CSV file
        max_workers: Maximum number of concurrent threads (default: 10)
    """
    print(f"Starting CSV processing with {max_workers} worker threads...")
    
    # First, read all rows from the input file
    rows_to_process = []
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = list(reader.fieldnames) + ['a1', 'a2', 'a3']
        
        for index, row in enumerate(reader):
            rows_to_process.append((index, row))
    
    total_rows = len(rows_to_process)
    print(f"Found {total_rows} rows to process")
    
    # Process rows concurrently
    processed_rows = []
    completed_count = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_row = {executor.submit(process_row, row_data): row_data for row_data in rows_to_process}
        
        # Collect results as they complete
        for future in as_completed(future_to_row):
            try:
                result_row = future.result()
                processed_rows.append(result_row)
                completed_count += 1
                
                if completed_count % 100 == 0 or completed_count == total_rows:
                    print(f"Completed {completed_count}/{total_rows} rows ({completed_count/total_rows*100:.1f}%)")
                    
            except Exception as e:
                row_data = future_to_row[future]
                print(f"Error processing row {row_data[0]}: {e}")
                # Create a row with null values for failed requests
                failed_row = row_data[1].copy()
                failed_row['a1'] = None
                failed_row['a2'] = None
                failed_row['a3'] = None
                failed_row['_row_index'] = row_data[0]
                processed_rows.append(failed_row)
                completed_count += 1
    
    # Sort results by original row index to maintain order
    processed_rows.sort(key=lambda x: x['_row_index'])
    
    # Write results to output file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in processed_rows:
            # Remove the temporary index field
            row.pop('_row_index', None)
            writer.writerow(row)

if __name__ == "__main__":
    input_csv = "data.csv"
    output_csv = "data_res.csv"
    
    # Configure number of worker threads (adjust based on your API rate limits)
    max_workers = 20  # You can adjust this based on your needs and API limits
    
    print("Starting multithreaded CSV processing with example API calls...")
    process_csv_file(input_csv, output_csv, max_workers)
    print(f"Processing completed! Output saved to: {output_csv}")

# Original curl command for reference:
