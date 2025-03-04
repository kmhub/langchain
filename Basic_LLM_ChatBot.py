{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyODQwXdlCU5EHrgUJ/OZkiX"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Streamlit ChatBot App using Langchain and OpenAI LLM GPT Models\n",
        "\n",
        "*  OpenAI LLM Chat Models and OpenAI API Key\n",
        "*  Langchain open source python framework - chains, agents and tools\n",
        "\n",
        "Basic Steps for Streamlit App to Run locally\n",
        "*   Install python\n",
        "*   Open Terminal or Command Line and check python is installed >> python3 --version\n",
        "*   Install streamlit >> pip3 install streamlit\n",
        "*   Add python to PATH env variable >> nano ~/.bash_profile >> export PATH=\"/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH\"\n",
        "*   Save the file as .py and run the command >> streamlit run appname.py"
      ],
      "metadata": {
        "id": "Jp3wfC62y6H6"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "CYLcDBPgdF8-"
      },
      "outputs": [],
      "source": [
        "# Install dependencies\n",
        "!pip install streamlit\n",
        "!pip install langchain\n",
        "!pip install langchain_community\n",
        "!pip install openai\n",
        "!pip install -U duckduckgo-search\n",
        "!pip install arxiv\n",
        "!pip install wikipedia\n",
        "!pip install langchain-openai"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "from langchain.agents import (\n",
        "    AgentExecutor, AgentType, initialize_agent, load_tools\n",
        ")\n",
        "\n",
        "#from langchain.chat_models import ChatOpenAI\n",
        "from langchain_openai import ChatOpenAI\n",
        "\n",
        "import os\n",
        "os.environ[\"OPENAI_API_KEY\"] = \" \" # provide your API key from https://platform.openai.com/api-keys"
      ],
      "metadata": {
        "id": "24R9-WNqd08t"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# This function returns AgentExecutor which is a chain\n",
        "def load_agent() -> AgentExecutor:\n",
        "\n",
        "    # streaming = True will result in better user experience since it means that the text response will be updated as it comes in, rather than once all the text has been completed\n",
        "    llm = ChatOpenAI(model=\"gpt-4o\",temperature=0, streaming=True)\n",
        "\n",
        "    # DuckDuckGo: A search engine that focuses on privacy; an added advantage is that it doesn’t require developer signup\n",
        "    # Wolfram Alpha: An integration that combines natural language understanding with math capabilities, for questions like “What is 2x+5 = -3x + 7?”\n",
        "    # arXiv: Search in academic pre-print publications; this is useful for research-oriented questions\n",
        "    # Wikipedia: For any question about entities of significant notoriety\n",
        "\n",
        "    tools = load_tools(\n",
        "        tool_names=[\"ddg-search\", \"arxiv\", \"wikipedia\"], # \"wolfram-alpha\" - requires a key\n",
        "        llm=llm\n",
        "    )\n",
        "\n",
        "    return initialize_agent(\n",
        "        tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True\n",
        "    )"
      ],
      "metadata": {
        "id": "uBXf5dwcdfzi"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "from langchain.callbacks import StreamlitCallbackHandler\n",
        "\n",
        "chain = load_agent()\n",
        "\n",
        "st_callback = StreamlitCallbackHandler(st.container())\n",
        "\n",
        "if prompt := st.chat_input():\n",
        "    st.chat_message(\"user\").write(prompt)\n",
        "    with st.chat_message(\"assistant\"):\n",
        "        st_callback = StreamlitCallbackHandler(st.container())\n",
        "        response = chain.run(prompt, callbacks=[st_callback])\n",
        "        st.write(response)"
      ],
      "metadata": {
        "id": "go0dInhwf9V4"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n"
      ],
      "metadata": {
        "id": "6-ecH4sflmyU"
      }
    }
  ]
}