# Contact manager

## Setting Up the Environment

1. **Clone the Repository**

   Copy the repository to your computer:
   ```bash
   git clone https://github.com/glodanm/contact-manager-api.git
   cd contact-manager-api
   ```

2. **Create a Virtual Environment**

   Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # For Windows
   venv\Scripts\activate
   # For macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. **Migrations**

   Run migrations to create the tables in the database:
   ```bash
   python manage.py migrate
   ```

## Google OAuth2 Setup

1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Obtain OAuth 2.0 credentials (Client ID and Client secret) for your project.
3. Add the redirect URI in the OAuth settings: `http://localhost:8000/accounts/google/login/callback/`.
4. Make sure to enable the Google+ API for your project.

## Environment Variables Configuration

This project uses a `.env` file to manage sensitive configuration settings such as the secret key, debug mode, and OAuth credentials. The `.env` file is not included in version control (for security reasons), so you will need to create it manually in the root directory of the project.

### Sample `.env` File

Below is an example of the `.env.sample` file that you can use as a template. Copy its contents and create a `.env` file in your project directory.

```bash
# .env.sample

SECRET_KEY=your_django_secret_key_here
DEBUG=True  # Set to False in production
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_oauth2_client_id
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_oauth2_client_secret


## Running the Project

Start the development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access your project.

## Admin Panel Setup for Social Authentication
1. **Create super user** 
```bash
python createsuperuser
```
2. **Log in to the Django admin panel** by navigating to `http://127.0.0.1:8000/admin/`.
3. **Create a new Social Application**:
   - Go to the **Social Applications** section.
   - Click **Add Social Application**.
   - Select **Google** as the provider.
   - Enter the **Client ID** and **Client Secret** obtained from the Google Cloud Console.
   - Set the correct **Sites** to include your domain (`localhost:8000` for local development).
   - Save the social application.

## Using the API

### Endpoints

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/contacts` | GET | READ | Get all contacts
`api/contacts/<int:pk>` | GET | READ | Get a single contact
`api/contacts`| POST | CREATE | Create a new contact
`api/contacts/<int:pk>` | PUT | UPDATE | Update a contact
`api/contacts/<int:pk>` | DELETE | DELETE | Delete a contact
`accounts/login`| POST | LOGIN | Login via google account
`accounts/logout`| POST | LOGOUT | Logout from account


## IP Address Handling in Development

When the application runs on a local server (localhost), all requests come from the IP address `127.0.0.1`. 
This can cause issues when trying to retrieve the real IP address of the user.

To properly obtain the user's IP address, we need to configure a **proxy**. When the request goes through a proxy 
(such as in production with Nginx or another load balancer), the real IP address can be found in the `HTTP_X_FORWARDED_FOR` header. 
However, on a local server, you will always receive `127.0.0.1` as the IP, since you're working on localhost.

