import asyncio
import random
import time

from rich.progress import Progress, TaskID
from rich.prompt import Confirm, IntPrompt


async def do_work_async(
    count: int, progress: Progress, task: TaskID, multiplier: float = 1.0
) -> None:
    """
    Coordinates work using an asynchronous worker.
    :param count: The number of individual work items to schedule.
    :param progress: The Rich progress bar instance to maintain.
    :param task: The Rich progress bar task to maintain.
    :param multiplier: An optional dampness factor to the sleep call.
    :return:
    """

    async def process_item_async(item: int):
        await asyncio.sleep(random.random() * multiplier)
        progress.update(task, advance=1)

    tasks = [asyncio.create_task(process_item_async(item)) for item in range(count)]
    await asyncio.gather(*tasks)


def do_work(
    count: int, progress: Progress, task: TaskID, multiplier: float = 1.0
) -> None:
    """
    Coordinates work using a synchronous worker.
    :param count: The number of individual work items to schedule.
    :param progress: The Rich progress bar instance to maintain.
    :param task: The Rich progress bar task to maintain.
    :param multiplier: An optional dampness factor to the sleep call.
    :return:
    """

    def process_item(item: int):
        time.sleep(random.random() * multiplier)
        progress.update(task, advance=1)

    [process_item(item) for item in range(count)]


async def main_async(tasks: int) -> None:
    """
    The hip and fast asynchronous version.
    :param tasks: The number of work items that each of the 3 workers will run.
    :return:
    """
    with Progress() as progress:
        task1 = progress.add_task("[red]Worker #1...", total=tasks)
        task2 = progress.add_task("[green]Worker #2...", total=tasks)
        task3 = progress.add_task("[cyan]Worker #3...", total=tasks)

        tasks = [
            asyncio.create_task(do_work_async(tasks, progress, task1, multiplier=10.0)),
            asyncio.create_task(do_work_async(tasks, progress, task2, multiplier=5.0)),
            asyncio.create_task(do_work_async(tasks, progress, task3, multiplier=1.0)),
        ]
        await asyncio.gather(*tasks)


def main(tasks: int) -> None:
    """
    Boring and slow synchronous version.
    :param tasks: The number of work items that each of the 3 workers will run.
    :return:
    """
    with Progress() as progress:
        task1 = progress.add_task("[red]Worker #1...", total=tasks)
        task2 = progress.add_task("[green]Worker #2...", total=tasks)
        task3 = progress.add_task("[cyan]Worker #3...", total=tasks)
        do_work(tasks, progress, task1, multiplier=10.0)
        do_work(tasks, progress, task2, multiplier=5.0)
        do_work(tasks, progress, task3, multiplier=1.0)


if __name__ == "__main__":
    """
    Visually demonstrates the power of asyncio as a TUI.
    """
    tasks = IntPrompt.ask("How many tasks per worker would you like?")
    asyncio.run(main_async(tasks)) if Confirm.ask("Run the async version?") else main(
        tasks
    )
