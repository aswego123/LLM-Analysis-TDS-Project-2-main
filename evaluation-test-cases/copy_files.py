import shutil
import os

files_to_copy = [
    'answer.json',
    'cache_answer.txt',
    'cache_submit.json',
    'gh_counter.py',
    'logs.jsonl',
    'logs.py',
    'order.py',
    'orders.csv',
    'shards.json',
    'shards_optimizer.py',
    'shards_submit.json',
    'tree.json'
]

dest_dir = '../evaluation-test-cases'
os.makedirs(dest_dir, exist_ok=True)

for file in files_to_copy:
    if os.path.exists(file):
        shutil.copy2(file, os.path.join(dest_dir, file))
        print(f"Copied: {file}")
    else:
        print(f"Not found: {file}")

print("Done!")