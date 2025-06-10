import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from github import get_github_repo_info
from gemini import generate_linkedin_post
from dotenv import load_dotenv

load_dotenv()

class GitToLinkedInApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GitHub → LinkedIn Post Generator (Desktop)")
        self.geometry("700x600")
        self.create_widgets()

    def create_widgets(self):
        # GitHub link
        tk.Label(self, text="Paste your GitHub repository link:").pack(anchor='w', padx=10, pady=(10,0))
        self.github_url = tk.Entry(self, width=80)
        self.github_url.pack(padx=10, pady=5)

        # Tone
        tk.Label(self, text="Select the tone of the post:").pack(anchor='w', padx=10, pady=(10,0))
        self.tone = ttk.Combobox(self, values=["Professional", "Casual", "Enthusiastic"])
        self.tone.current(0)
        self.tone.pack(padx=10, pady=5)

        # Hashtags
        self.add_hashtags = tk.BooleanVar(value=True)
        tk.Checkbutton(self, text="Add hashtags at the end of the post", variable=self.add_hashtags).pack(anchor='w', padx=10, pady=5)

        # Generate button
        self.generate_btn = tk.Button(self, text="Generate LinkedIn Post", command=self.generate_post)
        self.generate_btn.pack(pady=10)

        # Output
        tk.Label(self, text="Generated LinkedIn Post:").pack(anchor='w', padx=10, pady=(10,0))
        self.output = scrolledtext.ScrolledText(self, width=80, height=20, wrap=tk.WORD)
        self.output.pack(padx=10, pady=5)

    def generate_post(self):
        url = self.github_url.get().strip()
        tone = self.tone.get()
        add_hashtags = self.add_hashtags.get()
        self.output.delete(1.0, tk.END)
        if not url:
            messagebox.showwarning("Input required", "Please enter a GitHub repository link.")
            return
        self.output.insert(tk.END, "Fetching repo info and generating post...\n")
        self.update()
        repo_info = get_github_repo_info(url)
        if not repo_info:
            self.output.insert(tk.END, "Could not fetch repository info. Please check the link.\n")
            return
        post = generate_linkedin_post(repo_info, tone, add_hashtags=add_hashtags)
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, post)

if __name__ == "__main__":
    app = GitToLinkedInApp()
    app.mainloop()
