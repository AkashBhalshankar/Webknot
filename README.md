# Event Management Dashboard

## Project Overview

The Event Management Dashboard is a web-based application designed to streamline the process of creating, managing, and tracking events. It allows users to efficiently manage events, attendees, and tasks associated with the events. The application includes features such as event creation, task assignment, attendee management, and task progress tracking.

## Problem Statement

Organizations often face difficulties in managing events effectively. The goal of this project is to create a user-friendly and responsive dashboard that simplifies event management, attendee tracking, and task assignments. The dashboard will include CRUD operations for events, manage attendees, and track task progress.

## Features

### 1. Event Management
- Display a list of all events.
- CRUD operations: Create, Read, Update, and Delete events.
- Each event includes details like name, description, location, and date.

### 2. Attendee Management
- View and manage the list of attendees.
- Add or remove attendees from events.
- Assign attendees to specific events or tasks.

### 3. Task Tracker
- Display tasks related to each event.
- Allow users to update task status (Pending/Completed).

## UI Guidelines
- The interface is intuitive and user-friendly.
- The design is responsive, ensuring it works well on both mobile and desktop devices.
- Form validation is implemented to ensure no empty fields when adding an event or attendee.

## Backend Development

### APIs:

1. **Event Management API**:
   - `POST /events`: Create a new event.
   - `GET /events`: Get all events.
   - `PUT /events/{id}`: Update an event by ID.
   - `DELETE /events/{id}`: Delete an event by ID.

2. **Attendee Management API**:
   - `POST /attendees`: Add a new attendee.
   - `GET /attendees`: Get all attendees.
   - `DELETE /attendees/{id}`: Delete an attendee by ID.

3. **Task Management API**:
   - `POST /tasks`: Create a new task.
   - `GET /tasks/{eventId}`: Get tasks for a specific event.
   - `PUT /tasks/{taskId}`: Update task status (Pending/Completed).

## Integration
- Frontend is integrated with the backend APIs to fetch and display real-time data.
- Success and error messages are displayed for API calls.
- Loading indicators are shown while waiting for API responses.

## Constraints
- Each event has the following attributes: Name, Description, Location, Date, and a List of Attendees.
- Each task has the following attributes: Name, Deadline, Status (Pending/Completed), and Assigned Attendee.
- Form inputs are validated for correctness (e.g., no empty fields, valid dates).




### Installing Dependencies

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/AkashBhalshankar/Webknot.git
