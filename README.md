# GitHub → LinkedIn Post Generator (Desktop)

A simple desktop app to auto-generate a professional LinkedIn post about any GitHub repository using Google Gemini.

## Features
- **Paste a GitHub repository link** and fetch project info (name, description, languages, topics, README)
- **Select the tone** of the post: Professional, Casual, or Enthusiastic
- **Optionally add hashtags** (from repo topics/languages) at the end of the post
- **Generate a highly professional, well-structured LinkedIn post** using Google Gemini API
- **Copy and use the post anywhere** (no LinkedIn login required)
- **No browser or web server needed** – runs as a native Windows app

## How to Use
1. Run the app (either with Python or the provided .exe)
2. Paste your GitHub repository link
3. Select your preferred tone and whether to add hashtags
4. Click "Generate LinkedIn Post"
5. Copy the generated post and use it on LinkedIn or anywhere else

## Setup (for developers)
1. Clone the repository
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your Gemini API key in a `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
4. Run the app:
   ```bash
   python desktop_app.py
   ```

## Build Windows Executable
To build a standalone Windows executable:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole desktop_app.py
```
The exe will be in the `dist/` folder.

## Notes
- No user data is stored.
- Requires internet access for Gemini API and GitHub API.
- No LinkedIn login or posting is performed; you only get the generated post text.

## License
MIT
