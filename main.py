from typing import Callable

from rich.status import Status

from classes.FileWriter import FileWriter
from classes.Scraper import Scraper
from classes.Parser import Parser
from rich.console import Console
from Config import Config
from classes.Formatters.FormatterFactory import FormatterFactory

console = Console()


def main():
    console.print("[b]Criterion Collection Scraper :movie_camera:[/b]\n")
    console.print("Output file: [i blue]" + Config.OUTPUT_FILE + "[/i blue]")
    console.print("Output format: [i blue]" + Config.OUTPUT_FORMAT + "[/i blue]\n")

    spines = doTask("Fetching Spines...", "Spines Fetched\t\t", lambda: Scraper.fetch())
    spines = doTask("Parsing Spines...", "Spines parsed\t\t", lambda: Parser.parse_response(spines))
    spines = doTask("Formatting Spines...", "Spines formatted\t",
                    lambda: FormatterFactory.getInstance().format(spines))
    doTask("Writing to file...", "File written\t\t", lambda: FileWriter.write(spines))
    console.print("\n[green]Complete[/green]")
    exit(0)


def doTask(status_msg: str, success_msg: str, task: Callable):
    status = console.status(status_msg)
    status.start()
    try:
        response = task()
    except Exception as e:
        status.stop()
        console.print("[red][b]ERROR:[/b] " + str(e) + "[/red]" + "\t[b red]:cross_mark:[/b red]")
        exit(1)
    status.stop()
    console.print("" + success_msg + "[b green]:heavy_check_mark:[/b green]")
    return response


if __name__ == "__main__":
    main()
