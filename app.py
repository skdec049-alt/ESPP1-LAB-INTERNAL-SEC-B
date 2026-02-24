import streamlit as st
import random

def get_unique_sequences(total_rolls=60):
    """
    Generates a list of 5-number sequences for each roll number 
    ensuring no adjacent roll numbers share a value.
    """
    all_numbers = list(range(1, 31))
    assignments = {}
    last_set = set()

    # We use a fixed seed here so the entire 1-60 map is 
    # consistent every time the app re-runs.
    random.seed(42) 

    for roll in range(1, total_rolls + 1):
        # Find 5 numbers that do NOT intersect with the last_set
        available = [n for n in all_numbers if n not in last_set]
        
        # Pick 5 from the available pool
        current_set = random.sample(available, 5)
        current_set.sort()
        
        assignments[roll] = current_set
        last_set = set(current_set)
        
    return assignments

def main():
    st.set_page_config(page_title="Roll Number Portal", layout="centered")
    st.title("🔢 SELECT PROGRAM NO")
    
    # Restrict input between 1 and 60
    roll_no = st.number_input(
        "Enter Roll Number (50-110)", 
        min_value=50, 
        max_value=110, 
        step=1
    )

    # Pre-calculate the non-overlapping map
    data_map = get_unique_sequences(110)

    if st.button("View My Numbers"):
        my_numbers = data_map[roll_no]
        
        st.write(f"### Results for Roll No: **{roll_no}**")
        
        # Displaying numbers in a clean row
        cols = st.columns(5)
        for i, num in enumerate(my_numbers):
            cols[i].metric(label=f"Value {i+1}", value=num)
            
        # Comparison logic for peace of mind
        if roll_no > 1:
            prev_numbers = data_map[roll_no - 1]
            st.info(f"Note: These numbers are 100% different from Roll No {roll_no-1}.")

if __name__ == "__main__":
    main()
