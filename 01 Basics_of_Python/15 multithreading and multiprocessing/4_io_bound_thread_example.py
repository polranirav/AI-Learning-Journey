import threading
import time

def fake_download(site):
    print(f"Downloading from {site}...")
    time.sleep(2)
    print(f"Finished downloading from {site}")

websites = ["site1.com", "site2.com", "site3.com"]

threads = [threading.Thread(target=fake_download, args=(url,)) for url in websites]

for t in threads: t.start()
for t in threads: t.join()

print("All downloads done (IO-bound).")