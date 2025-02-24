
# Stock Market Dashboard

## Description
The Stock Market Dashboard is an interactive web application that allows users to monitor stock market trends, manage their portfolios, and analyze trading performance. The application provides a user-friendly interface for tracking stock prices and executing trades.

## Technologies Used
- Django (Backend)
- Tailwind CSS (Styling)
- HTML, CSS, JavaScript (Frontend)
- Chart.js (Data Visualization)
- SQLite (Database)

## Features
- User registration and authentication
- Stock monitoring with real-time data
- Portfolio management
- Buying and selling stocks
- User profile management

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd stock_market_dashboard
   ```
3. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
6. Run migrations:
   ```bash
   python manage.py migrate
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Register a new account or log in to an existing account.
- Use the dashboard to monitor stocks and manage your portfolio.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
