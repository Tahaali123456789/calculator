import streamlit as st

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."

# Streamlit app
st.title("Simple Calculator")

# User input
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")
operation = st.selectbox("Select operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result of {operation.lower()} is: {result}")
