from rich.console import Console
from rich.table import Table
from rich.progress import track
import time

def main():
    """
    main関数
    """
    console = Console()
    createTable(console)
    createProgress()

def createTable(console):
    # テーブルの紹介
    table = Table(show_header=True, header_style="bold magenta", title="ToDos")
    table.add_column("Date", style="dim", width=12)
    table.add_column("Title")
    table.add_column("Tags", justify="right")
    table.add_row("2021-08-01", "Finish rich tutorial", "python,rich")
    table.add_row("2021-08-02", "Write article", "python,rich")

    console.print(table)

def createProgress():
    for n in track(range(100), description="Processing..."):
        time.sleep(0.05)

if __name__ == "__main__":
    main()
    input() #待ち状態にする
