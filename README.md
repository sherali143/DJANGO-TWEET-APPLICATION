# DJANGO-TWEET-APPLICATION
Responsive Tweet Web Application built with Django, featuring user authentication and tweet management.

# Tweet Web Application 🐦

This is a responsive web application developed using the Python Django framework that allows users to tweet, edit, and delete their own tweets. The application also handles user authentication and form handling securely, utilizing Django's built-in features.

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
![LoginForm](https://github.com/user-attachments/assets/f41fd1a7-add2-4278-9d14-0e41bbd5bd7e)

### 3. RegistrationForm
![RegistrationForm](https://github.com/user-attachments/assets/63fb43e7-8eca-42a2-bca6-d4604c907d5b)

### 4. HomePage
![HomePage](https://github.com/user-attachments/assets/6265f684-859c-487c-bb19-ad2e8bc98934)

### 5. CreateTweetForm
![CreateTweetForm](https://github.com/user-attachments/assets/20f65571-c14b-4360-863a-ae59df3252d7)


### 6. EditTweetForm
![EditTweetForm](https://github.com/user-attachments/assets/048c503d-5075-42b4-a5e3-5d1fbf3cf968)

