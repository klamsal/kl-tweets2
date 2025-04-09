import pandas as pd

tweets = pd.read_csv('https://raw.githubusercontent.com/klamsal/kl-tweets2/refs/heads/main/Tweets.csv')

import plotly.express as px

sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']

fig = px.pie(sentiment_counts,
             values = 'count',
             names = 'sentiment',
             title = "Count of tweets by Sentiment"
             )
fig.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Calculate tweets counts by airlines
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

# Create a bargraph using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='airline', y='count', hue = 'airline',palette = 'pastel', legend = False, data=airline_counts)

# Add titles and labels
plt.title('Tweet counts by Airlines')
plt.xlabel('Airline')
plt.ylabel('Count')


plt.tight_layout()
plt.show()
