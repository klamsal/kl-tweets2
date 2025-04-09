import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tweets = pd.read_csv('https://raw.githubusercontent.com/klamsal/kl-tweets2/refs/heads/main/Tweets.csv')

# Streamlit App title
st.title("Airline Tweets Sentiment Analysis")

# Pie chart for sentiment counts
st.header("Count of Tweets by Sentiment")
sentiment_counts = tweets['airline_sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']

fig_pie = px.pie(sentiment_counts, values='count', names='sentiment', title="Count of tweets by Sentiment")
st.plotly_chart(fig_pie)

# Bar graph for airline counts
st.header("Tweet Counts by Airlines")
airline_counts = tweets['airline'].value_counts().reset_index()
airline_counts.columns = ['airline', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(x='airline', y='count', palette='pastel', data=airline_counts)
plt.title('Tweet Counts by Airlines')
plt.xlabel('Airline')
plt.ylabel('Count')
plt.tight_layout()

st.pyplot(plt)
