# Midnight Times

## Overview
Midnight Times is a web-based application that allows users to search for news articles from around the world using the News API. Users can view their previous searches and the results. Additional functionalities include user authentication, an admin panel, and automatic background updates.

## Features
- Search for news articles by keyword.
- View results of previous searches.
- Refresh search results.
- Sort search results by date published.
- Admin functionalities to manage users and view trending keywords.
- User-specific search history and results.

## Setup Instructions
1. Clone the repository:
    git clone https://github.com/your-repo/midnight-times.git
    cd midnight-times

2. Install the required libraries:
    pip install -r requirements.txt
4. Configure environment variables:
    - Create a `.env` file in the project root and add your News API key:
        NEWS_API_KEY=your_news_api_key
5. Run database migrations:
    python3 manage.py makemigrations
    python3 manage.py migrate

6. Create a superuser for accessing the admin panel:
    python manage.py createsuperuser

7. Start the development server:
    python3 manage.py runserver

## Development Time and Experience
- Total time taken: 48 hours
- Experience:
    a). The first problem was doing Authentication and autherisation of the users with built in feature in django.
    so to solve this I went through lectures and blogs to know how to implement these functionalities in django.
    b). Implementing celery and redis was toughest because i have never worked on anything like this 
    and did not knew about the background job which works allong side with application without disrupting it.
    so to overcame this i had to search a lot that what can be used and how it can be used.
    c) Generally i used to create every functinality in one app only but i have always thought of creating new app 
    for different functionalities so i had to learn about modularisation of the application.    

