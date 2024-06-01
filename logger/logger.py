class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Logger:
    def __init__(self, log_file, is_debug_mode=False):
        self.log_file = log_file
        self.is_debug_mode = is_debug_mode

    def log_header(self, message):
        if self.is_debug_mode:
            print(f"{Bcolors.HEADER} {message} {Bcolors.ENDC}")
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

    def log_warning(self, message):
        if self.is_debug_mode:
            print(f"{Bcolors.WARNING} {message} {Bcolors.ENDC}")
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

    def log_ok(self, message):
        if self.is_debug_mode:
            print(f"{Bcolors.OKBLUE} {message} {Bcolors.ENDC}")
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')


if __name__ == "__main__":
    logger = Logger("./log.txt", is_debug_mode=False)
    logger.log_warning("Hello World")
    logger.log_ok("Hello World")
    logger.log_header("Hello World")
