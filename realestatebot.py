from tkinter import *
from tkinter import scrolledtext

# Function to handle chatbot responses
def get_response():
    user_input = user_entry.get().strip()
    if not user_input:
        return

    chat_log.insert(END, f"You: {user_input}\n")

    # Generate a response based on user input
    response = real_estate_advisor(user_input)
    chat_log.insert(END, f"Advisor: {response}\n\n")

    user_entry.delete(0, END)  # Clear the input box

# Chatbot logic for real estate advice
def real_estate_advisor(question):
    question = question.lower()
    
    # Sample responses
    if "buy" in question:
        return "Buying a property? Make sure to evaluate the location, price trends, and resale value. Always get the property inspected before closing the deal."
    elif "sell" in question:
        return "Selling? Boost your property's curb appeal and stage it well. Also, ensure proper paperwork and fair market pricing to attract serious buyers."
    elif "rent" in question:
        return "Looking to rent? Set a fair rental price and screen tenants carefully. Ensure a written lease agreement to avoid disputes."
    elif "investment" in question:
        return "For real estate investment, research high-demand areas, check rental yields, and diversify your portfolio. Patience is key for long-term returns."
    elif "location" in question:
        return "The location depends on your needs. For families, good schools and safety matter. For investments, focus on areas with growth potential."
    elif "loan" in question:
        return "Applying for a home loan? Maintain a good credit score, compare interest rates, and check eligibility criteria before applying."
    elif "tips" in question:
        return "General real estate tips: Always do your due diligence, work with trusted agents, and never skip legal checks or property inspections."
    else:
        return "I'm here to help with real estate questions! Could you rephrase or provide more details?"

# Create the main Tkinter window
root = Tk()
root.title("Real Estate Advisor")
root.geometry("500x600")
root.resizable(False, False)

# Header label
Label(root, text="🏡 Real Estate Advisor 🏡", font=("Helvetica", 16, "bold")).pack(pady=10)

# Chat log display
chat_log = scrolledtext.ScrolledText(root, width=60, height=25, wrap=WORD, state="normal", bg="#F0F0F0", font=("Helvetica", 10))
chat_log.pack(pady=10)
chat_log.insert(END, "Advisor: Hello! I’m your Real Estate Advisor. How can I help you today?\n\n")
chat_log.config(state="disabled")  # Disable editing directly in the chat log

# Enable adding text to the chat log
def enable_log_edit():
    chat_log.config(state="normal")

# Input box and button
frame = Frame(root)
frame.pack(pady=10)

user_entry = Entry(frame, width=40, font=("Helvetica", 12))
user_entry.pack(side=LEFT, padx=5)

send_button = Button(frame, text="Send", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=lambda: [enable_log_edit(), get_response(), chat_log.config(state="disabled")])
send_button.pack(side=LEFT)

# Main loop
root.mainloop()
