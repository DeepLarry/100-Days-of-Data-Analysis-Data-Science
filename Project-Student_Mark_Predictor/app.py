import streamlit as st

# --- STEP 1: THE BLUEPRINT (Class) ---
class StudentPredictor:
    def __init__(self, hours, attendance, assignments):
        self.hours = hours
        self.attendance = attendance
        self.assignments = assignments
        
    def calculate_marks(self):
        result = (self.hours * 5) + (self.attendance * 0.3) + (self.assignments * 2)
        return result

    def get_performance(self, marks):
        if marks > 80:
            return "Excellent performance"
        elif marks >= 60:
            return "Good performance"
        else:
            return "Needs improvement"

# --- STEP 2: STREAMLIT UI (Web Interface) ---
st.title("🎓 Student Performance Predictor")

# Creating input boxes for the user
h_input = st.number_input("Enter study hours:", 0.0, 24.0, 5.0)
att_input = st.number_input("Enter attendance %:", 0.0, 100.0, 80.0)
ass_input = st.number_input("Enter assignments completed:", 0, 50, 7)

if st.button("Predict"):
    # 1. Create the object using the user's inputs
    # This is where OOP happens!
    predictor_obj = StudentPredictor(h_input, att_input, ass_input)
    
    # 2. Use the object's methods to get results
    final_marks = predictor_obj.calculate_marks()
    status = predictor_obj.get_performance(final_marks)
    
    # 3. Show the output
    st.divider()
    st.success(f"### Predicted Marks: {final_marks}")
    st.info(f"### Performance: {status}")