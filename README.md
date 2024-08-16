# DJANGO-TWEET-APPLICATION
Responsive Tweet Web Application built with Django, featuring user authentication and tweet management.

# Tweet Web Application 🐦

This is a web application developed using the Python Django framework that allows users to tweet, edit, and delete their own tweets. The application also handles user authentication and form handling securely, utilizing Django's features.

## 🔑 Key Features:

- **User Authentication:**
  - Secure user registration and login system using Django’s authentication framework.
  - Password hashing and protection against common vulnerabilities like CSRF and XSS.
  
- **Tweet Management:**
  - Users can create, edit, and delete their own tweets.
  - Tweets are dynamically updated in the interface using JavaScript.

- **Responsive Design:**
  - Built with HTML, CSS, and JavaScript to ensure a smooth user experience across all devices.
  - Mobile-first design approach with responsive layouts.

- **Form Handling:**
  - Forms are handled securely with Django’s built-in validation and protection mechanisms.

## 🛠️ Technologies Used:

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite 
- **Responsive Design:** CSS Flexbox, Media Queries

## 📂 Project Structure:

```
├── tweetapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started:

### 1. Clone the Repository:
```bash
git clone https://github.com/yourusername/DJANGO-TWEET-APPLICATION.git
cd DJANGO-TWEET-APPLICATION

```

### 2. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations:
```bash
python manage.py migrate
```

### 4. Run the Development Server:
```bash
python manage.py runserver
```

### 5. Access the Application:
Open your browser and navigate to `http://127.0.0.1:8000/`.


### 6. Screenshots

### 1. LoginPage
![LoginPage](https://github.com/user-attachments/assets/9323b5fc-26b3-4a6a-b1c2-95f6ba925713)

### 2. LoginForm
![LoginForm](https://github.com/user-attachments/assets/914272b0-b697-4b1b-b487-9cb33acf5edc)


### 3. RegistrationForm
![RegistrationForm](https://github.com/user-attachments/assets/ce60d224-7fc9-40d6-8c1f-3a852feab5e8)


### 4. HomePage
![HomePage](https://github.com/user-attachments/assets/6265f684-859c-487c-bb19-ad2e8bc98934)

### 5. CreateTweetForm
![CreateTweetForm](https://github.com/user-attachments/assets/72ea75d8-8f20-478b-a897-ff83622a433e)

### 6. EditTweetForm
![EditTweetForm](https://github.com/user-attachments/assets/c983568e-437b-4de4-ab35-cc60bf72e9b2)


