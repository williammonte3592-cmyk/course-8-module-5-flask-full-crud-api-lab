from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_id = len(events) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)
    
    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    event = None
    for e in events:
        if e.id == event_id:
            event = e
            break
    
    if not event:
        return jsonify({"error": "Event not found"}), 404
    
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    event.title = data["title"]
    
    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    
    # TODO: Task 3 - Implement the Loop and Process Each Element
    for i, e in enumerate(events):
        if e.id == event_id:
            events.pop(i)
            # TODO: Task 4 - Return and Handle Results
            return "", 204
    
    return jsonify({"error": "Event not found"}), 404

# GET /events - Return all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events])

# Welcome route
@app.route("/")
def welcome():
    return jsonify({"message": "Welcome to the Events API"})

if __name__ == "__main__":
    app.run(debug=True)