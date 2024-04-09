import dbconnect as db
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Book Hotel Room",
    page_icon="🛏️"
)

# Function to add a booking
def add_booking():
    with st.form("bookHotel"):
        guest_name = st.text_input("Enter Guest Name")
        hotel_name = st.text_input("Enter Hotel Name")
        room_number = st.number_input("Enter Room Number", step=1)
        check_in_date = st.date_input("Check-in Date")
        check_out_date = st.date_input("Check-out Date")
        submit = st.form_submit_button("Book Room")

    if guest_name and hotel_name and room_number and check_in_date and check_out_date and submit:
        # Perform booking insertion into the database
        sql = "INSERT INTO bookings (guest_name, hotel_name, room_number, check_in_date, check_out_date) VALUES (%s, %s, %s, %s, %s)"
        val = (guest_name, hotel_name, room_number, check_in_date, check_out_date)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        st.success("Room booked successfully!")
    else:
        st.warning("Please fill in all fields.")

# Function to delete a booking
def delete_booking():
    with st.form("deleteBooking"):
        booking_id = st.number_input("Enter Booking ID to delete", step=1)
        submit = st.form_submit_button("Delete Booking")

    if booking_id and submit:
        # Perform booking deletion from the database
        sql = "DELETE FROM bookings WHERE id = %s"
        val = (booking_id,)
        db.mycursor.execute(sql, val)
        db.mydb.commit()
        st.success("Booking deleted successfully!")
    else:
        st.warning("Please fill in all fields.")

# Function to view all bookings
def view_bookings():
    # Retrieve all bookings from the database
    db.mycursor.execute("SELECT * FROM bookings")
    bookings = db.mycursor.fetchall()

    st.write("### All Bookings")
    if not bookings:
        st.write("No bookings found.")
    else:
        import pandas as pd
        df = pd.DataFrame(bookings, columns=[i[0] for i in db.mycursor.description])
        st.dataframe(df)

# Main code
def main():
    st.title("Book Hotel Room")

    # Define tabs
    tabs = ["Book Room", "Delete Booking", "View Bookings"]
    selected_tab = st.radio("Select Action", tabs)

    # Handle each tab's functionality
    if selected_tab == "Book Room":
        add_booking()
    elif selected_tab == "Delete Booking":
        delete_booking()
    elif selected_tab == "View Bookings":
        view_bookings()

    st.write("____")

if __name__ == "__main__":
    main()


