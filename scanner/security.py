from bandit.core.manager import BanditManager
from bandit.core.config import BanditConfig

def scan_code_for_security(filepath):
    config = BanditConfig()
    manager = BanditManager(config, 'file')
    manager.discover_files([filepath])
    manager.run_tests()
    return manager.results
