Smart Bus Stop Arrival Information Platform

Problem Statement

Public transportation users often face difficulties in knowing the actual bus arrival time, bus location, available routes, and nearby bus stops. Passengers may have to wait for long periods because they do not have accurate real-time information. They also may not know which route or bus is the best option for their journey.

Existing transportation systems may provide basic schedules, but passengers need a more convenient platform that combines bus information, live tracking, AI-based arrival prediction, weather information, and smart travel assistance in one place.

The Smart Bus Stop Arrival Information Platform is developed to solve these problems by providing passengers with a centralized web appladication where they can view bus stops, routes, bus information, live tracking, AI-based arrival predictions, weather updates, and other smart transportation services.

Project Objective

The main objective of this project is to develop a full-stack smart transportation web application that helps passengers:

Find available buses and bus stops
View bus routes and schedules
Track buses
Predict bus arrival times using AI
Check weather conditions before travelling
Receive smart notifications
Access bus-stop information using QR codes
Save favorite routes
Access emergency contacts
Provide feedback
Get personalized travel assistance
Project Working Flow

The application follows this overall flow:

                    USER
                     │
                     ▼
              ┌─────────────┐
              │ Home Page   │
              └──────┬──────┘
                     │
       ┌─────────────┼─────────────────┐
       │             │                 │
       ▼             ▼                 ▼
    Register        Login          Browse Pages
       │             │                 │
       ▼             ▼                 │
    MySQL DB      Authentication        │
                     │                  │
                     └────────┬─────────┘
                              │
                              ▼
                     Smart Bus Services
                              │
       ┌──────────┬───────────┼───────────┬───────────┐
       │          │           │           │           │
       ▼          ▼           ▼           ▼           ▼
    Routes    Bus Stops   Live Tracking  AI Prediction Weather
       │          │           │           │           │
       └──────────┴───────────┴───────────┴───────────┘
                              │
                              ▼
                    Smart Travel Features
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
          QR Code       Notifications     Favorites
                              │
                              ▼
                       Emergency Contact
                              │
                              ▼
                          Feedback




                          
Current Status
✅ Flask Backend
✅ MySQL Database Connection
✅ User Registration
✅ User Login
✅ Home Page
✅ Routes
✅ Bus Stops
✅ Weather Page
✅ Live Tracking Page
✅ AI Prediction Page
✅ Contact Page
✅ Responsive CSS Styling
✅ GitHub Repository

## Database Setup
1. Start MySQL Server and open MySQL Workbench or another MySQL client.
2. Create the database used by the application (for example, `smartbus`).
3. Create the tables required by your project, such as `users`, `bus_stops`, buses, routes, schedules, favorites, or feedback, according to your actual code.
4. Configure the database connection in your project's configuration file.
5. Use your own local database credentials. Do not commit passwords, API keys, or other secrets to GitHub.

Example database creation statement:

```sql
CREATE DATABASE smartbus;
```

Enhance the Favorite Routes feature in the Smart Bus Stop Arrival Information Platform by allowing users to add, view, and remove their favorite bus routes easily. Save favorite routes in the MySQL database so that each user can access their saved routes after logging in. Display route details, including bus number, starting point, destination, and estimated arrival time. Add a remove button to delete unwanted routes and provide quick access to frequently used routes. This improvement makes bus travel more convenient, saves time, and provides a personalized experience for passengers.

Improve Feedback Management

Enhance the Feedback feature in the Smart Bus Stop Arrival Information Platform by allowing users to submit ratings, suggestions, and complaints about bus services. Users can provide feedback about bus arrival times, route information, service quality, and overall user experience. Store feedback in the MySQL database so that it can be reviewed later. Add a star-rating system, a feedback category dropdown, and a confirmation message after successful submission. Provide an admin option to view and manage submitted feedback. This improvement helps identify service issues, understand passenger needs, and improve the overall quality of the bus transportation system.