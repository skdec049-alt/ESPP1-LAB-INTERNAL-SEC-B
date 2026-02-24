import streamlit as st
import random

def get_unique_sequences(target_roll, total_range=110):
    """
    Generates 5-number sequences up to the target roll number 
    ensuring no adjacent rolls share a value.
    """
    all_numbers = list(range(1, 31))
    assignments = {}
    last_set = set()

    # REMOVED: random.seed(42) - This allows for true randomness on each run.

    for roll in range(1, target_roll + 1):
        # Find numbers that do NOT intersect with the previous roll
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
    
    # Input for Roll Number
    roll_no = st.number_input(
        "Enter Roll Number", 
        min_value=1, 
        max_value=110, 
        value=50,
        step=1
    )

    # We only generate numbers when the button is pressed
    if st.button("Generate New Numbers"):
        # Pre-calculate sequences up to the selected roll number
        data_map = get_unique_sequences(roll_no)
        my_numbers = data_map[roll_no]
        
        st.write(f"### Results for Roll No: **{roll_no}**")
        
        # Displaying numbers in metrics
        cols = st.columns(5)
        for i, num in enumerate(my_numbers):
            cols[i].metric(label=f"Value {i+1}", value=num)
            
        # Validation message
        if roll_no > 1:
            prev_numbers = data_map[roll_no - 1]
            st.success(f"Verified: These are different from Roll No {roll_no-1}.")
            with st.expander("Show Previous Roll Numbers"):
                st.write(f"Roll No {roll_no-1}: {prev_numbers}")

if __name__ == "__main__":
    main()
