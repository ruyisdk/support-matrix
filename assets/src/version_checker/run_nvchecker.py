"""
This file let nvrunner runs in a script and return the results.

It is directily copy and modify from the nvchecker's main, which uses MIT License
"""

import argparse
import asyncio
from typing import Coroutine, Tuple

from nvchecker import core
from nvchecker.util import ResultData, RawResult, EntryWaiter


async def run(
    result_coro: Coroutine[None, None, Tuple[ResultData, bool]],
    runner_coro: Coroutine[None, None, None],
) -> Tuple[ResultData, bool]:
    """
    From original nvchecker, create a runner
    """
    result_fu = asyncio.create_task(result_coro)
    runner_fu = asyncio.create_task(runner_coro)
    await runner_fu
    result_fu.cancel()
    return await result_fu


def run_nvchecker(file: str = 'config.toml', oldvers: dict = None,
                  logging='info', logger='pretty', version=False) -> Tuple[dict, bool]:
    """
    Modified way to run nvchecker in program
    return: new_ver, has_failure
    """
    if oldvers is None:
        oldvers = {}
    args = argparse.Namespace(
        file=file,
        logging=logging,
        logger=logger,
        version=version,
    )
    if core.process_common_arguments(args):
        return

    entries, options = core.load_file(
        file, use_keymanager=False)

    task_sem = asyncio.Semaphore(options.max_concurrency)
    result_q: asyncio.Queue[RawResult] = asyncio.Queue()
    dispatcher = core.setup_httpclient(
        options.max_concurrency,
        options.httplib,
        options.http_timeout,
    )
    entry_waiter = EntryWaiter()
    futures = dispatcher.dispatch(
        entries, task_sem, result_q,
        options.keymanager, entry_waiter,
        3,
        options.source_configs,
    )

    result_coro = core.process_result(
        oldvers, result_q, entry_waiter, verbose=False)
    runner_coro = core.run_tasks(futures)

    results, has_failures = asyncio.run(run(result_coro, runner_coro))

    new_vers = dict(sorted(results.items()))
    new_vers = {
        k: core.json_encode(v) for k,v in new_vers.items() if v is not None
    }

    return (new_vers, has_failures)


if __name__ == '__main__':
    a, _ = run_nvchecker()
    print(a)
