# PayHero Python Subscription: Full-Stack M-Pesa SaaS Boilerplate 🚀

**A production-ready, open-source Python Flask application for integrating M-Pesa mobile payments using the PayHero API.**
This project provides a complete SaaS subscription boilerplate featuring a beautiful responsive 3-tier pricing UI, real-time payment status polling, and asynchronous webhook callback handling.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![PayHero](https://img.shields.io/badge/PayHero-M--Pesa-green?style=for-the-badge&logo=mpesa)](https://payhero.co.ke/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📖 Table of Contents
- [About The Project](#-about-the-project)
- [Key Features](#-key-features)
- [Built With](#-built-with)
- [Live Demo](#-live-demo)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#-usage)
  - [Environment Variables](#environment-variables)
  - [Running the Application](#running-the-application)
  - [Testing with Ngrok](#testing-with-ngrok)
- [Project Structure](#-project-structure)
- [SEO & Analytics](#-seo--analytics)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📌 About The Project

This repository serves as a **complete boilerplate for any Kenyan developer or business** looking to accept M-Pesa payments instantly. 

Most developers struggle with PayHero's authentication or handling asynchronous M-Pesa callbacks. This project solves that by providing a **zero-configuration starting point** that handles everything from the secure `.env` setup to real-time frontend updates when a user enters their PIN.

Whether you are selling digital products, subscriptions, or physical goods, this application can be deployed to production in under 10 minutes.

---

## ✨ Key Features

- 💳 **Instant M-Pesa STK Push**: Utilizes PayHero's API to send payment prompts directly to mobile phones.
- 🎨 **Modern 3-Tier Pricing UI**: Beautiful, responsive cards (Basic, Premium, Premium+) with interactive hover effects and selection logic.
- 🔄 **Live Transaction Polling**: The frontend automatically checks the backend every 2 seconds. No page refresh required.
- 📡 **Asynchronous Webhooks**: Fully configured Flask routes to handle real-time callbacks from PayHero (Success, Failure, Cancelled).
- 📱 **Mobile-First Design**: Built with `Inter` fonts and Flexbox/Grid to look stunning on mobile devices and desktops.
- 🔒 **Enterprise-Grade Security**: API keys are loaded using `python-dotenv`. The `.env` file is explicitly ignored by `.gitignore`.

---

## 🛠️ Built With

*   **[Python 3.8+](https://www.python.org/)** - The core backend programming language.
*   **[Flask](https://flask.palletsprojects.com/)** - A lightweight WSGI web application framework.
*   **[PayHero API](https://payhero.co.ke/)** - The gateway used to bridge Python with Safaricom M-Pesa.
*   **[Ngrok](https://ngrok.com/)** - Used for tunneling localhost to the public internet for webhook testing.
*   **[JavaScript (ES6+)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)** - Handles the DOM manipulation and live polling logic.

---

## 🖥️ Live Demo

*(Insert a GIF screen recording here showing the 3 cards, selecting a plan, the payment popup on mobile, and the status box turning green).*

**Live URL:** *Pending deployment (See deployment guide below)*

---

## 🚀 Getting Started

Follow these steps to get a local copy up and running on your machine.

### Prerequisites

*   Python 3.8 or higher installed on your machine.
*   An active **PayHero** merchant account (with API Username, Password, Account ID, and Channel ID).
*   A **Ngrok** account (Free tier is sufficient for testing).

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/valentino-scott/payhero-python-subscription.git
    cd payhero-python-subscription
    ```
2. **Create and activate a Python virtual environment**

``` bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. **Install dependencies**

```bash
pip install -r requirements.txt