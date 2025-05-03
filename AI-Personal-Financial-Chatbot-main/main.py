import streamlit as st
from groq import Groq  # ✅ correct import

# Initialize Groq Client
API_KEY = "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"
groq_client = Groq(api_key=API_KEY)


# Sidebar for user input
st.sidebar.header("📌 Provide Your Financial Information")

income = st.sidebar.number_input("💰 Monthly Income (₹):", min_value=0.0, format="%.2f")
expenses = st.sidebar.number_input("📉 Monthly Expenses (₹):", min_value=0.0, format="%.2f")
savings = st.sidebar.number_input("🏦 Current Savings (₹):", min_value=0.0, format="%.2f")
goal = st.sidebar.text_input("🎯 Your Financial Goal:")

# Custom CSS to apply background and styling
st.markdown(
    """
    <style>
        .stApp {
            background: url("https://images.unsplash.com/photo-1579621970588-a35d0e7ab9b6?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDZ8fGZpbmFuY2V8ZW58MHx8MHx8fDA%3D") no-repeat center center fixed;
            background-size: cover;
        }
        .stTextInput, .stNumberInput, .stButton {
            border-radius: 10px;
            padding: 8px;
        }
        .stHeader, .stSubheader {
            font-weight: bold;
        }
        .title-text {
            font-size: 28px;
            font-weight: bold;
            color: black;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Main title
st.markdown('<h1 class="title-text">AI-Based Personal Finance Advisor</h1>', unsafe_allow_html=True)
st.markdown("###  Your Personalized Financial Plan")

# Function to get AI advice
def get_llm_advice(income, expenses, savings, goal):
    prompt = f"""
    You are a financial advisor helping users optimize their spending and saving strategies. 
    The user has the following financial details:
    
    - *Income:* ₹{income}
    - *Expenses:* ₹{expenses}
    - *Current Savings:* ₹{savings}
    - *Financial Goal:* {goal}
    
    Provide step-by-step budgeting advice with a structured breakdown of expenses, savings, and investment tips.
    """
    
    response = groq_client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",  # Fixed model name
        messages=[{"role": "system", "content": "Provide structured financial guidance."},
                  {"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content

# Button to get AI advice
ai_advice = ""  # Default empty text
if st.sidebar.button("🚀 Generate Financial Advice"):
    ai_advice = get_llm_advice(income, expenses, savings, goal)

# Display AI-generated advice inside a text area with increased height
st.markdown("###  Financial Insights & Recommendations")
st.text_area("📌 Your AI-Generated Financial Plan:", ai_advice, height=300)  # Increased height