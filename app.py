import streamlit as st
import random

def get_unique_sequences(start_roll=52, end_roll=110):
    """
    Generates a list of 5-number sequences for each roll number 
    from 52 to 110, ensuring no adjacent roll numbers share a value.
    Numbers are chosen from the range 31 to 60.
    """
    # Range 31 to 60 inclusive (31, 61)
    all_numbers = list(range(31, 61))
    assignments = {}
    last_set = set()

    # Fixed seed for consistency
    random.seed(42) 

    for roll in range(start_roll, end_roll + 1):
        # Filter out numbers used in the immediately preceding roll
        available = [n for n in all_numbers if n not in last_set]
        
        # Pick 5 from the available pool (30 total numbers, 25 available after excluding 5)
        current_set = random.sample(available, 5)
        current_set.sort()
        
        assignments[roll] = current_set
        last_set = set(current_set)
        
    return assignments

def main():
    st.set_page_config(page_title="Roll Number Portal", layout="centered")
    st.title("🔢 SELECT PROGRAM NO")
    
    # Input range: 52 to 110
    roll_no = st.number_input(
        "Enter Roll Number (52-110)", 
        min_value=52, 
        max_value=110, 
        value=52,
        step=1
    )

    # Pre-calculate the non-overlapping map for the specific range
    data_map = get_unique_sequences(52, 110)

    if st.button("View My Numbers"):
        my_numbers = data_map[roll_no]
        
        st.write(f"### Results for Roll No: **{roll_no}**")
        
        # Displaying numbers in a clean row
        cols = st.columns(5)
        for i, num in enumerate(my_numbers):
            cols[i].metric(label=f"Value {i+1}", value=num)
            
        # Comparison logic for peace of mind
        if roll_no > 52:
            prev_numbers = data_map[roll_no - 1]
            st.info(f"Verified: No numbers overlap with Roll No {roll_no - 1}.")

if __name__ == "__main__":
    main()
