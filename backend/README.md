Kenza’s Entrepreneurial Journey & Personal Portfolio - Backend API
Overview
This backend API serves as the data source for Kenza’s Portfolio & Entrepreneurial Journey. It handles all dynamic content such as personal experiences, projects, and products from the Loubana skincare brand. The API is built using Flask and provides the necessary endpoints to feed data to the frontend.

Technologies Used:

Python
Flask
PostgreSQL
REST API
Installation Instructions:

Clone the repository.
Set up a virtual environment.
Install dependencies: pip install -r requirements.txt.
Set environment variables for database and API keys.
Initialize the database: python manage.py db init.
Run the development server: flask run.
API Endpoints:

API Endpoints
Experiences and Projects
GET /api/experience
Retrieves a list of my professional experiences.
GET /api/projects
Returns a list of my development projects.
Loubana Skincare Brand
GET /api/loubana

Retrieves all Loubana products.
GET /api/loubana/creme

Retrieves data about Crème Oliban.
GET /api/loubana/masque

Retrieves data about Masque Oliban Miel.
GET /api/loubana/tabrima

Retrieves data about Tabrima.
Contact Form (optional future feature)
POST /api/contact
This endpoint can handle contact form submissions 
Usage:

This API is consumed by the Vue.js frontend to fetch product data and process form submissions.
