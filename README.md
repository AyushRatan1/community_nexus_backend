# Com_nex: Community Connection App

## Overview
Com_nex is a modern Android application built with Jetpack Compose that aims to empower communities through technology. The app provides a seamless interface for accessing government schemes, connecting with neighbors, and getting assistance in local languages.

## Features

### Home Screen
- **Welcome Header**: Animated gradient welcome banner with localized greeting (नमस्ते! Welcome)
- **Search Functionality**: Modern search bar with shadow effects for finding services
- **Quick Actions**: Beautiful cards for quick access to essential services:
  - Government Schemes
  - Voice Assistant
  - Community Forum
  - Emergency Services
- **Bottom Navigation**: Easy navigation between main app sections

### Chat Interface
- **AI Assistant**: Modern chat interface with an AI assistant
- **Real-time Messaging**: Interactive message bubbles with timestamps
- **Voice Input**: Voice input capability for hands-free interaction
- **Read Receipts**: Visual indicators showing message read status
- **Multi-Language Support**: Design prepared for supporting multiple languages

## Technical Implementation

### UI Components
- **Modern UI**: Implemented using Jetpack Compose
- **Material Design**: Following Material Design 3 principles with custom theming
- **Animations**: Smooth animations for better user experience
- **Responsive Layout**: Adapts to different screen sizes
- **Accessibility**: High contrast colors and proper sizing

### Design Principles
- **Color Scheme**:
  - Primary: #6200EE (Purple)
  - Primary Dark: #3700B3 (Dark Purple)
  - Secondary: #03DAC6 (Teal)
  - Background: #F5F5F5 (Light Grey)
  - Text Primary: #212121 (Near Black)
  - Text Secondary: #757575 (Dark Grey)

- **Visual Hierarchy**:
  - Important actions highlighted with primary colors
  - Secondary information with reduced visual weight
  - Consistent padding and spacing

## Screens

### HomeScreen.kt
The main landing page of the application featuring:
- Gradient background
- Welcome header with animation
- Search functionality
- Quick action cards for key features
- Bottom navigation bar

### ChatScreen.kt
A modern messaging interface featuring:
- Sleek header with contact information
- Message bubbles with different styles for user and assistant
- Timestamp display for each message
- Read status indicators
- Voice input option
- Modern text input field with rounded corners

### ExploreScreen.kt
Discover community resources and government schemes.

### CommunityScreen.kt
Connect with neighbors and local community groups.

### HelpScreen.kt
Get assistance and support in multiple languages.

## Installation & Setup
1. Clone the repository
2. Open the project in Android Studio
3. Sync Gradle files
4. Run the application on an emulator or physical device

## Future Enhancements
- Offline support
- Push notifications
- Location-based services
- Enhanced language support
- Dark mode theme

## Technologies Used
- Kotlin
- Jetpack Compose
- Material Design 3
- Gradle
- Firebase (backend services) 
