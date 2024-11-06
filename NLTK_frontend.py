import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

st.markdown(
    """
    <style>
    .stApp {
        background-color: gray;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize Streamlit app
st.title("NLP Application with Streamlit")

# Text input area for user-provided text
#user_text = st.text_area("Enter your text here:", "Artificial Intelligence is transforming the world...")
# Define options
# Get user input text



st.write("Choose an operation to perform on your text:")
option = st.selectbox("Operations", ["Tokenize", "Show Stop Words", "Apply Stemming", "Generate Word Cloud"])

# Sidebar options for user actions
# option = st.sidebar.selectbox(
#     "Choose an action",
#     ["Show Tokens", "Show Stop Words", "Apply Stemming", "Generate Word Cloud"]
# )

# Tokenization
if option == "Tokenize":
    user_text = st.text_area("Enter your text here", "")

    tokens = word_tokenize(user_text)
    st.subheader("Tokens")
    st.write(tokens)

elif option == "Show Stop Words":
    user_text = st.text_area("Enter your text here", "")

    tokens = word_tokenize(user_text)
    st_words = set(stopwords.words('english'))
    
    # Filter out the stop words from the tokens
    filtered_tokens = [word for word in tokens if word.lower() not in st_words]
    
    st.subheader("Tokens without Stop Words")
    st.write(filtered_tokens)

    # Show the list of stop words
    #st.subheader("List of Stop Words")
    #st.write(list(st_words))
# Stemming
elif option == "Apply Stemming":
    word = st.text_input("Enter a word to stem:", "affection")
    pst = PorterStemmer()
    stemmed_word = pst.stem(word)
    st.subheader("Stemmed Word")
    st.write(f"Original Word: {word}")
    st.write(f"Stemmed Word: {stemmed_word}")

# Word Cloud
elif option == "Generate Word Cloud":
    user_text = st.text_area("Enter your text here", "Artificial Intelligence refers to the intelligence of machines...")
    wordcloud = WordCloud(width=420, height=200, margin=2, background_color='black', colormap='Accent').generate(user_text)
    st.subheader("Word Cloud")
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)
