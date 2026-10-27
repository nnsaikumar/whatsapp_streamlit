
import streamlit as st
from datetime import date, time
from urllib.parse import quote
import re

# Replace with your WhatsApp number (country code included)
# Example: 919876543210
WHATSAPP_NUMBER = "919440882425"

st.set_page_config(
    page_title="Theja -Swetha Wedding Vehicle Arrangement",
    page_icon="💒",
    layout="centered"
)

st.title("💒 Wedding Vehicle Arrangement")
st.write(
    "Welcome! If you need transportation for the wedding, "
    "please submit your requirements below."
)

st.divider()

with st.form("vehicle_request_form"):

    st.subheader("Guest Details")

    name = st.text_input(
        "Guest Name *",
        placeholder="Enter your full name"
    )

    contact = st.text_input(
        "Contact Number *",
        placeholder="Enter mobile number"
    )

    st.subheader("Travel Details")

    booking_date = st.date_input(
        "Travel Date *",
        value=date.today()
    )

    booking_time = st.time_input(
        "Pickup Time *",
        value=time(9, 0)
    )

    pickup = st.text_input(
        "Pickup Location *",
        placeholder="Where should we pick you up?"
    )

    destination = st.text_input(
        "Destination *",
        placeholder="Wedding venue or drop location"
    )

    guests = st.number_input(
        "Number of Passengers",
        min_value=1,
        max_value=100,
        value=2,
        step=1
    )

    vehicle = st.selectbox(
        "Vehicle Requirement",
        [
            "Any suitable vehicle",
            "Car",
            "SUV",
            "Tempo Traveller",
            "Mini Bus",
            "Bus"
        ]
    )

    additional_info = st.text_area(
        "Additional Requirements (Optional)",
        placeholder="Luggage, return trip, special requests..."
    )

    submitted = st.form_submit_button(
        "Submit Vehicle Requirement",
        use_container_width=True
    )


if submitted:

    name = name.strip()
    contact = contact.strip()
    pickup = pickup.strip()
    destination = destination.strip()

    if not name:
        st.error("Please enter the guest name.")

    elif not re.fullmatch(r"\+?[\d\s()-]{10,20}", contact):
        st.error("Please enter a valid contact number.")

    elif not pickup:
        st.error("Please enter the pickup location.")

    elif not destination:
        st.error("Please enter the destination.")

    elif "X" in WHATSAPP_NUMBER or not WHATSAPP_NUMBER.isdigit():
        st.error("Please configure WHATSAPP_NUMBER in app.py.")

    else:
        message = (
            "💒 WEDDING VEHICLE REQUIREMENT\n\n"
            f"Guest Name: {name}\n"
            f"Contact Number: {contact}\n"
            f"Travel Date: {booking_date.strftime('%d-%m-%Y')}\n"
            f"Pickup Time: {booking_time.strftime('%I:%M %p')}\n"
            f"Pickup Location: {pickup}\n"
            f"Destination: {destination}\n"
            f"Passengers: {guests}\n"
            f"Vehicle Required: {vehicle}\n"
            f"Additional Requirements: {additional_info.strip() or 'None'}"
        )

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}"
            f"?text={quote(message)}"
        )

        st.success("Your vehicle requirement is ready!")

        st.link_button(
            "Send Requirement on WhatsApp",
            whatsapp_url,
            use_container_width=True
        )

st.divider()

st.caption(
    "Please submit your transportation requirements in advance. "
    "Vehicle availability will be confirmed separately."
)
