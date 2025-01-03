import sys

def parse_arguments():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        sys.exit(1)
    return sys.argv[1], sys.argv[2:]
