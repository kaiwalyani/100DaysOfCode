# Pomodoro Timer

## Description
The Pomodoro Timer is a time management tool based on the Pomodoro Technique. It alternates between periods of focused work and short breaks to boost productivity. The application is built using Python's Tkinter library for the graphical user interface (GUI).

## Features
- Work Sessions: 25-minute work sessions.
- Breaks: 5-minute short breaks and a 20-minute long break after every 4 work sessions.
- Visual Countdown: A visual countdown timer.
- Checkmarks: Track completed work sessions with checkmarks.
- Reset Functionality: Reset the timer at any time.

## Requirements
- Python 3.x
- Tkinter (built-in with Python installations)

## Files
1. main.py: The main script containing the Pomodoro timer logic and UI.
2. tomato.png: Image file used in the timer UI.

## Setup
- Ensure Python 3.x is installed on your system.
- Install any missing dependencies (Tkinter should come pre-installed with Python).
- Place the tomato.png file in the same directory as main.py.

## How it Works
1. The Pomodoro timer starts with a 25-minute work session.
2. After each work session, a 5-minute break follows.
3. After 4 work sessions, a longer 20-minute break is triggered.
4. Every work session adds a checkmark ✔ to track progress.
5. The timer can be reset at any time using the Reset button.

## Notes
You can customize the durations of the work sessions, short breaks, and long breaks by changing the constants:
```
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

Stay productive with the Pomodoro Timer!
