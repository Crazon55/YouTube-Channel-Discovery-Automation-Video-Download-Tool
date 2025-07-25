import subprocess
import argparse
import sys
import re


def sanitize_filename(title):
    return re.sub(r'[\\/*?:"<>|]', "", title)


def download_video(url, resolution):
    output_template = "%(title)s_" + resolution + ".%(ext)s"
    output_template = sanitize_filename(output_template)

    cmd = [
        sys.executable,
        "-m",
        "yt_dlp",
        "-f",
        f"bestvideo[height={resolution[:-1]}]+bestaudio/best[height={resolution[:-1]}]",
        "-o",
        output_template,
        url,
    ]

    print("Running:", " ".join(cmd))
    subprocess.run(cmd)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download YouTube videos using yt-dlp."
    )
    parser.add_argument("--url", type=str, help="YouTube video URL")
    parser.add_argument("--res", type=str, choices=["720p", "1080p"], help="Resolution")

    args = parser.parse_args()

    url = args.url or "https://www.youtube.com/watch?v=nSM1m7Q8gkg"
    res = args.res or "1080p"

    download_video(url, res)
