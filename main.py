from rich.console import Console
from rich.panel import Panel
import requests
import zipfile
import re
import os

console = Console()

def show_banner():
    console.clear()
    console.print(Panel.fit(
        "[bold red] ____  _   _    ____ _  __ ____  _   _[/bold red]\n"
        "[bold yellow]| __ )| | | |  / \  / ___| |/ // ___|| | | |[/bold yellow]\n"
        "[bold green]|  _ \| |_| | / _ \ | |   | ' / \___ \| |_| |[/bold green]\n"
        "[bold cyan]| |_) |  _  |/ ___ \| |___| . \  ___) |  _  |[/bold cyan]\n"
        "[bold blue]|____/|_| |_/_/   \_\____|_|\_\|____/|_| |_|[/bold blue]\n\n"
        "[bold white on red]   BHANDARA CYBER SQUAD - V10 FINAL OP!   [/bold white on red]",
        border_style="bold red",
        title="[bold yellow]🔥 BHACKSH TOOLKIT 🔥[/bold yellow]"
    ))
    console.print(Panel(
        "[bold magenta]👑 Made With 💀 By: [bold white on magenta] PRANAY (BHACKSH) [/bold white on magenta][/bold magenta]\n"
        "[bold cyan]📍 Location: Bhandara, Maharashtra | Team: Bhandara Cyber Squad OP![/bold cyan]\n\n"
        "[bold yellow]⚠️  DISCLAIMER:[/bold yellow] [bold white]This tool is for [bold red]EDUCATIONAL PURPOSE ONLY![/bold red][/bold white]\n"
        "[dim white]We are not responsible for any misuse or illegal activity.[/dim white]",
        border_style="bold magenta",
        title="[bold green]✨ INFO ✨[/bold green]",
        padding=(1, 2)
    ))

def link_osint():
    console.print("[bold yellow][*] LINK OSINT[/bold yellow]")
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
       show_banner()

    while True:
        console.print("\n[bold white][1] Link OSINT | [2] Insta OSINT | [3] Email Leak Checker | [4] BHACKSH APK Scanner V2 | [5] Exit[/bold white]")
        choice = input("\nChoice daal (1-5): ")

        if choice == "1":
            link_osint()
        elif choice == "2":
            insta_osint()
        elif choice == "3":
            email_leak_checker()
        elif choice == "4":
            apk_scanner_module()
        elif choice == "5":
            console.print("[bold red]Exiting... Bhandara Cyber Squad OP! 👑[/bold red]")
            break
        else:
            console.print("[bold red]Galat choice! 1-5 me se daal[/bold red]")
