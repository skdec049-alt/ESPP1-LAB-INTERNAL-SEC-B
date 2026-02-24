import streamlit as st
import random
import os

def get_unique_sequences(target_roll):
    all_numbers = list(range(1, 31))
    assignments = {}
    last_set = set()

    # This ensures that even if you copy the code to app1.py, 
    # the "randomness" is fresh every time the script starts.
    random.seed(None) 

    for roll in range(1, target_roll + 1):
        available = [n for n in all_numbers if n not in last_set]
        current_set = random.sample(available, 5)
        current_set.sort()
        
        assignments[roll] = current_set
        last_set = set(current_set)
        
    return assignments

def main():
    st.set_page_config(page_title="Unique Roll Portal")
    st.title("🔢 Unique Number Generator")
    
    roll_no = st.number_input("Enter Roll Number", min_value=1, max_value=110, value=1)

    if st.button("Generate Numbers"):
        # Every click or refresh will now produce a brand new set
        data_map = get_unique_sequences(roll_no)
        my_numbers = data_map[roll_no]
        
        st.write(f"### Results for Roll No: **{roll_no}**")
        
        cols = st.columns(5)
        for i, num in enumerate(my_numbers):
            cols[i].metric(label=f"Value {i+1}", value=num)

        st.toast("New unique sequence generated!", icon="🎲")

if __name__ == "__main__":
    main()
