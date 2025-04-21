# 📸 InstaTerminal

A fully-functional, terminal-based Instagram-like app written in Python — designed with 💖, built with ☕, and polished through days of love and code.

## ✨ About the Project

InstaTerminal is a command-line social media platform that simulates the core features of Instagram using only terminal inputs and JSON file storage. The project was developed with a strong emphasis on code quality, user experience, and data integrity.

## 🚀 Features

### 👤 User Authentication
- Secure **signup** and **login** system
- Proper **input validation** and **exception handling**
- Friendly error messages with `rich`

### 🏠 Home Section
- View **posts** from followed users
- Like ❤️, comment 💬, save 🔖, and share ✉ posts
- Publish new posts with captions
- Interact with **stories** (watch, like)
- Create and manage **private/group chats**

### 🔍 Explore/Search
- Search for users by username
- View public or private profiles
- **Follow / Unfollow** functionality with support for:
  - **Public accounts** (instant follow)
  - **Private accounts** (send/receive follow requests)
- **Block / Unblock** other users

### 📨 Follow Requests Management
- See all pending requests
- Approve or reject individually or in bulk
- Real-time update of followers/following count

### 🧑‍💻 Profile Page
- Edit profile info (name, username, bio)
- Toggle between **public/private** account
- View own posts and saved posts
- Manage **blocked users list**

## 📂 Data Storage
All user data is stored in readable and editable `.json` files:
- `users.json` – user accounts, followers, posts, etc.
- `posts.json` – post metadata, likes, comments
- `messages.json` – private/group chat logs

> ❗ No database required. Just pure JSON magic!

## 🎨 Terminal UI
Thanks to the [rich](https://github.com/Textualize/rich) library, InstaTerminal features:
- Styled panels
- Colorful text
- Clear layout for better readability

## 🧠 Development Principles

- ✔ Follows **PEP 8** and clean code practices  
- ✔ Fully **modular** and easy to extend  
- ✔ Includes **meaningful docstrings and comments**  
- ✔ **Robust against bad inputs** (won’t crash!)  
- ✔ Uses **virtual environment** with requirements exported

## 🛠 Installation

```bash
git clone https://github.com/your-username/InstaTerminal.git
cd InstaTerminal
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py

