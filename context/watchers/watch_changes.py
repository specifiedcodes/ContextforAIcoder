import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from update_embeddings import embed_files

TARGET_EXTENSIONS = [".js", ".ts", ".jsx", ".md", ".json", ".cs"]

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if any(event.src_path.endswith(ext) for ext in TARGET_EXTENSIONS):
            print(f"{event.src_path} changed, re-embedding...")
            embed_files([event.src_path])

if __name__ == "__main__":
    path_to_watch = "."  # Or pass as arg
    observer = Observer()
    observer.schedule(ChangeHandler(), path=path_to_watch, recursive=True)
    observer.start()
    print(f"Watching {path_to_watch} for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
