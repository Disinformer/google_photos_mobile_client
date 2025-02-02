import argparse
import os
import time

from .api_methods import DEFAULT_TIMEOUT
from .client import Client


def main():
    parser = argparse.ArgumentParser(description="Google Photos mobile client.")
    parser.add_argument("--path", type=str, help="Path to the file or directory to upload.")
    parser.add_argument("--auth_data", type=str, help="Google auth data for authentication. If not provided, `GP_AUTH_DATA` env variable will be used.")
    parser.add_argument("--progress", action="store_true", help="Display upload progress.")
    parser.add_argument("--recursive", action="store_true", help="Scan the directory recursively.")
    parser.add_argument("--threads", type=int, default=1, help="Number of threads to run uploads with. Defaults to 1.")
    parser.add_argument("--force-upload", action="store_true", help="Upload files regardless of their presence in Google Photos (determined by hash).")
    parser.add_argument("--delete-from-host", action="store_true", help="Delete uploaded files from source path.")
    parser.add_argument("--timeout", type=int, default=30, help=f"Requests timeout, seconds. Defaults to {DEFAULT_TIMEOUT}.")
    parser.add_argument("--attempt-timeout", type=int, default=30, help=f"Timeout between processing attempts when run in loop. Defaults to {DEFAULT_TIMEOUT}.")
    parser.add_argument("--run-in-loop", action="store_true", help="Utility will run infinitely. You may stop it by 'cntrl+c'")
    parser.add_argument("--log-level", type=str, default="INFO", choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], help="Set the logging level (default: INFO)")

    args = parser.parse_args()
    attempt_timeout = int(os.getenv("ATTEMPT_TIMEOUT") or args.attempt_timeout or DEFAULT_TIMEOUT)

    while True:
        client = Client(auth_data=args.auth_data, timeout=args.timeout, log_level=args.log_level)
        output = client.upload(target=args.path, show_progress=args.progress, recursive=args.recursive, threads=args.threads, force_upload=args.force_upload, delete_from_host=args.delete_from_host)
        print(output)
        print(f"All files processed. Next processing will start in {attempt_timeout} seconds.", flush=True)
        if not args.run_in_loop:
            break
        time.sleep(attempt_timeout)
