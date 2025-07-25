# YouTube-Channel-Discovery-Automation-Video-Download-Tool


# YouTube-Channel-Discovery-Automation Workflow

A powerful n8n automation workflow that searches for YouTube channels based on keywords and automatically analyzes their performance metrics, storing the results in Google Sheets.

## 🚀 Features

- **Keyword-based Channel Search**: Find relevant YouTube channels using search terms
- **Comprehensive Metrics Analysis**: 
  - Total views and subscriber count
  - Video count and upload frequency
  - Average views on last 5 videos
  - Engagement rate (likes + comments / views)
- **Smart Filtering**: Only analyzes active channels (uploaded within 30 days) with 1000+ subscribers
- **Automated Data Export**: Results automatically saved to Google Sheets
- **Chat Interface**: Easy-to-use chat trigger for initiating searches

## 📋 Prerequisites

Before setting up this workflow, ensure you have:

1. **n8n Instance**: Running n8n (cloud or self-hosted)
2. **YouTube Data API Key**: 
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Enable YouTube Data API v3
   - Create credentials (API Key)
3. **Google Sheets Access**: 
   - Google account with Sheets access
   - OAuth2 credentials configured in n8n
4. **Google Sheets Document**: Pre-created spreadsheet with appropriate columns

## 🛠️ Setup Instructions

### 1. Import the Workflow
1. Copy the JSON content from `Get Youtube channel metrics-FINAL.json`
2. In your n8n instance, go to **Workflows** → **Import from JSON**
3. Paste the JSON and import

### 2. Configure API Credentials

#### YouTube API Key
1. Replace `AIzaSyCj1HttdqyqPq1bgAivbEsh4DJWmQT9oZI` in all HTTP Request nodes with your API key
2. Nodes to update:
   - `channel stats1`
   - `Get Last 5 Videos`
   - `Each video metric`
   - `search channels`

#### Google Sheets Integration
1. Set up Google Sheets OAuth2 credentials in n8n
2. Update the Google Sheets document ID in nodes:
   - `dashboard`
   - `dashboard1`
   - `Final_Result`

### 3. Prepare Google Sheets
Create a Google Sheets document with these columns:
- Channel_Name
- Link of the channel
- Subscriber_Count
- No. of videos
- Total_Views
- Avg views on the last 5 videos
- Engagement rate(likes+comments/views)

## 🔄 How It Works

### Workflow Architecture

```
Chat Input → Keyword Processing → Channel Search → Channel Filtering → Metrics Collection → Data Export
```

### Detailed Process Flow

#### 1. **Input Stage**
- **Trigger**: Chat message received with search keyword
- **Node**: `When chat message received`
- **Output**: Keyword extracted for YouTube search

#### 2. **Channel Discovery**
- **Node**: `search channels`
- **Process**: Searches YouTube for channels matching the keyword
- **API Call**: `GET /youtube/v3/search`
- **Parameters**: 
  - `q`: Search keyword
  - `type`: channel
  - `maxResults`: 3
- **Output**: Channel IDs, titles, and links

#### 3. **Channel Processing**
- **Node**: `fetch channelTitle and Links`
- **Process**: Extracts and formats channel information
- **Node**: `Loop Over Items`
- **Process**: Iterates through each found channel

#### 4. **Channel Statistics**
- **Node**: `channel stats1`
- **Process**: Fetches detailed channel statistics
- **API Call**: `GET /youtube/v3/channels`
- **Data Retrieved**: 
  - Subscriber count
  - Total view count
  - Video count
  - Channel metadata

#### 5. **Channel Filtering**
- **Node**: `Switch`
- **Filter Criteria**: Only processes channels with 1000+ subscribers
- **Purpose**: Focus on established channels with meaningful metrics

#### 6. **Video Analysis**
- **Node**: `Get Last 5 Videos`
- **Process**: Retrieves the 5 most recent videos
- **API Call**: `GET /youtube/v3/search`
- **Parameters**: 
  - `channelId`: Target channel
  - `order`: date
  - `maxResults`: 5

#### 7. **Activity Check**
- **Node**: `get videoIDs`
- **Process**: 
  - Checks if last upload was within 30 days
  - Extracts video IDs for metrics analysis
  - Skips inactive channels

#### 8. **Video Metrics Collection**
- **Node**: `GET each videoID` → `Each video metric`
- **Process**: 
  - Splits video IDs into individual items
  - Fetches statistics for each video
- **API Call**: `GET /youtube/v3/videos`
- **Metrics**: Views, likes, comments per video

#### 9. **Analytics Calculation**
- **Node**: `Avg_view_count and engagement_rate`
- **Calculations**:
  ```javascript
  averageViews = totalViews / videoCount
  engagementRate = ((totalLikes + totalComments) / totalViews) * 100
  ```

#### 10. **Data Export**
- **Nodes**: `dashboard`, `dashboard1`, `Final_Result`
- **Process**: 
  - Combines all collected metrics
  - Exports to different sheets in Google Sheets
  - Merges channel stats with video analytics

## 📊 Output Data Structure

<img width="1324" height="326" alt="image" src="https://github.com/user-attachments/assets/82e68e38-ff14-4fd5-b9dc-911a851f8fa2" />


## 🚦 Usage

1. **Start the Workflow**: Activate the workflow in n8n
2. **Send Search Query**: Use the chat interface to send a keyword (e.g., "cooking", "tech reviews")
3. **Automatic Processing**: The workflow will:
   - Search for relevant channels
   - Filter active channels with 1000+ subscribers
   - Analyze their recent video performance
   - Calculate engagement metrics
4. **View Results**: Check your Google Sheets for the compiled analytics

## ⚙️ Configuration Options

### API Rate Limits
- YouTube API has daily quotas (10,000 units/day for free tier)
- Each channel analysis uses approximately 50-100 API units
- Monitor usage in Google Cloud Console

### Filtering Criteria
Modify these parameters in the respective nodes:

```javascript
// Subscriber threshold (Switch node)
subscriberCount > 1000

// Activity threshold (get videoIDs node)
daysSinceUpload <= 30

// Number of recent videos to analyze
maxResults: 5
```

### Search Parameters
```javascript
// Number of channels to find per search
maxResults: 3

// Search order and type
order: "relevance" // or "date", "rating", "viewCount"
type: "channel"
```

## 🔧 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify YouTube Data API v3 is enabled
   - Check API key permissions and quotas
   - Ensure API key is correctly placed in all HTTP nodes

2. **Google Sheets Connection**
   - Verify OAuth2 credentials are properly configured
   - Check sheet permissions (edit access required)
   - Ensure sheet structure matches expected columns

3. **No Results**
   - Check if channels meet filtering criteria (1000+ subs, active within 30 days)
   - Verify search keywords are relevant
   - Review API quota usage

### Debug Tips

- Enable logging in n8n to trace execution flow
- Check the "Console" output in Code nodes for debugging information
- Verify API responses in HTTP Request nodes

## 📈 Extending the Workflow

### Additional Metrics
- Video upload frequency analysis
- Competitor comparison features
- Historical data tracking
- Sentiment analysis of comments

### Integration Options
- Slack notifications for new results
- Email reports with analytics summaries
- Dashboard visualization with charts
- Database storage for historical tracking

## ⚠️ Disclaimer

- Ensure compliance with YouTube's Terms of Service
- Respect API rate limits and quotas
- Use collected data responsibly and in accordance with privacy regulations
- This tool is for analytical purposes only

---




