"""
main.py — Entry point for the Enterprise AI Analytics Platform.

Usage:
    python main.py                    # Run all 3 demo queries
    python main.py --query "your Q"   # Run a custom query
    python main.py --no-rag           # Disable RAG (faster, no HuggingFace download)
"""
import argparse
import time
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text
from agents.supervisor import SupervisorAgent

console = Console()

DEMO_QUERIES = [
    "Which customers have the highest churn risk this quarter and what is the revenue at stake?",
    "Detect anomalies in our transactions and summarize the findings per our fraud policy.",
    "Forecast revenue for the next 3 months and tell me the ROI of running a retention campaign.",
]


def run_query(supervisor: SupervisorAgent, query: str, idx: int):
    console.print(Rule(f"[bold cyan]Query {idx}[/bold cyan]"))
    console.print(Panel(f"[bold white]{query}[/bold white]", title="🧠 User Query", border_style="cyan"))

    start = time.time()
    result = supervisor.run(query)
    elapsed = time.time() - start

    console.print(Panel(result, title="💡 Platform Insight", border_style="green"))
    console.print(f"[dim]⏱ Completed in {elapsed:.1f}s[/dim]\n")


def main():
    parser = argparse.ArgumentParser(description="Enterprise AI Analytics Platform")
    parser.add_argument("--query", type=str, help="Custom query to run")
    parser.add_argument("--no-rag", action="store_true", help="Disable RAG (skip HuggingFace)")
    args = parser.parse_args()

    console.print(Panel.fit(
        "[bold cyan]Enterprise AI Analytics Platform[/bold cyan]\n"
        "[dim]Supervisor · Data · Analysis · ML · RAG · Insight · ROI[/dim]",
        border_style="cyan",
    ))

    use_rag = not args.no_rag
    if not use_rag:
        console.print("[yellow]RAG disabled (--no-rag flag set)[/yellow]\n")

    supervisor = SupervisorAgent(use_rag=use_rag)
    console.print("[green]✓ All agents ready.[/green]\n")

    if args.query:
        run_query(supervisor, args.query, 1)
    else:
        console.print(f"[dim]Running {len(DEMO_QUERIES)} demo queries...[/dim]\n")
        for i, q in enumerate(DEMO_QUERIES, 1):
            run_query(supervisor, q, i)
            if i < len(DEMO_QUERIES):
                time.sleep(1)

    console.print(Rule("[bold green]Done[/bold green]"))


if __name__ == "__main__":
    main()
