
import streamlit as st
from datetime import date, time
from urllib.parse import quote
import re

# Your WhatsApp number with country code, without + or spaces
WHATSAPP_NUMBER = "919440882425"

st.set_page_config(
    page_title="Theja - Swetha Wedding Vehicle Arrangement",
    page_icon="💒",
    layout="centered"
)

st.write(
    "Welcome! Please provide your details below "
    "if you need transportation for the wedding."
)

st.divider()

with st.form("vehicle_request_form"):
    st.subheader("Guest Details")

    name = st.text_input(
        "Guest Name *",
        placeholder="Enter your full name",
    )

    contact = st.text_input(
        "Contact Number *",
        placeholder="Enter your mobile number",
    )

    st.subheader("Travel Details")

    booking_date = st.date_input(
        "Travel Date *",
        value=date.today(),
        min_value=date.today(),
    )

    booking_time = st.time_input(
        "Pickup Time *",
        value=time(9, 0),
    )

    passengers = st.number_input(
        "Number of Passengers",
        min_value=1,
        max_value=100,
        value=2,
        step=1,
    )

    additional_info = st.text_area(
        "Additional Requirements (Optional)",
        placeholder="Enter any additional requirements...",
    )

    submitted = st.form_submit_button(
        "Submit Vehicle Requirement",
        use_container_width=True,
    )

if submitted:
    name = name.strip()
    contact = contact.strip()

    if not name:
        st.error("Please enter the guest name.")

    elif not re.fullmatch(r"\+?[\d\s()-]{10,20}", contact):
        st.error("Please enter a valid contact number.")

    elif not WHATSAPP_NUMBER.isdigit() or "X" in WHATSAPP_NUMBER:
        st.error("Please configure WHATSAPP_NUMBER in app.py.")

    else:
        message = (
            "💒 WEDDING VEHICLE REQUIREMENT\n\n"
            f"Guest Name: {name}\n"
            f"Contact Number: {contact}\n"
            f"Travel Date: {booking_date.strftime('%d-%m-%Y')}\n"
            f"Pickup Time: {booking_time.strftime('%I:%M %p')}\n"
            f"Number of Passengers: {passengers}\n"
            f"Additional Requirements: "
            f"{additional_info.strip() or 'None'}"
        )

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}"
            f"?text={quote(message)}"
        )

        st.success("Your vehicle requirement is ready.")

        st.link_button(
            "Continue to WhatsApp",
            whatsapp_url,
            use_container_width=True,
        )

        st.caption(
            "WhatsApp will open with your details filled in. "
            "Please press Send in WhatsApp to submit your request."
        )

st.divider()

st.caption(
    "Please submit your transportation requirements in advance. "
    "Vehicle availability will be confirmed separately."
)
