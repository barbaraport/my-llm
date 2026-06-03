# Scholarship Summarizer API

A REST API that collects master's degree scholarship information and generates concise AI-powered summaries.

The API currently supports scholarship programs listed on the Erasmus Mundus catalogue and uses either OpenRouter-hosted LLMs or locally hosted Ollama models to summarize program descriptions.

## Features

* Scrapes scholarship information from Erasmus Mundus program pages
* Extracts and cleans relevant program content
* Generates AI-powered summaries using LLMs
* Supports multiple model providers through OpenRouter
* Supports local inference with Ollama
* Streams generated summaries in real time
* Uses asynchronous LLM streaming via the OpenAI Async Client
* Environment-based configuration using Pydantic Settings

## Tech Stack

| Component          | Technology        |
| ------------------ | ----------------- |
| API Framework      | FastAPI           |
| Web Scraping       | BeautifulSoup4    |
| HTTP Client        | Requests          |
| HTML Parser        | lxml              |
| LLM Gateway        | OpenRouter        |
| Local LLM Runtime  | Ollama            |
| AI SDK             | OpenAI Python SDK |
| Configuration      | Pydantic Settings |
| Package Management | uv                |
| Runtime            | Python 3.12+      |

## Architecture

<div align="center">
<pre>
Erasmus Mundus Website
│
▼
Web Scraper
(Requests + BS4)
│
▼
Content Extraction
│
▼
┌─────────────────┐
│    OpenRouter   │
│        or       │
│      Ollama     │
└─────────────────┘
│
▼
Selected LLM
│
▼
Streaming Output
│
▼
FastAPI
REST API
</pre>
</div>

## How It Works

1. Fetch scholarship program pages from the Erasmus Mundus catalogue.
2. Extract and clean relevant program information.
3. Send the extracted content to a language model.
4. Receive generated tokens through a streaming response.
5. Stream the generated summary back to the client in real time.

## Key Design Decisions

### Streaming Responses

The API returns summaries as a stream instead of waiting for the entire generation to finish.

This is implemented using:

* FastAPI asynchronous endpoints
* OpenAI Async Client
* Token streaming
* Python generators (`yield`)

Benefits:

* Lower perceived latency
* Faster feedback to API consumers
* Better user experience for long generations
* Reduced waiting time before receiving the first tokens

### Flexible Model Providers

The API can run with either:

#### OpenRouter

Use cloud-hosted models from providers such as:

* OpenAI
* Anthropic
* Google
* DeepSeek
* Mistral
* Meta

#### Ollama

Run models locally for:

* Offline development
* Reduced inference costs
* Improved privacy
* Self-hosted deployments

## Prerequisites

* Python 3.12+
* Make

Additionally, choose one of:

* OpenRouter API key
* Ollama installed locally

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd masters-summarizer-api
```

Install dependencies and create the virtual environment:

```bash
make setup
```

## Configuration

Create a `.env` file:

```env
API_KEY="<your_api_key>"
API_BASE_URL="<api_base_url>" # Ollama: http://localhost:11434/v1
MODEL_NAME="<preferred_model_name>"
CATALOGUE_URL="https://www.eacea.ec.europa.eu/scholarships/erasmus-mundus-catalogue_en"
```

### Option 1: OpenRouter

The same `.env` file can be used for both approaches.

### Option 2: Ollama

Start Ollama locally:

```bash
ollama serve
```

Pull a model:

```bash
ollama pull llama3.2
```

Because Ollama exposes an OpenAI-compatible API, the same OpenAI SDK can be used for both providers.

## Running the API

Start the development server:

```bash
make run
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

## Development Commands

| Command          | Description                                          |
| ---------------- | ---------------------------------------------------- |
| `make setup`     | Install uv and project dependencies                  |
| `make run`       | Start the FastAPI development server                 |
| `make reset`     | Remove virtual environment, caches, and uv artifacts |
| `make update-uv` | Update uv to the latest version                      |
