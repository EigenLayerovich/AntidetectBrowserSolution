import asyncio
import logging
from aioconsole import ainput

from profile_manager.manager import ProfileManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


async def run_profile_manager():
    manager = ProfileManager()

    async def handle_create_profile():
        name = await ainput('Profile name: ')
        proxy_str: str = await ainput(
            'Proxy (protocol:host:port:user:pass) or leave empty ('
            'protocol is http or socks5; Socks5 does not supports user auth!): ',
        )
        try:
            created_name = await manager.create_profile(name, proxy_str)
            print(f'Profile "{created_name}" created!')
        except Exception as e:
            logger.exception(f'Error creating profile: {e}')

    async def handle_launch_profile():
        if not manager.profiles:
            print('No profiles available')
            return

        print('\nAvailable profiles:')
        for name in manager.get_profile_names():
            status = manager.get_profile_status(name)
            print(f' - {name} ({status})')

        profile_name = await ainput('Enter profile name: ')
        try:
            await manager.launch_profile(profile_name)
            print(f'Profile "{profile_name}" launched!')
        except Exception as e:
            logger.exception(f'Error launching profile: {e}')

    async def handle_change_proxy():
        if not manager.profiles:
            print('No profiles available')
            return

        print('\nAvailable profiles:')
        for name in manager.get_profile_names():
            print(f' - {name}')

        profile_name = await ainput('Enter profile name to change proxy: ')
        new_proxy_str = await ainput(
            'New Proxy (protocol:host:port:user:pass) or empty to remove ('
            'protocol is http or socks5; Socks5 does not supports user auth!): ',
        )
        try:
            await manager.update_proxy(profile_name, new_proxy_str)
            print(f'Proxy for profile "{profile_name}" updated!')
            if manager.is_profile_running(profile_name):
                print('Note: Changes will take effect after restarting the profile')
        except Exception as e:
            logger.exception(f'Error updating proxy: {e}')

    async def input_handler():
        handlers = {
            '1': handle_create_profile,
            '2': handle_launch_profile,
            '3': handle_change_proxy
        }

        while True:
            try:
                choice = await ainput(
                    '\n1. Create Profile\n'
                    '2. Launch Profile\n'
                    '3. Change Proxy\n'
                    '4. Exit\n'
                    '> '
                )

                if choice == '4':
                    # Останавливаем все запущенные задачи
                    for task in manager.running_tasks.values():
                        task.cancel()
                    await asyncio.gather(*manager.running_tasks.values(), return_exceptions=True)
                    return

                if choice in handlers:
                    await handlers[choice]()
                else:
                    print('Invalid choice')
            except (KeyboardInterrupt, EOFError):
                print("\nExiting...")
                return

    await input_handler()
