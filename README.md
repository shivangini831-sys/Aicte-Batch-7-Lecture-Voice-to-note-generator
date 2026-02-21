Lecture Voice to Notes Generator
Abstract

The Lecture Voice to Notes Generator is an AI-based web application developed to convert recorded lecture audio into structured text notes. The system utilizes speech recognition technology to transcribe spoken content into readable text, reducing the manual effort required for note-taking. The application is built using Python and Streamlit and integrates the Vosk speech recognition model for offline processing.

Introduction

In academic environments, students often find it difficult to take notes while simultaneously understanding lecture content. This project addresses that problem by automatically converting lecture audio into text. The system processes audio input and generates structured notes that can be saved for future reference.

The application is designed to be simple, efficient, and user-friendly, making it accessible to students with minimal technical knowledge.

Problem Statement

Students face challenges in writing notes during live or recorded lectures. Manual note-taking can lead to incomplete or inaccurate documentation of important concepts. There is a need for an automated system that converts lecture speech into written text efficiently and accurately.

Proposed Solution

The proposed system accepts a lecture audio file as input and processes it using a speech recognition model. The application converts the audio into text format and displays the transcribed content on the interface. The generated notes are also saved in a text file for future use.

Key Features

Upload lecture audio files

Convert speech to text automatically

Generate readable and structured notes

Save transcribed text in output files

Simple and interactive user interface

Offline speech recognition support

Technologies Used

Programming Language: Python

Framework: Streamlit

Speech Recognition Model: Vosk

Supporting Libraries:

wave

json

subprocess

tempfile

Version Control: Git and GitHub

System Workflow

User uploads a lecture audio file.

The system converts the audio into WAV format if required.

The Vosk model processes the audio data.

Speech is recognized and converted into text.

The transcribed text is displayed on the screen.

The output is saved as a text file in the output directory.

Results

The system successfully converts lecture audio into readable text with satisfactory accuracy. It significantly reduces the time and effort required for manual note-taking.

Future Scope

Integration of automatic text summarization

Support for multiple languages

Improved punctuation and formatting

Export notes in PDF format

Real-time microphone recording support

Cloud-based deployment

Learning Outcomes

Implementation of speech recognition using Vosk

Development of interactive web applications using Streamlit

Audio processing and file handling in Python

Version control using Git and GitHub

Practical experience in AI-based application development
