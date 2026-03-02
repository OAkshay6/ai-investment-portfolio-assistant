# AI Investment Portfolio Assistant

An AI-powered investment planning application built using **Streamlit** and **Google Gemini API**.

This application allows users to simulate SIP and Lumpsum investments, visualize projected returns, and receive AI-generated portfolio guidance based on risk level and investment duration.

---

## Overview

The application combines financial modeling, data visualization, and generative AI to create an interactive investment assistant suitable for beginner and intermediate investors.

It supports dynamic return projections, risk categorization, and AI-driven portfolio suggestions.

---

## Features

### Investment Simulation

- Supports SIP (Systematic Investment Plan)
- Supports Lumpsum Investment
- Adjustable investment duration (1–40 years)
- Adjustable expected annual return (3%–30%)
- Automatic risk classification:
  - Conservative
  - Moderate
  - Aggressive

---

### Financial Calculations

#### SIP Future Value Formula

\[
FV = P \times \frac{(1+r)^n - 1}{r} \times (1+r)
\]

Where:

- **P** = Monthly investment  
- **r** = Monthly interest rate  
- **n** = Total number of months  

#### Lumpsum Formula

\[
FV = P \times (1+r)^t
\]

Where:

- **P** = Initial investment  
- **r** = Annual return  
- **t** = Investment duration in years  

---

### Visual Analytics

- Pie chart breakdown of:
  - Invested amount
  - Returns generated
- Real-time updates based on user inputs

---

### AI Investment Advisor

Powered by the `gemini-2.5-flash` model.

Provides:

- Beginner-friendly portfolio strategy guidance
- Risk-based asset allocation suggestions
- Fund category recommendations
- ETF suggestions
- Historical performance references (1 year, 3 years, 5 years, since inception)

Chat history is maintained using Streamlit session state.

---

## Tech Stack

- Python
- Streamlit
- Matplotlib
- Plotly
- Google Gemini API
- python-dotenv

---

## Project Structure

ai-investment-portfolio-assistant/
│
├── ai_investment_portfolio_assistant.py
├── README.md
├── .gitignore
├── .env (not pushed to GitHub)
└── requirements.txt

---

## Installation and Setup

### 1. Clone the Repository
git clone https://github.com/OAkshay6/ai-investment-portfolio-assistant.git

cd ai-investment-portfolio-assistant

### 2. Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

If requirements file is not available:

pip install streamlit matplotlib plotly python-dotenv google-generativeai

### 4. Add Gemini API Key

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

### 5. Run the Application

streamlit run ai_investment_portfolio_assistant.py


---

## Learning Outcomes

This project demonstrates:

- Financial modeling using Python
- Risk classification logic
- Interactive UI development with Streamlit
- Generative AI integration in real-world applications
- Stateful conversation handling
- Secure environment variable management

---

### Author

Built as a practical AI + Finance application to demonstrate end-to-end development skills combining:

- Financial logic
- Data visualization
- LLM integration
- Interactive UI design
