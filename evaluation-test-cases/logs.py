import json

# Download the logs.zip from:
# https://tds-llm-analysis.s-anand.net/project2/logs.zip

# Read the JSONL file (you'll need to extract logs.zip first)
filename = "logs.jsonl"  # Update path if needed

total_bytes = 0
count = 0

try:
    with open(filename, 'r') as f:
        for line in f:
            data = json.loads(line.strip())
            if data.get('event') == 'download':
                total_bytes += data.get('bytes', 0)
                count += 1
                print(f"Download event: {data.get('bytes')} bytes")
    
    print(f"\n{'='*50}")
    print(f"Total download events: {count}")
    print(f"Sum of bytes: {total_bytes}")
    
    # Calculate offset
    email = "24ds1000070@ds.study.iitm.ac.in"
    email_length = len(email)
    offset = email_length % 5
    
    answer = total_bytes + offset
    
    print(f"Email length: {email_length}")
    print(f"Offset (email_length mod 5): {offset}")
    print(f"{'='*50}")
    print(f"ANSWER: {answer}")
    print(f"{'='*50}")
    
except FileNotFoundError:
    print(f"Error: {filename} not found!")
    print("Please download and extract logs.zip first:")
    print("https://tds-llm-analysis.s-anand.net/project2/logs.zip")