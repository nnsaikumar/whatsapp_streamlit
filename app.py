import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Wedding Vehicle Arrangement",
    page_icon="💒",
    layout="centered",
)

WHATSAPP_NUMBER = "919440882425"  # Replace with your number

st.title("💒 Wedding Vehicle Arrangement")

components.html(
    f"""
    <form id="vehicleForm">
        <label>Guest Name *</label>
        <input id="name" required placeholder="Enter your full name">

        <label>Contact Number *</label>
        <input id="contact" required type="tel"
               placeholder="Enter mobile number">

        <label>Travel Date *</label>
        <input id="travelDate" required type="date">

        <label>Pickup Time *</label>
        <input id="pickupTime" required type="time" value="09:00">

        <label>Number of Passengers</label>
        <input id="passengers" type="number" min="1" max="100" value="2">

        <label>Additional Requirements</label>
        <textarea id="additional"
                  placeholder="Enter additional requirements"></textarea>

        <button type="submit">Submit Vehicle Requirement</button>
    </form>

    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        label {{
            display: block;
            margin-top: 14px;
            margin-bottom: 6px;
            font-weight: 600;
        }}
        input, textarea {{
            width: 100%;
            box-sizing: border-box;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }}
        button {{
            width: 100%;
            margin-top: 20px;
            padding: 12px;
            background: #128C7E;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }}
    </style>

    <script>
        document.getElementById("vehicleForm").addEventListener("submit", function(e) {{
            e.preventDefault();

            const name = document.getElementById("name").value.trim();
            const contact = document.getElementById("contact").value.trim();
            const travelDate = document.getElementById("travelDate").value;
            const pickupTime = document.getElementById("pickupTime").value;
            const passengers = document.getElementById("passengers").value;
            const additional = document.getElementById("additional").value.trim() || "None";

            const message =
                "💒 WEDDING VEHICLE REQUIREMENT\\n\\n" +
                "Guest Name: " + name + "\\n" +
                "Contact Number: " + contact + "\\n" +
                "Travel Date: " + travelDate + "\\n" +
                "Pickup Time: " + pickupTime + "\\n" +
                "Number of Passengers: " + passengers + "\\n" +
                "Additional Requirements: " + additional;

            const url = "https://wa.me/{WHATSAPP_NUMBER}?text=" +
                        encodeURIComponent(message);

            window.location.href = url;
        }});
    </script>
    """,
    height=680,
)