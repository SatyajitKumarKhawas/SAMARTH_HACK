import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')


def correct_spelling(text):
    """Correct spelling using TextBlob"""
    blob = TextBlob(text)
    return blob.correct()

def correct_grammar(text):
    """Basic grammar correction using TextBlob's syntactic features"""
    blob = TextBlob(text)
    # TextBlob automatically improves some grammatical structures in its correction
    return str(blob)

def find_errors(original_text, corrected_text):
    """Find the errors in the original text compared to the corrected text"""
    original_blob = TextBlob(original_text)
    corrected_blob = TextBlob(corrected_text)
    
    errors = []
    
    # Check for word-level differences
    for orig, corrected in zip(original_blob.words, corrected_blob.words):
        if orig != corrected:
            errors.append((orig, corrected))
    
    return errors

def main():
    st.title("Spelling and Grammar Checker using TextBlob")

    # Text input
    user_input = st.text_area("Enter your text here", height=200)

    if st.button("Correct Spelling and Grammar"):
        if user_input:
            # Correct spelling
            corrected_spelling = correct_spelling(user_input)

            # Correct grammar (TextBlob will adjust basic structure)
            corrected_text = correct_grammar(str(corrected_spelling))

            # Find errors made by the user
            errors = find_errors(user_input, corrected_text)

            # Display original text with errors
            st.subheader("Original Text")
            st.write(user_input)

            # Display the errors
            if errors:
                st.subheader("Errors Found:")
                for orig, corrected in errors:
                    st.write(f"Incorrect: '{orig}' -> Corrected: '{corrected}'")
            else:
                st.write("No spelling or grammar errors found.")

            # Display corrected text
            st.subheader("Corrected Text")
            st.write(corrected_text)
        else:
            st.warning("Please enter some text to check.")

if __name__ == "__main__":
    main()
