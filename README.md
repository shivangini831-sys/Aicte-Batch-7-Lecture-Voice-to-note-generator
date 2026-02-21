Lecture Voice to Notes Generator
Project Description

The Lecture Voice to Notes Generator is an AI-based web application that converts lecture audio into structured text notes using speech recognition technology.

Many students face difficulty in writing notes while listening to lectures. This project provides a solution by automatically converting recorded lecture audio into readable text. The system is developed using Python and Streamlit and uses the Vosk Speech Recognition model for offline transcription.

Objectives

To develop a system that converts lecture voice into text

To simplify the note-taking process for students

To implement speech recognition in a real-world application

To build a simple and user-friendly web interface

Key Features

Upload lecture audio file

Convert speech to text

Generate readable text notes

Save output text files

Simple and interactive Streamlit interface

Works offline using Vosk model

Technologies Used

Programming Language: Python

Frontend Framework: Streamlit

Speech Recognition Model: Vosk

Libraries Used:

wave

json

subprocess

tempfile

Version Control: Git and GitHub

System Architecture

User uploads lecture audio file

Audio is converted into WAV format if required

Vosk model processes the audio

Speech is converted into text

Transcribed text is displayed and saved as notes

Project Structure
voice_lecture_to_notes/
│
├── main.py                  # Main Streamlit application
├── requirements.txt         # Required dependencies
├── vosk-model/              # Speech recognition model files
├── output/                  # Generated notes
└── README.md                # Project documentation
How to Run the Application

Run the following command:

streamlit run main.py

The application will open in your default web browser.

Output

The application displays the transcribed text on the screen

Generated notes are saved inside the output folder

Output format: .txt file

Results

The system successfully converts lecture audio into readable text with good accuracy. It reduces manual effort and saves time for students.

Future Enhancements

Add automatic summarization of notes

Improve punctuation and formatting

Support multiple languages

Export notes in PDF format

Add real-time microphone recording

Deploy application on cloud platform

Learning Outcomes

Implementation of speech recognition using Vosk

Development of web applications using Streamlit

Audio processing in Python

Virtual environment management

Git and GitHub version control

Deployment of AI-based applications
