import asyncio

from profile_manager.cli import run_profile_manager

if __name__ == '__main__':
    try:
        asyncio.run(run_profile_manager())
    except KeyboardInterrupt:
        pass
