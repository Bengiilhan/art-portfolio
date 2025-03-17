Art Portfolio

A fully responsive portfolio website where artists can showcase their work, manage their gallery through an admin panel, and improve visibility with SEO-friendly features.

Experience the live version of this portfolio website: 
[seyhanilhan.com](https://seyhanilhan.com)

Features
- Artist biography and portfolio display
- Image gallery with Cloudinary storage
- Contact page with social media links
- Responsive design with Bootstrap 5
- Django admin panel for managing artworks
- SEO-friendly sitemap

Technologies Used
- Frontend: HTML, CSS, Bootstrap 5, JavaScript 
- Backend: Django 5.1.5, Python
- Database: PostgreSQL (on Render)
- Media Storage: Cloudinary
- Deployment: GitHub + Render

Installation & Setup
Clone the repository:
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/art-portfolio.git
cd art-portfolio
```

Create a virtual environment and install dependencies:
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Configure environment variables
Create a `.env` file in the project root and add:
```sh
SECRET_KEY=your_secret_key
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
DATABASE_URL=your_postgresql_database_url
# If running locally, use:
ALLOWED_HOSTS=127.0.0.1,localhost

# If deploying on a server, replace with your own domain:
ALLOWED_HOSTS=yourwebsite.com,www.yourwebsite.com
```

Apply database migrations:
```sh
python manage.py migrate
```

Run the development server
```sh
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

Adding New Artworks
1. Go to Django Admin Panel: `/admin/`
2. Log in with your admin credentials
3. Navigate to "Resim" (Artworks) and add new items
4. Upload images (stored via Cloudinary)

Models & Admin Panel
Models (`models.py`)
```python
from django.db import models
from cloudinary.models import CloudinaryField

class Resim(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image')

    def __str__(self):
        return self.title
```

Admin Panel (`admin.py`)
```python
from django.contrib import admin
from .models import Resim

class ResimAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')
    list_filter = ('title',)

admin.site.register(Resim, ResimAdmin)
```

License
This project is open-source and available under the MIT License.

