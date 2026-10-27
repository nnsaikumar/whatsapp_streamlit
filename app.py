
import streamlit as st
from datetime import date, time
from urllib.parse import quote
import re

# Configure your WhatsApp number with country code.
# Example: 919876543210 (no + or spaces)
WHATSAPP_NUMBER = "91XXXXXXXXXX"

st.set_page_config(
    page_title="Booking Form",
    page_icon="📅",
    layout="centered"
)

st.title("Booking Form")

with st.form("booking_form"):
    name = st.text_input("Name")

    booking_date = st.date_input(
        "Date",
        value=date.today()
    )

    booking_time = st.time_input(
        "Time",
        value=time(10, 0)
    )

    contact = st.text_input(
        "Contact Number",
        placeholder="Enter your phone number"
    )

    submitted = st.form_submit_button(
        "Submit",
        use_container_width=True
    )

if submitted:
    name = name.strip()
    contact = contact.strip()

    if not name:
        st.error("Please enter your name.")

    elif not re.fullmatch(r"\+?[\d\s()-]{10,20}", contact):
        st.error("Please enter a valid contact number.")

    elif "X" in WHATSAPP_NUMBER or not WHATSAPP_NUMBER.isdigit():
        st.error(
            "Please configure WHATSAPP_NUMBER in app.py."
        )

    else:
        message = (
            "New Booking Details\n\n"
            f"Name: {name}\n"
            f"Date: {booking_date.strftime('%d-%m-%Y')}\n"
            f"Time: {booking_time.strftime('%I:%M %p')}\n"
            f"Contact Number: {contact}"
        )

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}"
            f"?text={quote(message)}"
        )

        st.success("Your booking details are ready!")

        st.link_button(
            "Open WhatsApp and Send",
            whatsapp_url,
            use_container_width=True
        )
