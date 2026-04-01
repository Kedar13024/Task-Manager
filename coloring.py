from rich import print
from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from tqdm import tqdm
from rich.columns import Columns
from time import sleep
console=Console(record=True)
def processing():
    for steps in tqdm(range(5),desc="Processing..."):
        sleep(0.3)
def loading():
    with console.status("[bold green]⬇️ Loading tasks...[/bold green]"):
        sleep(2)

def updating():
    with console.status("[bold green] Updating file...[/bold green]"):
        sleep(2)
    console.log("💾 Task list updated successfully!")

def deleting():
    for steps in tqdm(range(5),desc="Deleting..."):
        sleep(0.5)

def banner(msg):
    console.print(Panel(msg,border_style="red",style="black on white",box=box.HEAVY_EDGE,width=50,height=5),justify="center")

def user(userinput:str):
    console.print(Panel(userinput,border_style="blue",title="YOU",title_align="center",box=box.ROUNDED,expand=False,padding=(0,2)),justify="right")

def bot(botreply):
    with console.status("[bold green]Analysing...[/bold green]"):
        sleep(1)
    console.print(Panel(f"[bold green]{botreply}[/bold green]",title="🤖",title_align="left",border_style="green",box=box.ROUNDED,expand=False,padding=(0,2)))





if __name__=="__main__":
    banner("hello")
    