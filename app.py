
import re
from datetime import date, time

import requests
import streamlit as st


st.set_page_config(
    page_title="Booking Form",
    page_icon="📅",
    layout="centered",
)

st.title("Booking Form")


def send_whatsapp_message(name, booking_date, booking_time, contact):
    """Send an approved WhatsApp template through Meta Cloud API."""

    token = st.secrets["WHATSAPP_TOKEN"]
    phone_number_id = st.secrets["PHONE_NUMBER_ID"]
    receiver = st.secrets["WHATSAPP_RECEIVER"]
    api_version = st.secrets["GRAPH_API_VERSION"]
    template_name = st.secrets["TEMPLATE_NAME"]
    template_language = st.secrets["TEMPLATE_LANGUAGE"]

    url = (
        f"https://graph.facebook.com/"
        f"{api_version}/{phone_number_id}/messages"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": receiver,
        "type": "template",
        "template": {
            "name": template_name,
            "language": {"code": template_language},
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {"type": "text", "text": name},
                        {"type": "text", "text": booking_date},
                        {"type": "text", "text": booking_time},
                        {"type": "text", "text": contact},
                    ],
                }
            ],
        },
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=20,
    )

    if not response.ok:
        # Do not display the access token or request headers.
        try:
            error = response.json().get("error", {})
            message = error.get("message", "WhatsApp API request failed.")
        except ValueError:
            message = "WhatsApp API request failed."

        raise RuntimeError(message)

    return response.json()


with st.form("booking_form"):
    name = st.text_input("Name")
    selected_date = st.date_input("Date", value=date.today())
    selected_time = st.time_input("Time", value=time(10, 0))
    contact = st.text_input("Contact Number")

    submitted = st.form_submit_button("Submit")


if submitted:
    clean_name = name.strip()
    clean_contact = re.sub(r"[\s()+-]", "", contact.strip())

    if not clean_name:
        st.error("Please enter your name.")

    elif not re.fullmatch(r"\d{10,15}", clean_contact):
        st.error(
            "Enter a valid contact number with country code "
            "(10–15 digits)."
        )

    else:
        try:
            message_result = send_whatsapp_message(
                clean_name,
                selected_date.strftime("%d-%m-%Y"),
                selected_time.strftime("%I:%M %p"),
                contact.strip(),
            )

            message_id = (
                message_result.get("messages", [{}])[0].get("id")
            )

            st.success(
                "Details submitted and WhatsApp API accepted "
                "the message request."
            )

            if message_id:
                st.caption(f"Message ID: {message_id}")

        except KeyError as exc:
            st.error(
                f"Missing configuration in secrets.toml: {exc}"
            )

        except requests.RequestException:
            st.error(
                "Could not connect to WhatsApp. "
                "Check your internet connection and try again."
            )

        except RuntimeError as exc:
            st.error(f"WhatsApp API error: {exc}")

        except Exception:
            st.error(
                "Something went wrong. Check your configuration "
                "and Streamlit logs."
            )
