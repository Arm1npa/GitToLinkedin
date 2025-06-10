import os
import google.generativeai as genai


def generate_linkedin_post(repo_info, tone, add_hashtags=False):
    """Generate a highly professional, well-structured LinkedIn post using Google Gemini API."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "[Gemini API key not set]"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.0-flash')
    hashtags = ''
    if add_hashtags:
        # Generate hashtags from topics and languages
        tags = repo_info['topics'] + repo_info['languages']
        hashtags = '\n' + \
            ' '.join(f"#{tag.replace(' ', '')}" for tag in tags if tag)
    prompt = f"""
You are a professional technical content writer. Write a highly polished, engaging, and well-structured LinkedIn post (3-5 sentences, with clear paragraphing and advanced vocabulary) about the following GitHub project. The post should:
- Start with a respectful greeting to the audience (e.g., 'Hello esteemed professionals,' or 'Greetings to all tech enthusiasts,').
- Then, provide a strong, attention-grabbing introduction.
- Clearly explain the main features and technical highlights.
- Emphasize the value and potential impact for the tech community or industry.
- End with a compelling call to action to check out the repository.
- Use professional, confident, and inspiring language.
- Format the post with logical paragraphs and line breaks for readability.
- Always mention the GitHub repository link as the last line of the post, starting with: 'GitHub repository: {repo_info['html_url']}'
- If hashtags are provided, add them as a separate paragraph at the end.

Project name: {repo_info['name']}
Description: {repo_info['description']}
Languages: {', '.join(repo_info['languages'])}
Topics: {', '.join(repo_info['topics'])}
README:
{repo_info['readme'][:1500]}
GitHub link: {repo_info['html_url']}
Hashtags: {hashtags}
"""
    try:
        response = model.generate_content(prompt)
        post = response.text.strip()
        # Ensure the GitHub link is always the last line before hashtags
        github_line = f"GitHub repository: {repo_info['html_url']}"
        if github_line not in post:
            # Remove any existing GitHub link lines
            lines = [l for l in post.split('\n') if 'github.com' not in l.lower()]
            post = '\n'.join(lines)
            post += f"\n\n{github_line}"
        if add_hashtags and hashtags.strip():
            if hashtags.strip() not in post:
                post += f"\n\n{hashtags.strip()}"
        return post
    except Exception as e:
        return f"[Gemini error: {e}]"
