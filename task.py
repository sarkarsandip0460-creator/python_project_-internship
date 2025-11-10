import json

class Task:
    def _init_(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority

    def to_dict(self):
        """Convert Task object to dictionary for JSON storage"""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority
        }

    @staticmethod
    def from_dict(data):
        """Convert dictionary back to Task object"""
        return Task(
            title=data.get("title", ""),
            description=data.get("description", ""),
            priority=data.get("priority", "Low")
        )

    def _str_(self):
        return f"{self.title} ({self.priority}) - {self.description}"