" Aria2 is an open-source, lightweight, and multi-protocol command-line download utility. It supports downloading files from HTTP, FTP, BitTorrent, and Metalink protocols. Aria2 is known for its high download speed, low memory usage, and ability to download files in parallel."

## Basic Installation:
```bash
sudo apt update
sudo apt install aria2
```
## Basic Usage Examples:

1. Simple HTTP Download:
```bash
aria2c https://example.com/file.zip
```

2. Download with multiple connections (faster):
```bash
aria2c -x 16 https://example.com/file.zip
```
(-x 16 means use 16 connections)

3. Download to specific directory:
```bash
aria2c -d /path/to/directory https://example.com/file.zip
```

4. Download from a text file containing URLs:
```bash
aria2c -i downloads.txt
```

5. BitTorrent download:
```bash
aria2c example.torrent
# Or using magnet link
aria2c "magnet:?xt=urn:btih:..."
```

## Common Useful Options:

1. Speed limits:
```bash
# Limit download speed to 1MB/s
aria2c --max-download-limit=1M URL

# Limit upload speed (for torrents)
aria2c --max-upload-limit=500K URL
```

2. Continue interrupted download:
```bash
aria2c -c URL
```

3. Set filename:
```bash
aria2c -o newname.zip URL
```

Setting Up Configuration File:
Create `~/.aria2/aria2.conf`:
```bash
mkdir ~/.aria2
nano ~/.aria2/aria2.conf
```

## Basic configuration example:
```conf
# Default number of connections per server
max-connection-per-server=16

# Overall download speed limit (0 means unlimited)
max-overall-download-limit=0

# Overall upload speed limit
max-overall-upload-limit=1M

# Download directory
dir=/home/username/Downloads

# Continue downloading partially downloaded files
continue=true

# Allow overwriting existing files
allow-overwrite=true

# Auto file renaming
auto-file-renaming=true

# For BitTorrent
bt-enable-lpd=true
check-integrity=true
bt-save-metadata=true
bt-max-peers=0
```

## Advanced Usage:

1. Download with authentication:
```bash
aria2c --http-user=username --http-passwd=password URL
```

2. Using aria2 with RPC (for web interfaces):
```bash
aria2c --enable-rpc --rpc-listen-all=true --rpc-allow-origin-all
```

3. Download multiple files:
```bash
aria2c -Z URL1 URL2 URL3
```

## Web Interfaces:
You can use web interfaces like:
1. webui-aria2
2. AriaNg
3. YAAW

To setup AriaNg (a popular web interface):
1. Download from GitHub
2. Host it on a local web server
3. Connect to your aria2 RPC server

## Monitoring Downloads:

1. Show progress:
```bash
# Show progress bar
aria2c --show-console-readout=true URL

# Show detailed progress
aria2c --show-files=true URL
```

2. Log downloads:
```bash
aria2c --log=download_log.txt URL
```

## Useful Tips:

1. For large files:
```bash
aria2c -x16 -s16 -k1M URL
```
- -x16: 16 connections per server
- -s16: Split file into 16 parts
- -k1M: Minimum split size 1MB

2. For torrents with better speeds:
```bash
aria2c --bt-max-peers=0 --bt-tracker-connect-timeout=10 --bt-stop-timeout=180 torrent_file
```


## Scripts :
```
#!/bin/bash

URL="http://example.com/file.txt"
OUTPUT="file.txt"

aria2c -o "$OUTPUT" "$URL"
```
