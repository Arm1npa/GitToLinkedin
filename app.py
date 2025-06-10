import streamlit as st
import os
from github import get_github_repo_info
from gemini import generate_linkedin_post

st.set_page_config(
    page_title="GitHub to LinkedIn Post Generator", layout="centered")

st.title("GitHub → LinkedIn Post Generator")

# Session state for tokens and drafts
if 'post_draft' not in st.session_state:
    st.session_state['post_draft'] = ''

# Step 1: Input GitHub repo link
github_url = st.text_input("Paste your GitHub repository link:")

tone = st.selectbox("Select the tone of the post:", [
                    "Professional", "Casual", "Enthusiastic"])
add_hashtags = st.checkbox("Add hashtags at the end of the post", value=True)

if st.button("Generate LinkedIn Post"):
    if github_url:
        with st.spinner("Fetching repo info and generating post..."):
            repo_info = get_github_repo_info(github_url)
            if repo_info:
                post = generate_linkedin_post(
                    repo_info, tone, add_hashtags=add_hashtags)
                st.session_state['post_draft'] = post
            else:
                st.error("Could not fetch repository info. Please check the link.")
    else:
        st.warning("Please enter a GitHub repository link.")

# Step 2: Show generated post
draft = st.text_area("Generated LinkedIn Post:",
                     value=st.session_state['post_draft'], height=200)
st.session_state['post_draft'] = draft
