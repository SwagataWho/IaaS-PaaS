import streamlit as st

# Page title
st.title("Basic Math Operations Calculator")

# Input fields for two numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Operation selection
operation = st.selectbox("Select the math operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2

    st.success(f"Result: {result}")
