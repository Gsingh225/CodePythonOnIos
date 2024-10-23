# CodePythonOnIos 🐍📱

> A free and easy solution for on-the-fly Python development on iOS devices using iSH Shell and a web-based code editor.

## 📝 Overview

iOS development can be restrictive when it comes to executing arbitrary code. This project provides a straightforward solution by combining iSH Shell (a Linux-like environment) with a web-based application, enabling Python development directly on your iOS device.

## 🚀 Installation Guide

### 1. Install iSH Shell
[![Download on the App Store](https://img.shields.io/badge/Download-App%20Store-blue.svg)](https://apps.apple.com/us/app/ish-shell/id1436902243)
- Search for "iSH Shell" on the App Store or use the link above
- Install the application (it's free!)

### 2. Set Up Python Environment
Launch iSH Shell and run the following commands:
```bash
# Install Python 3
apk add python3

# Install Git
apk add git
```

### 3. Project Setup
```bash
# Clone the repository
git clone https://github.com/Gsingh225/CodePythonOnIos

# Navigate to project directory
cd CodePythonOnIos

# Install required dependencies
pip install -r requirements.txt
```

### 4. Configure Shared Memory
```bash
# Create and mount shared memory
mkdir -p /dev/shm
mount -t tmpfs -o size=512M tmpfs /dev/shm
```

> ⚠️ **Important**: After configuring shared memory, restart iSH Shell:
> 1. Swipe up to view app dock
> 2. Close iSH Shell
> 3. Relaunch the application

## 🖥️ Running the Application

1. Navigate to the project directory:
```bash
cd CodePythonOnIos
```

2. Start the application:
```bash
python3 app.py
```

3. Open your preferred browser and visit `localhost` to access the web-based Python editor

## ⚠️ Known Issues

- The code editor is currently optimized for desktop view
- Mobile-responsive design update is in progress
- Please do not open issues related to mobile responsiveness at this time

## 📋 Requirements

- iOS device
- iSH Shell
- Internet connection (for initial setup)

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests for improvements.

## 📄 License

[Insert License Information Here]

---
Made with ❤️ for iOS Python developers
