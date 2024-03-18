# Tweet-App-Generator

Tweet-App-Generator is a Streamlit-based web application that leverages the power of GPT-3.5 to generate tweets on any topic specified by the user. Developed with the help of the GenAI Crash Course by Satvik Paramkusham ([satvik314](https://github.com/satvik314)), this application demonstrates the practical application of generative AI models in creating engaging and relevant content.

## Features

- **Custom Tweet Generation**: Generate a specified number of tweets on a user-defined topic, utilizing GPT-3.5's language model capabilities.
- **Interactive User Interface**: Simple and intuitive UI powered by Streamlit, allowing users to input their topic and choose the number of tweets to generate.
- **Real-time Results**: Instantly view generated tweets upon submission, with the flexibility to modify topics and numbers for new results.

## Acknowledgements

Special thanks to Satvik Paramkusham ([satvik314](https://github.com/satvik314)) for the GenAI Crash Course, which provided valuable insights and guidance in the development of this application. The course is a fantastic resource for anyone looking to dive into the world of generative AI.

## Getting Started

To use the Tweet-App-Generator, simply navigate to the deployed application's URL and:

1. Enter a topic of interest in the "Topic" input field.
2. Specify the number of tweets you wish to generate using the "Number of tweets" selector.
3. Click the "Generate" button to view the generated tweets based on your inputs.

## Requirements

This application is built using the following major dependencies:

- Streamlit
- langchain_openai
- langchain

Ensure you have an OpenAI API key to use the `langchain_openai` functionalities.

## Installation and Local Setup

To run Tweet-App-Generator locally, follow these steps:

```bash
git clone https://github.com/yourgithubusername/Tweet-App-Generator.git
cd Tweet-App-Generator
pip install -r requirements.txt
streamlit run main.py

# Environment Variables
Before running the application, ensure you set up the OPENAI_API_KEY in your Streamlit secrets file .streamlit/secrets.toml:
OPENAI_API_KEY = "your_openai_api_key_here"

