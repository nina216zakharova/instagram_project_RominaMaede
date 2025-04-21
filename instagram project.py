from typing import Dict
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
import re
import json
import os
console=Console()
DATABASE_FILE="database.json"
def show_main_menu():
    console.print(Panel.fit("[bold pink]Welcome to InstaRominaMaede [/bold pink]", border_style="magenta"))
    console.print("[1] Sign Up", style="cyan")
    console.print("[2] Log In", style="cyan")
    console.print("[3] Exit", style="cyan")
    choice=Prompt.ask("\n[bold yellow]Choose an ooption[/bold yellow]", choices=["1", "2", "3"])
    return choice
def main():
    while True:
        choice=show_main_menu()
        if choice=="1":
            console.print("\n[bold green] Sign Up selected[/bold green]\n")
            sign_up()
        elif choice=="2":
            console.print("\n[blod green] Log In selected[/bold green]\n")
            logged_in_user=login()
            if logged_in_user:
                pass
        elif choice=="3":
            console.print("\n[bold green] Goodbye![/bold green]\n")
            break
def load_users() -> Dict[str, Dict]:
    try:
        with open(DATABASE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
def save_users(users: Dict[str, Dict]) -> None:
    with open(DATABASE_FILE,"w") as f:
        json.dump(users, f, indent=4)
def is_valid_email(email: str) -> bool:
    pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
def sign_up() -> None:
    print(Panel("[bold cyan]Sign Up[/bold cyan]"))
    users= load_users()
    email=Prompt.ask("Would you please enter your [green]email[/green]?").strip()
    username=Prompt.ask("How about a [green]username[/green]?").strip()
    password=Prompt.ask("Now, set a [green]password[/green]", password=True).strip()
    if not is_valid_email(email):
        print("[bold red]INVALID EMAIL![/bold red]")
        return
    if email in [info["email"] for info in users.values()]:
        print("[bold red]EMAIL HAS ALREADY BEEN REGISTERED![/bold red]")
        return
    if username in users:
        print("[bold red]USERNAME HASALREDY BEEN TAKEN![/bold red]")
        return
    users[username]={
        "email":email,
        "password":password,
        "followers":[],
        "following":[],
        "posts":[]
    }
    save_users(users)
    print("[bold green]SIGN UP HAS BEEN SUCCESFUL, YOU CAN LOG IN NOW![/bold green]")
def login() -> str | None:
    print(Panel("[bold cyan]Login[/bold cyan]"))
    users=load_users()
    username=Prompt.ask("Please enter you [green]username[/green]").strip()
    password=Prompt.ask("Please enter you [green]password[/green]", password=True).strip()
    if username not in users:
        print("[bold red]USERNAME NOT FOUND![bold red]")
        return None
    if users[username]["password"]!=password:
        print("[bold red]PASSWORD IS INCORRECT![/bold red]")
        return None
    print(f"[bold green] Welcome back, {username}![/bold green]")
    return username
def load_posts():
    try:
        with open('posts.json', "r") as f:
            posts=json.load(f)
        return posts
    except FileNotFoundError:
        return []
def save_posts(posts):
    with open("posts.json", 'w') as f:
        json.dump(posts, f, indent=4)
def display_posts(post):
    table=Table(show_header=True, header_style="bold magenta")
    table.add_column("User", style="dim")
    table.add_column("Saves")
    table.add_column("Comments")
    table.add_column("Likes")
    table.add_column("Caption")
    table.add_row(post['user'], post['caption'], str(post['likes']), str(len(post['comments'])), str(post['saves']))
    console.print(table)
    for comment in post['comments']:
        console.print(f"[{comment['user']}], {comment['text']}")
def like_posts(post):
    post['likes']+=1
    save_posts(post)
def comment_on_post(post):
    comment_text=input()
    comment={
        'user': 'current_user',
        'text': comment_text
    }
    post['comments'].append(comment)
    save_posts(post)
def post_new_content():
    caption=input()
    new_post={
        "user":"current_user",
        "caption": caption,
        "likes": 0,
        "commnets": [],
        "saves": 0
    }
    posts=load_posts()
    posts.append(new_post)
    save_posts(posts)
    print("YOUR POST HAS BEEN SUCCESSFULLY PUBLISHED!!")
def show_home_feed():
    posts=load_posts()
    followed_users=['user1','user2']
    for post in posts:
        if post['user'] in followed_users:
            display_posts(post)
            print("Choose an action: (1) Like, (2) Comment, (3) Save, (4) Post New Content, (5) Skip, (6) Next Post: ")
            while True:
                action=input()
                if action == "1":
                    like_posts(post)
                elif action == "2":
                    comment_on_post(post)
                elif action == "3":
                    save_posts(post)
                elif action == "4":
                    post_new_content()
                elif action == "5":
                    break
                elif action== "6":
                    continue
                else:
                    print("Invalid action.Please try again.")


    
sample_posts = [
    {
        "user": "user1",
        "caption": "Beautiful day at the beach!",
        "likes": 10,
        "comments": [{"user": "user2", "text": "Looks amazing!"}],
        "saves": 5
    },
    {
        "user": "user2",
        "caption": "Had a great time at the park!",
        "likes": 8,
        "comments": [{"user": "user1", "text": "Wish I was there!"}],
        "saves": 3
    }
]
if not load_posts():
    save_posts(sample_posts)
#show_home_feed()
def load_stories():
    try:
        with open('stories.json', 'r') as f:
            stories=json.load(f)
            return stories
    except FileNotFoundError:
        return []
def post_story():
    story_content=input()
    new_story={
        'user': 'current_user',
        'content': story_content,
        'likes': 0,
        'comments': []
    }
    stories=load_stories()
    stories.append(new_story)
    save_stories(stories)
def save_stories(stories):
    with open('stories.json', 'w') as f:
        json.dump(stories, f, indent=4)
def like_story(story):
    story['likes']+=1
    save_stories(load_stories())
def comment_on_story(story):
    comment_text=input()
    comment={
        'user': 'current_user',
        'text': comment_text
    }   
    story['comments'].append(comment)
    save_stories(load_stories())
def show_stories():
    stories=load_stories()
    followed_users=['user1', 'user2']
    for story in stories:
        if story['user'] in followed_users:
            print(f"{story['user']} has just shared a story! Here it is: {story['content']}")
            print("Choose an action: (1) Like, (2) Comment, (3) Post New Story, (4) Skip: ")
            action=input()
            if action == "1":
                like_story(story)
            elif action == "2":
                comment_on_story(story)
            elif action == "3":
                post_story()
            elif action== "4":
                continue
            else:
                print("Invalid action.")
def load_messages():
    try:
        with open('messages.json', 'r') as f:
            messages=json.load(f)
            return messages
    except FileNotFoundError:
        return []
def save_messages(messages):
    with open('messages.json', 'w') as f:
        json.dump(messages, f, indent=4)                           
def send_message():
    print("Enter the username of the receiver: ")
    receiver=input()
    print("Enter your message: ")
    message_text=input()
    message={
        "sender": 'current_user',
        "receiver": receiver,
        "message": message_text    
    }
    messages=load_messages()
    messages.append(message)
    save_messages(messages)
def show_messages():
    messages=load_messages()
    for message in messages:
        if message['receiver']=='current_user':
            print(f"You've got a new message from {message['sender']}: {message['message']}")
def load_groups():
    with open('groups.json', 'r') as f:
        try: 
            groups=json.load(f)
            return groups
        except FileNotFoundError:
            return []
def save_groups(groups):
    with open('groups.json', 'w') as f:
        json.dump(groups, f, indent=4)    
def create_group():
    print("PLease enter the name of you group: ")
    group_name=input()
    members=["current_user"]
    print("Enter the usernames of users to add to the group (type 'done' to finish): ") 
    while True:
        member=input()
        if member=="done":
            break
        elif member not in members:
            members.append(member)
        else:
            print(f"{member} has alredy been added.")
    new_group={
        "group_name": group_name,
        "members": members,
        "messages": []
    }  
    groups=load_groups()          
    groups.append(new_group)
    save_groups(groups)
    print(f"New group has been created under the name of {group_name} and the members are: { ' ,'.join(members)}.")

def send_group_messages():
    print("Enter the group name to send a message to: ")
    group_name=input()
    groups=load_groups()
    group=next((g for g in groups if g['group_name']==group_name), None)
    if not group:
        print(f"There doesn't exist any group under the name of {group_name}.")
        return
    if 'current_user' not in group['members']:
        print(f"You are not a member of the group you asked for.")
        return
    print("Enter your message: ")
    message_text=input()
    message={
        'sender':'current_user',
        'message':message_text
    }
    group['messages'].append(message)
    save_groups(groups)
    print("Your message has been sent to the group.")
def show_messages():
    print('Enter the group name to view messages: ')
    group_name=input()
    groups=load_groups()
    group=next((g for g in groups if g==group_name), None)
    if not group:
        print(f"There is no such group under the name of {group_name}.")
        return
    if 'current_user' not in group['members']:
        print("Apologies. You are not a member of this group.")
        return
    for message in group['messages']:
        print(f"{message['sender']}: {message['message']}")
def load_users():
    try:
        with open('users.json', 'r')as f:
            users=json.load(f)
            return users
    except FileNotFoundError:
        return []
def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)
sample_user=[
    {
        "username": "user1",
        "email": "user1@example.com",
        "password": "hashed_password1",
        "followers": ["user2", "user3"],
        "follow_requests": ["user4"],
        "posts": [
            {
                "caption": "This is a sample post",
                "likes": 10,
                "comments": ["Nice post!", "Great!"]
            }
        ]
    }
]
if not load_users:
    save_users(sample_user)
