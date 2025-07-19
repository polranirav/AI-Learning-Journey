# Combination of multiple structures

complex_data = {
    "name": "Nirav",
    "courses": ["Python", "ML", "AI"],
    "grades": {"Python": 90, "ML": 85},
    "projects": [
        {"title": "Chatbot", "status": "Completed"},
        {"title": "Recommender", "status": "Ongoing"}
    ]
}

print("First course:", complex_data["courses"][0])
print("ML grade:", complex_data["grades"]["ML"])
print("Project title:", complex_data["projects"][1]["title"])