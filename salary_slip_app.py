import streamlit as st
import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import io
import base64

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@3179",
    database="salary_slip_app"
)

# Create a cursor to interact with the database
cursor = connection.cursor()

# Fetch data from the database
query = "SELECT * FROM demo_salary_file"
cursor.execute(query)
data = cursor.fetchall()

# Extract relevant data columns
employees_code = [row[1] for row in data]
# Extract other necessary data columns here

# Streamlit app layout
st.title('Employee Salary Slip Generator')
st.sidebar.title('Options')

# Add UI elements
selected_month = st.sidebar.selectbox('Select Month', ["February'22", "March'22","April'22","May'22","June'22","July'22","August'22","September'22","October'22","November'22","December'22","January'23","Feburary'23", "March'23","April'23","May'23","June'23","July'23"])  # Add all month names
selected_employee_code = st.sidebar.selectbox('Select Employee Code', employees_code)

# Fetch data for the selected month
selected_month_table = f"demo_salary_file_{selected_month.lower()}"
query = f"SELECT * FROM {selected_month_table}"
cursor.execute(query)
data = cursor.fetchall()

# Filter data based on selections
selected_employee_data = [row for row in data if row[1] == selected_employee_code]

# Display selected employee data
if selected_employee_data:
    selected_row = selected_employee_data[0]
    st.write("Selected Employee Data:")
    st.write(f"Employee Code: {selected_row[1]}")
    st.write(f"Employee Name: {selected_row[2]}")
    st.write(f"Employee Designation: {selected_row[3]}")
    st.write(f"Employee Department: {selected_row[4]}")
    st.write(f"Employee In Hand Salary: {selected_row[32]}")

    # Provide the option to view the salary slip as a letter
    if st.button("View Salary Slip"):
        # Generate the PDF content
        pdf_buffer = io.BytesIO()
        pdf = canvas.Canvas(pdf_buffer, pagesize=(792, 612))
        
        # Generate the PDF content
    pdf_buffer = io.BytesIO()
    pdf = canvas.Canvas(pdf_buffer, pagesize=(792, 612))

    # Add content to the PDF
    text_x = 100
    text_y = 600

    pdf.setFont("Helvetica", 12)  # Set default font size and color
    pdf.setFillColorRGB(0, 0, 0)  # Reset fill color to black

    # Draw "Salary Slip" with different font size and color
    pdf.setFont("Helvetica-Bold", 22)
    pdf.setFillColorRGB(0.2, 0.4, 0.8)
    pdf.drawString(310, 480, "SALARY SLIP")
    underline_width = pdf.stringWidth("SALARY SLIP")
    pdf.rect(310, 475, underline_width, 1, fill=1)

    # Draw the header sepration line
    pdf.rect(60, 470, 680,1, fill=1)

    # middel content
    pdf.setFont("Helvetica-Bold", 11)  # Set font for fixed labels
    pdf.setFillColorRGB(0, 0, 0)  
    pdf.drawString(60, 450, "EMP Code :")
    pdf.drawString(60, 430, "EMP Name :")
    pdf.drawString(60, 410, "Designation :")
    pdf.drawString(60, 390, "Date of joining :")
    pdf.drawString(60, 370, "Department :")
    pdf.drawString(60, 350, "UAN NO. :")
    pdf.drawString(60, 330, "ESIC NO. :")
    # Parallel content
    pdf.drawString(500, 450, "MONTH OF :")
    pdf.drawString(500, 430, "MONTH DAYS :")
    pdf.drawString(500, 410, "PAID DAYS :")
    pdf.drawString(500, 390, "WEEKLY OFF :")
    pdf.drawString(500, 370, "OT HOURS :")
    pdf.drawString(500, 350, "ACCOUNT NO :")
    pdf.drawString(500, 330, "IFSC CODE :")
    # Input string
    pdf.setFont("Helvetica", 11)  # Set font for dynamic data
    
    pdf.drawString(230, 430, f"{selected_row[2]}")
    pdf.drawString(230, 410, f"{selected_row[3]}")
    pdf.drawString(230, 390, f"{selected_row[0]}")
    pdf.drawString(230, 370, f"{selected_row[4]}")
    pdf.drawString(230, 350, f"{selected_row[5]}")
    pdf.drawString(230, 330, f"{selected_row[6]}")
    # Parrallel content
    pdf.drawString(655, 450, f"June'23")
    pdf.drawString(665, 430, f"30")
    pdf.drawString(665, 410, f"{selected_row[17]}")
    pdf.drawString(665, 390, f"{selected_row[18]}")
    pdf.drawString(665, 370, f"{selected_row[19]}")
    pdf.drawString(640, 350, f"{selected_row[8]}")
    pdf.drawString(640, 330, f"{selected_row[9]}")
    
    
    
    # Draw the two middle line 
    pdf.rect(60, 300, 680,1, fill=1)
    pdf.rect(60, 280, 680,1, fill=1)
    pdf.line(500,280,500,300)


    # between the line content
    pdf.setFont("Helvetica-Bold", 12)
    pdf.setFillColorRGB(0, 0, 0)   
    pdf.drawString(70, 287, "MONTHLY EARNINGS")
    pdf.drawString(340, 287, "CURRENT EARNING")
    pdf.drawString(580, 287, "DEDUCTION")

    # between double line content
    pdf.setFont("Helvetica-Bold", 11)
    pdf.setFillColorRGB(0, 0, 0)  
    pdf.drawString(60, 260, "NET BASIC+DA") 
    pdf.drawString(60, 240, "HRA")
    pdf.drawString(60, 220, "SPECIAL ALLOWANCE")
    pdf.drawString(60, 200, "BONUS")
    pdf.drawString(60, 180, "WEEKLY OFF")
    pdf.drawString(60, 160, "OVERTIME")
    pdf.drawString(60, 140, "INCENTIVE")
    pdf.drawString(60, 120, "STAR AWARD")
    pdf.drawString(60, 87, "GROSS SALARY")
    # Parrallel 
    pdf.drawString(500, 260, "EPF 12% ")
    pdf.drawString(500, 240, "ESIC 0.75%")
    pdf.drawString(500, 220, "ADVANCE")
    pdf.drawString(500, 200, "TDS")
    pdf.drawString(500, 105, "TOTAL DEDUCTION")
    pdf.drawString(500, 87, "NET SALARY")  
    # Input string  
    pdf.setFont("Helvetica", 11)
    pdf.drawString(250, 260, f"{selected_row[11]}")
    pdf.drawString(250, 240, f"{selected_row[13]}")
    pdf.drawString(250, 220, f"{selected_row[14]}")
    pdf.drawString(255, 200, f"{selected_row[15]}")
    pdf.drawString(260, 180,            "0")
    pdf.drawString(260, 160,            "0")
    pdf.drawString(260, 140,            "0")
    pdf.drawString(260, 120,            "0")
    # Parallel
    pdf.drawString(400, 260, f"{selected_row[20]}")
    pdf.drawString(400, 240, f"{selected_row[22]}")
    pdf.drawString(400, 220, f"{selected_row[23]}")
    pdf.drawString(400, 200, f"{selected_row[24]}")
    pdf.drawString(400, 180, f"{selected_row[26]}")
    pdf.drawString(400, 160, f"{selected_row[25]}")
    pdf.drawString(400, 140,            "0")
    pdf.drawString(400, 120,            "0")
    # second parralel
    pdf.drawString(655, 260, f"{selected_row[29]}")
    pdf.drawString(655, 240, f"{selected_row[30]}")
    pdf.drawString(655, 220,            "0")
    pdf.drawString(655, 200,            "0")
    pdf.drawString(655, 105, f"{selected_row[31]}")
    # Higlighted
    pdf.setFont("Helvetica-Bold", 12)
    pdf.setFillColorRGB(0, 0, 0)
    pdf.drawString(230, 450, f"{selected_row[1]}")
    pdf.drawString(400, 87, f"{selected_row[28]}")
    pdf.drawString(655, 87, f"{selected_row[32]}")

    # Draw the two tail line 
    pdf.rect(60, 100, 680,1, fill=1)
    pdf.rect(60, 80, 680,1, fill=1)

     

    # Draw "Tail line" 
    pdf.setFont("Helvetica-Bold", 16)
    pdf.setFillColorRGB(0, 0, 0)  # Reset fill color to black
    pdf.drawString(125, 60, "** This is system generated payslip do not require any Seal or Signature **")

    # Draw "address" with different font size
    pdf.setFont("Helvetica-Bold", 16)
    pdf.setFillColorRGB(0, 0, 0)  # Reset fill color to black
    pdf.drawString(150, 515, "Plot No-62, Lan No-2, Gopalbari, Near Ajmer Puliya, Jaipur-302001")
        
    

    # Add employee photo if available
    photo_path = (r"C:\Salary_slip_maker_streamlit\attachments\Picture1.jpg")  # Replace with the appropriate column index or key
    if photo_path:
        photo = ImageReader(photo_path)
        pdf.drawImage(photo, 10, 530, width=760, height=100)  # Adjust the positioning and size

    # Save the PDF
    pdf.save()
    pdf_buffer.seek(0)

    

    # Display the generated salary slip PDF within an iframe
    pdf_base64 = base64.b64encode(pdf_buffer.read()).decode("utf-8")
    pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    # Provide the option to download the PDF
    st.download_button(
        label="Download PDF",
        data=pdf_buffer,
        file_name=f"salary_slip_{selected_row[1]}.pdf",
        mime="application/pdf"
    )
    
else:
    st.write("Sorry, data not available for the selected employee code.")

# Close the cursor and connection
cursor.close()
connection.close()
