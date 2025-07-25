# YouTube Video Downloader

A simple Python script that downloads YouTube videos in high quality using yt-dlp. Supports 720p and 1080p resolutions with automatic audio merging.

## 🚀 Features

- **High-Quality Downloads**: Support for 720p and 1080p video resolution
- **Audio Integration**: Automatically merges best available audio with video
- **Smart Filename Handling**: Sanitizes video titles for safe file naming
- **Command-Line Interface**: Easy-to-use command-line arguments
- **Fallback Options**: Uses best available quality if specified resolution isn't available

## 📋 Prerequisites

Before using this script, you need to install the following:

### 1. Python Dependencies
```bash
pip install yt-dlp
```

### 2. FFmpeg (REQUIRED)
**⚠️ Important**: You must have `ffmpeg.exe` in the same folder as the Python script for video and audio merging to work properly.

#### Download FFmpeg:
1. Go to [FFmpeg Official Website](https://ffmpeg.org/download.html)
2. Download the appropriate version for your operating system
3. Extract the downloaded archive
4. Copy `ffmpeg.exe` to the same directory as `youtube_downloader.py`

#### Folder Structure:
```
your-project-folder/
├── youtube_downloader.py
├── ffmpeg.exe          # <- This file is REQUIRED
└── downloaded_videos/   # (created automatically)
```

## 🛠️ Installation

1. **Clone or download** the script file
2. **Install yt-dlp**:
   ```bash
   pip install yt-dlp
   ```
3. **Download FFmpeg** and place `ffmpeg.exe` in the same folder as the script
4. **Verify installation**:
   ```bash
   python youtube_downloader.py --help
   ```

## 📖 Usage

### Basic Usage
```bash
python youtube_downloader.py --url "https://www.youtube.com/watch?v=VIDEO_ID" --res 1080p
```

### Command-Line Arguments

| Argument | Description | Options | Default |
|----------|-------------|---------|---------|
| `--url` | YouTube video URL | Any valid YouTube URL | Demo video URL |
| `--res` | Video resolution | `720p`, `1080p` | `1080p` |

### Examples

#### Download in 1080p (default):
```bash
python youtube_downloader.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

#### Download in 720p:
```bash
python youtube_downloader.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --res 720p
```

#### Run with default demo video:
```bash
python youtube_downloader.py
```

## 🔧 How It Works

### Script Workflow

1. **Input Processing**:
   - Accepts YouTube URL and resolution parameters
   - Uses default values if arguments not provided

2. **Filename Sanitization**:
   - Removes invalid characters from video titles
   - Ensures safe file naming across different operating systems
   ```python
   # Characters removed: \ / * ? : " < > |
   sanitized_title = re.sub(r'[\\/*?:"<>|]', "", title)
   ```

3. **Quality Selection**:
   - Prioritizes best video at specified resolution + best audio
   - Falls back to best available quality if exact resolution unavailable
   ```
   Format: bestvideo[height=1080]+bestaudio/best[height=1080]
   ```

4. **Download Process**:
   - Uses yt-dlp to fetch video and audio streams
   - FFmpeg merges video and audio into final file
   - Saves with format: `{VideoTitle}_{Resolution}.{Extension}`

### Output File Format
Downloaded files are named as:
```
VideoTitle_1080p.mp4
VideoTitle_720p.mp4
```

## ⚙️ Configuration

### Supported Resolutions
- **720p**: 1280x720 HD resolution
- **1080p**: 1920x1080 Full HD resolution

### File Format
- **Video**: MP4 (default)
- **Audio**: Best available audio quality automatically merged

### Custom Output Template
The script uses this naming template:
```python
output_template = "%(title)s_" + resolution + ".%(ext)s"
```

You can modify this in the code to change the naming convention.

## 🔍 Troubleshooting

### Common Issues

#### 1. FFmpeg Not Found Error
```
ERROR: ffmpeg not found. Please install or provide the path using --ffmpeg-location
```
**Solution**: 
- Download `ffmpeg.exe` from the official website
- Place it in the same folder as `youtube_downloader.py`
- Ensure the filename is exactly `ffmpeg.exe`

#### 2. yt-dlp Not Installed
```
ModuleNotFoundError: No module named 'yt_dlp'
```
**Solution**:
```bash
pip install yt-dlp
```

#### 3. Video Unavailable
```
ERROR: Video unavailable
```
**Solution**:
- Check if the YouTube URL is correct and accessible
- Verify the video is not private or region-restricted
- Try a different video URL

#### 4. Resolution Not Available
The script will automatically fall back to the best available quality if the specified resolution isn't available.

#### 5. Permission Errors
**Solution**:
- Run the script from a directory where you have write permissions
- On some systems, you might need to run as administrator

### Debug Mode
To see detailed output, you can modify the script to add verbose logging:
```bash
# Add -v flag to the yt-dlp command for verbose output
```

## 🛡️ Legal Considerations

- **Respect Copyright**: Only download videos you have permission to download
- **YouTube Terms of Service**: Ensure your usage complies with YouTube's ToS
- **Personal Use**: This tool is intended for personal, educational, or fair use purposes
- **Content Creator Rights**: Consider supporting content creators through official channels


## ⚠️ Disclaimer

This tool is for educational and personal use only. Users are responsible for complying with YouTube's Terms of Service and applicable copyright laws. The developers are not responsible for any misuse of this software.

---
