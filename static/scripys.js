document.addEventListener("DOMContentLoaded", function () {
    // Fetch and display events
    fetchEvents();

    // Event form submission
    document.getElementById("event-form").addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById("event-name").value;
        const description = document.getElementById("event-description").value;
        const location = document.getElementById("event-location").value;
        const date = document.getElementById("event-date").value;

        fetch("/api/events/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, description, location, date }),
        })
            .then((response) => response.json())
            .then(() => {
                fetchEvents();
                document.getElementById("event-form").reset();
            });
    });

    // Fetch and display attendees
    fetchAttendees();

    // Attendee form submission
    document.getElementById("attendee-form").addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById("attendee-name").value;
        const email = document.getElementById("attendee-email").value;

        fetch("/api/attendees/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, email }),
        })
            .then((response) => response.json())
            .then(() => {
                fetchAttendees();
                document.getElementById("attendee-form").reset();
            });
    });

    // Fetch and display tasks
    fetchTasks();

    // Task form submission
    document.getElementById("task-form").addEventListener("submit", function (e) {
        e.preventDefault();
        const description = document.getElementById("task-description").value;
        const event = document.getElementById("task-event").value;

        fetch("/api/tasks/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ description, event }),
        })
            .then((response) => response.json())
            .then(() => {
                fetchTasks();
                document.getElementById("task-form").reset();
            });
    });
});

function fetchEvents() {
    fetch("/api/events/")
        .then((response) => response.json())
        .then((events) => {
            const eventList = document.getElementById("event-list");
            eventList.innerHTML = events
                .map(
                    (event) =>
                        `<div class="list-item">
                            <div>
                                <strong>${event.name}</strong>
                                <p>${event.description}</p>
                                <p>${event.location} - ${event.date}</p>
                            </div>
                            <button onclick="deleteEvent(${event.id})">Delete</button>
                        </div>`
                )
                .join("");
        });
}

function fetchAttendees() {
    fetch("/api/attendees/")
        .then((response) => response.json())
        .then((attendees) => {
            const attendeeList = document.getElementById("attendee-list");
            attendeeList.innerHTML = attendees
                .map(
                    (attendee) =>
                        `<div class="list-item">
                            <div>
                                <strong>${attendee.name}</strong>
                                <p>${attendee.email}</p>
                            </div>
                            <button onclick="deleteAttendee(${attendee.id})">Delete</button>
                        </div>`
                )
                .join("");
        });
}

function fetchTasks() {
    fetch("/api/tasks/")
        .then((response) => response.json())
        .then((tasks) => {
            const taskList = document.getElementById("task-list");
            taskList.innerHTML = tasks
                .map(
                    (task) =>
                        `<div class="list-item">
                            <div>
                                <strong>${task.description}</strong>
                                <p>Event: ${task.event.name}</p>
                                <p>Status: ${task.status}</p>
                            </div>
                            <button onclick="updateTask(${task.id})">Mark Completed</button>
                        </div>`
                )
                .join("");
        });
}

function deleteEvent(eventId) {
    fetch(`/api/events/${eventId}/`, { method: "DELETE" }).then(() => fetchEvents());
}

function deleteAttendee(attendeeId) {
    fetch(`/api/attendees/${attendeeId}/`, { method: "DELETE" }).then(() => fetchAttendees());
}

function updateTask(taskId) {
    fetch(`/api/tasks/${taskId}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ status: "Completed" }),
    }).then(() => fetchTasks());
}
