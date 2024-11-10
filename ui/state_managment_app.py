import streamlit as st

st.title("Counter with Session State")

if "counter" not in st.session_state:
    st.session_state.counter = 0

increment_btn = st.button("Increment")

if increment_btn:
    st.session_state.counter = st.session_state.counter + 1
    st.write("Counter Incremented!")


reset_btn = st.button("Reset")

if reset_btn:
    st.session_state.counter = 0
    st.write("Counter reset")

example_button = st.button("Example")
if example_button:
    st.write("You pressed on example button")

st.write(f"Current counter value: {st.session_state.counter}")



























# st.title("Counter without session state")
#
# counter = 100
#
# increment_btn = st.button("Increment")
#
# if increment_btn:
#     counter = counter + 1
#     st.write("Counter Incremented!")
#
#
# reset_btn = st.button("Reset")
#
# if reset_btn:
#     counter = 0
#     st.write("Counter reset")
#
#
# example_button = st.button("Example")
#
# if example_button:
#     st.write("You pressed on example button")
#
# st.write(f"Current value of the counter is: {counter}")




