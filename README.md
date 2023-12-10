# SPA

This is a Single Page Application (SPA) built with Django, designed for handling comments. Users can leave comments with various features including file uploads, and the application provides a secure environment with protection against XSS attacks and SQL injections.

## Features

- **User Comments:** Users can leave comments with the following fields:
  - User Name (alphanumeric characters)
  - E-mail (email format)
  - CAPTCHA verification
  - Text (comment text with limited HTML tags)

- **Comment Hierarchy:** Supports cascading comments, allowing users to reply to existing comments.

- **Sorting and Pagination:** Comments are displayed in a table format with the ability to sort by User Name, E-mail, and the date of submission (ascending and descending order). Pagination is implemented with 25 comments per page.

- **File Uploads:** Users can attach images or text files to their comments. Image files are resized to 320x240 pixels if they exceed this size. Accepted formats include JPG, GIF, and PNG for images, and TXT for text files.

- **Rich Text Editor:** Provides a simple rich text editor for users, allowing them to format their comments using allowed HTML tags.

- **JavaScript and AJAX:** Implements client-side and server-side data validation. Enables a preview function for comments without reloading the page. Offers a toolbar with buttons for allowed HTML tags.

## Getting Started

Follow these steps to set up and run the project locally:

1. Clone the repository:

   git clone https://github.com/igorkulish09/SPA_Comments_App.git

2. Install dependencies:

   pip install -r requirements.txt

3. Run migrations:

   python manage.py makemigrations
   python manage.py migrate

4. Start the development server:

   python manage.py runserver
   Visit http://localhost:8000 in your web browser to access the application.

Technologies Used

    Django
    Django ORM
    JavaScript
    HTML/CSS
    Docker
    WebSocket (WS)

Security Considerations

The project is designed with security in mind to protect against XSS attacks and SQL injections. Make sure to follow best practices for web application security.
