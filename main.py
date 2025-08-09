import streamlit as st
import qrcode
from qrcode.constants import ERROR_CORRECT_M
from io import BytesIO

st.title("📷 Simple QR Code Generator")

# Input
x = st.text_input('Enter the text or URL:')

if st.button('Generate QR') and x:
    with st.spinner('Generating....'):
        
        # Create QR object
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_M,
            box_size=10,
            border=4
        )
        qr.add_data(x)
        qr.make(fit=True)

    # Generate image
    img = qr.make_image(fill_color="black", back_color="white")
    

    # Convert PIL image to bytes
    
    y = BytesIO()
    img.save(y, format='PNG')
    z = y.getvalue()
    
    st.image(z , caption="Your Generated QR")
   
   