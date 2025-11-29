import json
import math

# Read constraints
with open('shards.json', 'r') as f:
    constraints = json.load(f)

dataset = constraints['dataset']
max_docs_per_shard = constraints['max_docs_per_shard']
max_shards = constraints['max_shards']
min_replicas = constraints['min_replicas']
max_replicas = constraints['max_replicas']
memory_per_shard = constraints['memory_per_shard']
memory_budget = constraints['memory_budget']

print("Constraints:")
print(f"  Dataset: {dataset} docs")
print(f"  Max docs per shard: {max_docs_per_shard}")
print(f"  Max shards: {max_shards}")
print(f"  Replicas: {min_replicas}-{max_replicas}")
print(f"  Memory per shard: {memory_per_shard} GB")
print(f"  Memory budget: {memory_budget} GB")
print()

# Calculate minimum shards needed
min_shards_needed = math.ceil(dataset / max_docs_per_shard)
print(f"Minimum shards needed (dataset/max_docs_per_shard): {min_shards_needed}")

# Try all valid combinations
best_solution = None
best_score = -1

for shards in range(min_shards_needed, max_shards + 1):
    for replicas in range(min_replicas, max_replicas + 1):
        # Check memory constraint
        total_memory = shards * replicas * memory_per_shard
        
        if total_memory <= memory_budget:
            # Valid solution - score by total capacity or minimizing resources
            # Higher shards and replicas = better (more capacity/redundancy)
            score = shards * replicas
            
            if score > best_score:
                best_score = score
                best_solution = {
                    "shards": shards,
                    "replicas": replicas,
                    "total_memory": total_memory
                }

print()
print("="*50)
if best_solution:
    print("BEST SOLUTION:")
    print(f"  Shards: {best_solution['shards']}")
    print(f"  Replicas: {best_solution['replicas']}")
    print(f"  Total memory: {best_solution['total_memory']} GB (budget: {memory_budget} GB)")
    print()
    
    answer = {
        "shards": best_solution['shards'],
        "replicas": best_solution['replicas']
    }
    
    print("ANSWER (JSON):")
    print(json.dumps(answer))
else:
    print("NO VALID SOLUTION FOUND")
print("="*50)