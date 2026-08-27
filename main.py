from rich.console import Console
from rich.panel import Panel
import requests
import zipfile
import re
import os

console = Console()

def show_banner():
    def apk_scanner_module():
    console.print("\n[bold green]📦 BHACKSH APK SCANNER V2[/bold green]")
    apk_path = input("APK ka path daal BHACKSH: ").strip().replace('"','')
    if not os.path.exists(apk_path):
        console.print("[bold red]File nahi mila! Path check kar[/bold red]")
        return
    try:
        with zipfile.ZipFile(apk_path, 'r') as apk:
            files = apk.namelist()
            console.print(f"[cyan]Total Files in APK: {len(files)}[/cyan]")
            if 'AndroidManifest.xml' in files:
                data = apk.read('AndroidManifest.xml')
                perms = re.findall(b'android\\.permission\\.[A-Z_]+', data)
                if perms:
                    console.print("[bold red]Found Permissions:[/bold red]")
                    for p in set(perms):
                        console.print(f" [yellow]{p.decode()}[/yellow]")
                else:
                    console.print("[dim]No permissions decoded (binary xml)[/dim]")
            console.print("[bold green]Scan Complete - BHACKSH V2 FINAL[/bold green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
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
