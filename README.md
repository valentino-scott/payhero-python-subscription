# 🚀 PayHero Python Subscription Boilerplate

A production-ready Flask SaaS starter kit for integrating **M-Pesa payments via the PayHero API**.

Build subscription platforms, membership sites, digital product stores, and SaaS applications with a complete payment workflow already implemented.

This open-source project includes:

* Instant M-Pesa STK Push payments
* Real-time transaction status updates
* Secure webhook callback handling
* Responsive subscription pricing interface
* Environment-based configuration
* Production-ready Flask architecture

Perfect for developers and startups looking to launch M-Pesa-powered products quickly without spending days implementing payment infrastructure.

---

## ✨ Features

### 💳 M-Pesa STK Push Integration

Trigger payment requests directly to customer phones using the PayHero API and Safaricom M-Pesa.

### 📡 Webhook Callback Processing

Receive and process payment confirmations asynchronously with secure Flask webhook endpoints.

### 🔄 Real-Time Payment Status Tracking

Automatic frontend polling keeps users informed of payment progress without refreshing the page.

### 🎨 Modern Subscription UI

Responsive pricing cards with support for multiple plans, plan selection, and mobile-friendly layouts.

### 🔒 Secure Configuration

Sensitive credentials are managed through environment variables using `python-dotenv`.

### 📱 Mobile-First Experience

Optimized for smartphones, tablets, and desktop devices.

### ⚡ Production-Ready Foundation

Well-structured Flask project suitable for SaaS products, subscription services, digital marketplaces, and membership platforms.

---

## 🛠 Technology Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python 3.8+       | Backend Development       |
| Flask             | Web Framework             |
| PayHero API       | M-Pesa Payment Processing |
| JavaScript (ES6+) | Frontend Interactions     |
| HTML/CSS          | User Interface            |
| Ngrok             | Local Webhook Testing     |

---

## 🎯 Use Cases

This boilerplate can be adapted for:

* SaaS subscriptions
* Membership platforms
* Online courses
* Digital downloads
* Premium content websites
* E-commerce stores
* Event ticketing systems
* Donation platforms

---

## 🚀 Quick Start

### Clone the Repository

```bash
git clone https://github.com/valentino-scott/payhero-python-subscription.git
cd payhero-python-subscription
```

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
API_USERNAME=your_payhero_username
API_PASSWORD=your_payhero_password
ACCOUNT_ID=your_account_id
CHANNEL_ID=your_channel_id
PUBLIC_URL=https://your-ngrok-url.ngrok-free.app
```

### Start the Application

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

---

## 🧪 Testing M-Pesa Callbacks

Because M-Pesa confirmations are asynchronous, PayHero requires a publicly accessible callback URL.

Start Ngrok:

```bash
ngrok http 5000
```

Copy the generated HTTPS URL and update:

```env
PUBLIC_URL=https://your-ngrok-url.ngrok-free.app
```

Restart the Flask server and initiate a test payment.

---

## 📂 Project Structure

```text
payhero-python-subscription/
│
├── app.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
│
└── templates/
    ├── index.html
    └── success.html
```

---

## 🤝 Contributing

Contributions are welcome.

If you would like to improve the project:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes

```bash
git commit -m "Add amazing feature"
```

4. Push to GitHub

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

Please open an issue first for major changes so the proposal can be discussed.

---

## 📄 License

Distributed under the MIT License.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Valentino Scott**

GitHub: https://github.com/valentino-scott

Repository:
https://github.com/valentino-scott/payhero-python-subscription

If this project helps you, consider giving it a ⭐ on GitHub.
