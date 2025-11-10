import re

def get_valid_string(prompt, pattern=None):
    """Ask for a valid string input with optional regex validation."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty.")
            continue
        if pattern and not re.match(pattern, value):
            print("Invalid format. Try again.")
            continue
        return value

def get_valid_priority():
    """Get valid priority: Low, Medium, or High."""
    priorities = ["low", "medium", "high"]
    while True:
        p = input("Enter priority (Low/Medium/High): ").strip().lower()
        if p in priorities:
            return p.capitalize()
        print("Invalid priority! Choose from Low, Medium, or High.")

