from rich.console import Console
from rich.panel import Panel
import requests
import re
import os

console = Console()

def show_banner():
    skull_banner = """
██████╗ ██╗ ██╗ █████╗ ███╗ ██╗██████╗ █████╗ ██████╗ █████╗
██╔══██╗██║ ██║██╔══██╗████╗ ██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║███████║██╔██╗ ██║██║ ██║███████║██████╔╝███████║
██╔══██╗██╔══██║██╔══██║██║╚██╗██║██║ ██║██╔══██║██╔══██╗██╔══██║
██████╔╝██║ ██║██║ ██║██║ ╚████║██████╔╝██║ ██║██║ ██║██║ ██║
╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═══╝╚═════╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚═╝ ╚═╝
    """
    console.print(Panel(skull_banner, title="[bold green]BHANDARA CYBER SQUAD[/bold green]", subtitle="[cyan]Created by Pranay | Pranav Leak Hunter[/cyan]", border_style="green"))
    console.print("[bold cyan]💀 CYBORG OSINT - SKULL x MATRIX Edition 💀[/bold cyan]\n")
    console.print("[dim]Repo: https://github.com/Pranay7030/Pranay-cyborg-osint[/dim]\n")

def link_osint():
    console.print("\n[bold yellow][*] LINK OSINT[/bold yellow]")
    link = input("Link daal: ")
    console.print(f"[green]Scanning {link}...[/green]")
    try:
        r = requests.get(link, timeout=5)
        console.print(f"[green]✓ Status Code: {r.status_code}[/green]")
        console.print(f"[cyan]✓ Server: {r.headers.get('Server', 'Unknown')}[/cyan]")
    except:
        console.print("[red]Link dead ya galat hai![/red]")

def insta_osint():
    console.print("\n[bold magenta][*] INSTA PUBLIC CHECK[/bold magenta]")
    username = input("Insta username daal: ").strip()
    console.print(f"[yellow]Checking @{username}...[/yellow]")
    console.print(f"[cyan]Profile Link: https://instagram.com/{username}[/cyan]")
    console.print("[green]✓ Public info extracted (demo - private data nahi)[/green]")

def email_leak_checker():
    console.print("\n[bold cyan][*] EMAIL LEAK CHECKER[/bold cyan]")
    email = input("Email daal: ").strip()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        console.print("[red]Invalid email format![/red]")
        return
    console.print(f"[yellow]Checking {email}...[/yellow]")
    console.print(f"[green]✓ Valid Format: {email}[/green]")
    domain = email.split('@')[1]
    console.print(f"[cyan]Domain: {domain}[/cyan]")
    console.print(f"\n[bold]👉 Real Leak Check (HIBP): https://haveibeenpwned.com/account/{email}[/bold]")
    console.print("[dim]For Educational Purpose Only![/dim]")

# === MAIN ===
try:
    os.system('clear' if os.name == 'posix' else 'cls')
except:
    pass

show_banner()

while True:
    console.print("\n[bold white][1] Link OSINT | [2] Insta OSINT | [3] Email Leak Checker | [4] Exit[/bold white]")
    choice = input("\nChoice daal (1-4): ")

    if choice == "1":
        link_osint()
    elif choice == "2":
        insta_osint()
    elif choice == "3":
        email_leak_checker()
    elif choice == "4":
        console.print("[bold red]Exiting... Bhandara Cyber Squad OP! 🔥[/bold red]")
        break
    else:
        console.print("[red]Galat choice! 1-4 me se daal[/red]")
