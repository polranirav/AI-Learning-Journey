import json

# JSON string (like from an API)
json_str = '{"project": "AI Genie", "version": 1.0, "active": true}'

# Convert string to dict
data = json.loads(json_str)
print("Parsed JSON (string → dict):", data)

# Convert dict to string
json_out = json.dumps(data, indent=2)
print("Back to JSON string:\n", json_out)