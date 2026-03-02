import os
from google import genai
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from dotenv import load_dotenv

load_dotenv()

# ==============================
# Loading API Key
# ==============================

api_key = os.getenv('GEMINI_API_KEY')

if not api_key:
    st.error("API Key not found. Please check your .env file.")
    st.stop()

# ================================================
# Initialize client once in session_state
# ================================================

if "client" not in st.session_state:
    st.session_state.client = genai.Client()

client  = st.session_state.client


syst_prompt = """
You are an experienced investment advisor in India.

Speak clearly and naturally.
Do not repeat your role.
Do not promise guaranteed returns.
Give practical beginner-friendly advice.
Suggest fund categories (not specific stock tips).
Suggest few top funds and Etfs as per the requirement and also provide past -
1year, 3years, 5years and inception data.

"""
# ========================================================
# Create chat session with memory only once
# ========================================================

if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash",
        config = genai.types.GenerateContentConfig(
            system_instruction=syst_prompt,
        )
    )

chat_session = st.session_state.chat_session

# ==============================
# Page setup
# ==============================

import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="AI Investment Assistant", layout="wide")

st.title("AI Investment Portfolio Assistant")

# ==============================
# Sidebar - Investment Controls
# ==============================

st.sidebar.header("Investment Assumptions")

# ==============================
# Investment Type Toggle
# ==============================

investment_type = st.sidebar.radio(
    "Select Investment Type",
    ["SIP", "Lumpsum"]
)

# ==============================
# Expected Return
# ==============================

expected_return_percent = st.sidebar.slider(
    "Expected Annual Return (%)", 3, 30, 12
)

expected_return = expected_return_percent / 100

# ==============================
# Risk Classification
# ==============================

if expected_return_percent <= 7:
    risk_label = "Conservative (FD-like stability)"
elif expected_return_percent <= 15:
    risk_label = "Moderate (Balanced growth)"
else:
    risk_label = "Aggressive (High growth, high volatility)"

st.sidebar.markdown(f"## Risk Category: **{risk_label}**")

# ==============================
# Investment Duration (Common)
# ==============================

years = st.sidebar.slider(
    "Investment Duration (Years)",
    1,
    40,
    value = 5
)

# ==============================
# Input Based on Investment Type
# ==============================

if investment_type == "SIP":
    amount = st.sidebar.number_input(
        "Monthly Investment Amount",
        min_value=0,
        max_value=100_000,
        value=500
    )
else:
    amount = st.sidebar.number_input(
        "Lumpsum Investment Amount",
        min_value=1_000,
        max_value=10_000_000,
        value=10000
    )

# ==============================
# Calculation Logic
# ==============================

if investment_type == "SIP":
    months = years * 12
    monthly_rate = expected_return / 12

    if monthly_rate > 0:
        total_value = amount * (
            ((1 + monthly_rate) ** months - 1) / monthly_rate
        ) * (1 + monthly_rate)
    else:
        total_value = amount * months

    invested_amount = amount * months

else:
    total_value = amount * (1 + expected_return) ** years
    invested_amount = amount

returns = total_value - invested_amount

# ==============================
# Sidebar Returns Display
# ==============================

st.sidebar.markdown("### Returns")
st.sidebar.write(f"Invested: ₹{int(invested_amount):,}")
st.sidebar.write(f"Returns: ₹{int(returns):,}")
st.sidebar.write(f"Total: ₹{int(total_value):,}")

# ==============================
# Main Panel - Pie Chart
# ==============================

labels = ["Invested Amount", "Returns"]
values = [invested_amount, returns]
colors = ['#4CAF50', '#FFC107']

fig, ax = plt.subplots()
ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

st.sidebar.pyplot(fig)

# ==============================
# CHAT HISTORY
# ==============================

st.subheader("Ask the AI Investment Advisor")

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==============================
# Display past messages
# ==============================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# CHAT INPUT
# ==========================================

user_input = st.chat_input("Ask about portfolio strategy, risk, SIP planning...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    response = chat_session.send_message(user_input)
    bot_reply = response.text

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.markdown(bot_reply)


# ==========================================
# RESET BUTTON
# ==========================================

if st.button("Reset Conversation"):
    st.session_state.messages = []
    st.session_state.chat_session = client.chats.create(
        model="gemini-2.5-flash",
        config=genai.types.GenerateContentConfig(
            system_instruction="You are an experienced investment advisor."
        )
    )
    st.rerun()