import streamlit as st
import requests
from streamlit_lottie import st_lottie
from datetime import datetime
import time

# page configuration
st.set_page_config(
    page_title="Personal Library Management System",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

#  CSS for styling
st.markdown("""
<style>
    .main-header{
        font-size: 3rem !important;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1) !important;     
    }

    .sub_header {
        font-size: 1.8rem !important;
        color: #3882F6;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    .stButton>button {
        border-radius: 0.375rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("<h1> Choose an option:</h1>", unsafe_allow_html=True)

# Lottie animation
def load_lottie_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

lottie_book = load_lottie_url("https://assets9.lottiefiles.com/temp/1f20_aKAFIn.json")
if lottie_book:
    with st.sidebar:
        st_lottie(lottie_book, height=200, key='book_animation')

nav_option = st.sidebar.radio(
    "",
    ["View Library", "Add Book", "Search Book", "Library Statistics"]
)

# session state for book storage
if 'library' not in st.session_state:
    st.session_state.library = []

# Function to save books 
def save_library():
    pass  

# Function to add book to session state
def add_book(title, author, publication_year, genre, read_status):
    book = {
        'title': title,
        'author': author,
        'publication_year': publication_year,
        'genre': genre,
        'read_status': read_status,
        'added_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.library.append(book)
    save_library()
    st.success("Book added successfully!")
    time.sleep(0.5)  # Animation delay

# Main header
st.markdown("<h1 class='main-header'>Library Manager </h1>", unsafe_allow_html=True)

# Navigation 
if nav_option == "Add Book":
    st.markdown("<h2 class='sub_header'> Add a New Book</h2>", unsafe_allow_html=True)

    # Error message 
    error_message = ""

    with st.form(key='add_book_form'):
        col1 = st.columns(1)[0]  # Single column layout
        with col1:
            title = st.text_input("Book Title", max_chars=100)
            author = st.text_input("Author", max_chars=100)
            publication_year = st.number_input("Publication Year", max_value=2025, step=1, value=2025)
            genre = st.selectbox("Genre", [
                "Fiction", "Non-Fiction", "Science", "Technology", "Fantasy", "Romance",
                "History", "Thriller", "Psychology", "Philosophy", "Biographies"
            ])
            read_status = st.radio("Have you read this book?", ("Yes", "No"))

        submit_button = st.form_submit_button("Submit")

        # Validation
        if submit_button:
            if not title.strip() or not author.strip():
                error_message = "❌ Title and Author fields cannot be empty!"
            else:
                add_book(title, author, publication_year, genre, read_status)

    # Display error message 
    if error_message:
        st.error(error_message)

elif nav_option == "View Library":
    st.markdown("<h2 class='sub_header'> Your Library </h2>", unsafe_allow_html=True)
    
    if len(st.session_state.library) == 0:
        st.info("No books added yet.")
    else:
        for idx, book in enumerate(st.session_state.library):
            with st.expander(f"📖 {book['title']} by {book['author']}"):
                st.write(f"**Publication Year:** {book['publication_year']}")
                st.write(f"**Genre:** {book['genre']}")
                st.write(f"**Read Status:** {book['read_status']}")
                st.write(f"**Added on:** {book['added_date']}")


elif nav_option == "Search Book":
    st.markdown("<h2 class='sub_header'> Search Books </h2>", unsafe_allow_html=True)
    search_term = st.text_input("Enter search term")
    search_by = st.radio("Search by", ["Title", "Author", "Genre"])
    search_button = st.button("Search")

    if search_button:
        results = [
            book for book in st.session_state.library
            if search_term.lower() in book[search_by.lower()].lower()
        ]
        
        if results:
            st.success(f"Found {len(results)} book(s).")
            for book in results:
                with st.expander(f"📖 {book['title']} by {book['author']}"):
                    st.write(f"**Publication Year:** {book['publication_year']}")
                    st.write(f"**Genre:** {book['genre']}")
                    st.write(f"**Read Status:** {book['read_status']}")
                    st.write(f"**Added on:** {book['added_date']}")
        else:
            st.warning("No matching books found.")

elif nav_option == "Library Statistics":
    st.markdown("<h2 class='sub_header'> Library Statistics </h2>", unsafe_allow_html=True)
    
    if len(st.session_state.library) == 0:
        st.info("No data available.")
    else:
        total_books = len(st.session_state.library)
        read_books = sum(1 for book in st.session_state.library if book["read_status"] == "Yes")
        unread_books = total_books - read_books

        st.write(f"📚 **Total Books:** {total_books}")
        st.write(f"✔ **Books Read:** {read_books}")
        st.write(f"⏳ **Books Unread:** {unread_books}")