def send_follow_requests():
    print("Enter the username to send follow request: ")
    user_to_follow=input()
    if user_to_follow=='current_user':
        print("HOW SELFISH! I'm awfully sorry, but you cannot follow yourself.")
        return
    users=load_users() 
    user=next((u for u in users if u['username']==user_to_follow), None)
    if not user:
        print("User {user_to_follow} was not found.")
        return
    if 'follow_requests' not in user:
        user['follow_requests']=[]
    if 'current_user' in user['follow_requests']:
        print("YOU've already sent them a follow request.")
        return
    user['follow_requests'].append('current_user')
    save_users(users)
    print(f"Don't you worry now because we have sent {user_to_follow} your follow request.")
def view_follow_requests():
    users=load_users()
    user=next((u for u in users if u['username']=='current_user'), None)
    if not user or 'follow_requests' not in user:
        print("You have no follow requests!")
        return
    print("Follow requests:")
    for requester in user['follow_requests']:
        print("-", requester)
def manage_follow_requests():
    users=load_users()
    user=next((u for u in users if u['username']=='current_user'), None)
    if not user not in users or 'follow_requests' not in user:
        print("You have no follow requests.")
        return
    print('Follow requests are:d ')
    for index, requester in enumerate(user['follow_requests']):
        print(f"{index+1}-{requester}")
        print("Enter the number of the user to approve, or type 'reject' to reject a request: ")
        choice=input()
        if choice.lower()== 'reject':
            user['follow_requests']=[]
            print("Based on your choice, all the requests have been rejected.")
        elif choice.isdigit() and 1<=int(choice)<=len(user['followed_requests']):
            requester=user['follow_requests'][int(choice)-1]
            user['follow_requests'].remove(requester)
            if 'followers' not in user:
                user['followers']=[]
            user['followers'].append(requester)
            print(f"User {requester} has been approved added to your followers.")
        else:
            print("Invalid choice. Please make another attempt.")
    save_users(users)
