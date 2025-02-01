# Mini Project: Vue, Python, Django on Google Cloud Platform

This mini project integrates a Vue.js frontend with a Django backend, deployed on Google Cloud Platform using Terraform for infrastructure management. 

## Project Structure

```
mini-project
├── frontend
│   ├── src
│   │   ├── App.vue
│   │   ├── main.js
│   │   └── components
│   │       └── HelloWorld.vue
│   ├── public
│   │   └── index.html
│   ├── package.json
│   └── README.md
├── backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── backend
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── app
│       ├── __init__.py
│       ├── models.py
│       ├── views.py
│       └── urls.py
├── terraform
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── README.md
```

## Getting Started

### Prerequisites

- Node.js and npm installed for the frontend
- Python and pip installed for the backend
- Terraform installed for infrastructure management
- Google Cloud account with billing enabled

### Frontend Setup

1. Navigate to the `frontend` directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run serve
   ```

### Backend Setup

1. Navigate to the `backend` directory:
   ```
   cd backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run database migrations:
   ```
   python manage.py migrate
   ```

4. Start the Django development server:
   ```
   python manage.py runserver
   ```

### Terraform Setup

1. Navigate to the `terraform` directory:
   ```
   cd terraform
   ```

2. Initialize Terraform:
   ```
   terraform init
   ```

3. Plan the deployment:
   ```
   terraform plan
   ```

4. Apply the configuration:
   ```
   terraform apply
   ```

## Usage

- Access the Vue.js application at `http://localhost:8080`.
- Access the Django API at `http://localhost:8000`.

## License

This project is licensed under the MIT License.