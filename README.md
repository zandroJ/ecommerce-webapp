
# Bath Spa RAK - Final Year Project for Tomorrow's Web Module
Deployed website code is on an alt account here: https://github.com/gachaman32/ecommerce-web-app/tree/main (currently unavailable)

# 🛒 E-Commerce & Auction Web Application

A Django-based e-commerce platform featuring product listings, active auction bidding, watchlists, and categories. This repository is fully optimized to run entirely locally using an isolated Python environment and a local SQLite database setup.

## Local Quickstart Guide

Follow these steps to set up, configure, and launch this application on your local Linux machine.

### 1. Install System Prerequisites
Ensure your Linux Mint system has Python 3 and its virtual environment development tools installed:
```bash
sudo apt update
sudo apt install python3-venv python3-full -y
```

### 2. Clone and Navigate
Clone this repository to your desktop and move directly into the project directory:
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL_HERE>
cd ecommerce-webapp
```

### 3. Set Up the Virtual Environment
Create and activate an isolated virtual environment to manage dependencies securely without altering system packages:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
*(Your terminal prompt should now show `(.venv)` at the beginning, confirming activation).*

### 4. Install Dependencies
Install all the required Python libraries specified for the local application:
```bash
pip install -r requirements.txt
```

### 5. Configure Local Environment Variables
Create a file named `.env` in the root folder (`ecommerce-webapp/`) to house placeholder environment keys. This satisfies the local configuration parameters:
```text
SECRET_KEY=local_development_secret_key_string_12345
DEBUG=True
STRIPE_PUBLISHABLE_KEY=pk_test_mock
STRIPE_SECRET_KEY=sk_test_mock
```

### 6. Initialize Database and Run
Generate your local SQLite database architecture and launch the built-in development hosting server:
```bash
python manage.py migrate
python manage.py runserver
```

Open your web browser and navigate to **`http://127.0.0`** to view your live application!

## ⚠️ Stripe API & Payments Disclaimer
Because this repository is tailored strictly for standalone local execution, the live **Stripe API integration is unavailable**. 

To prevent transaction crashes caused by expired or missing production cloud API keys, all checkout routes (`/watchlist_checkout` and `/listed_detail_checkout`) are hardcoded to completely bypass external payment networks. Initiating a purchase automatically generates a mock transaction event and transitions the interface directly to the local success summary screens.