def follow_or_unfollow(target_user):
    users=load_users()
    if target_user in users['current_user'].get("following", []):
        users['current_user']["following"].remove(target_user)
        users[target_user]["followers"].remove('current_user')
        console.print(f"[yellow] You no longer follow {target_user}. [/yellow]")
    else:
        if users[target_user].get("private_account", False):
            if 'current_user' not in users[target_user].get("follow_requests", []):
                users[target_user].setdefault("follow_requests", []).append('current_user')
                console.print(f"[cyan] Your request has been sent to {target_user}. [/cyan]")
            else:
                console.print(f"[yellow] You have already sent a request. [/yellow]")
        else:
            users['current_user'].setdefault("following", []).append(target_user)
            users[target_user].setdefault("followers", []).append('current_user')
            console.print(f"[green] You have started following {target_user} [/green]")
def block_or_unblock(users, current_user, target_user):
    users=load_users()
    if target_user in users[current_user].get("blocked_users", []):
        users[current_user]["blocked_users"].remove(target_user)
        console.print(f"[green]{target_user} unblocked. [/green]")
    else:
        users['current_user'].setdefault("blocked_users", []).append(target_user)
        console.print(f"[red] {target_user} blocked. [/red]")

def search_user(logged_in_user):
    users=load_users()
    username = Prompt.ask("Who do you want to search for?")
    if username in users:
        show_user_profile(logged_in_user, username)
    else:
        return
def show_user_profile(logged_in_user, target_username):
    users = load_users()
    target_user = users.get(target_username)
    if not target_user:
        console.print(f"[red]No such user was found.[/red]")
        return
    if logged_in_user in target_user.get("blocked_users", []) or target_username in users[logged_in_user].get("blocked_users", []):
        console.print("[red]You cant access this profile.[/red]")
        return
    bio = target_user.get("bio", None)
    followers = len(target_user.get("followers", []))
    following = len(target_user.get("following", []))
    posts = len(target_user.get("posts", []))
    console.print(Panel.fit(f"""
    [bold]{target_username}[/bold]
    Bio: {bio}
    Followers: {followers} | Following: {following}
    Posts: {posts}
    """, title="User Profile"))
    console.print("\n[1] follow/unfollow")
    console.print("[2] block/unblock")
    console.print("[0] return")
    choice = Prompt.ask("Choose please:", choices=["0", "1", "2"])
    if choice == "1":
        follow_or_unfollow(users, logged_in_user, target_username)
    elif choice == "2":
        block_or_unblock(users, logged_in_user, target_username)

    save_users(users)


if __name__ == "__main__":
    main()