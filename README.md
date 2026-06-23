# 📰 Multi-Agent Newsletter Generator

A multi-agent newsletter generation system built with **CrewAI** that transforms a single topic prompt into a polished, publication-ready newsletter. The system uses a team of specialized AI agents that collaborate in sequence to research, write, edit, and format content automatically.

---

## 📌 Overview

Creating a high-quality newsletter typically involves multiple steps, including researching information, drafting content, editing for clarity, and formatting for presentation. This project automates the entire workflow using CrewAI's multi-agent architecture.

Simply provide a topic, and the crew generates a complete newsletter with minimal human intervention.

---

## 🚀 Features

* 🤖 Fully autonomous newsletter generation
* 🔍 Automated research and information gathering
* ✍️ Structured content drafting
* 📝 Editorial review and quality assurance
* 🎨 Automated formatting and organization
* 📄 Markdown-based newsletter output
* 🔄 Modular and extensible CrewAI architecture
* ⚙️ Easy customization of agents, tasks, and prompts

---

## 🏗️ Architecture

The newsletter is generated through a pipeline of four specialized agents:

### 1. Researcher Agent

**Role:** Information Gathering Specialist

**Responsibilities:**

* Research the given topic
* Collect facts, trends, and supporting information
* Gather reliable sources and references

---

### 2. Writer Agent

**Role:** Newsletter Content Creator

**Responsibilities:**

* Transform research into engaging content
* Structure the newsletter into logical sections
* Create introductions, highlights, and conclusions

---

### 3. Editor Agent

**Role:** Quality Assurance Reviewer

**Responsibilities:**

* Improve readability and clarity
* Correct grammar and language issues
* Ensure consistency in tone and style
* Verify factual coherence

---

### 4. Formatter Agent

**Role:** Newsletter Presentation Specialist

**Responsibilities:**

* Apply final formatting
* Organize sections properly
* Generate a publication-ready newsletter

---

## 🔄 Workflow

```text
User Topic
    │
    ▼
Researcher Agent
    │
    ▼
Writer Agent
    │
    ▼
Editor Agent
    │
    ▼
Formatter Agent
    │
    ▼
Final Newsletter
```

---

## 📂 Project Structure

```bash
multiagent-newsletter/
│
├── agents.py          # Agent definitions
├── tasks.py           # Task definitions
├── tools.py           # Custom tools and utilities
├── crew.py            # Crew creation and orchestration
├── app.py             # Application entry point
├── newsletter.md      # Generated newsletter output
├── requirements.txt   # Project dependencies
├── .env               # Environment variables
└── README.md          # Project documentation
```

---

## 🛠️ Tech Stack

| Technology  | Purpose                         |
| ----------- | ------------------------------- |
| Python      | Core programming language       |
| CrewAI      | Multi-agent orchestration       |
| Groq/OpenAI | Large Language Model provider   |
| dotenv      | Environment variable management |
| Markdown    | Newsletter output format        |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/multiagent-newsletter.git
cd multiagent-newsletter
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the value with your actual API key.

---

## ▶️ Usage

Run the application:

```bash
python app.py
```

Provide a topic when prompted:

```text
Artificial Intelligence in Healthcare
```

The crew will automatically:

1. Research the topic
2. Draft the newsletter
3. Edit and refine the content
4. Format the final output

The generated newsletter will be saved as:

```text
newsletter.md
```

---

## 📖 Example Output Structure

```text
Newsletter Title

Introduction

Key Highlights

Industry Insights

Important Updates

Conclusion
```

---

## 🎯 Why This Project?

Writing newsletters manually can be repetitive and time-consuming. This project helps by:

* Saving hours of manual work
* Maintaining consistent content quality
* Scaling newsletter creation across multiple topics
* Demonstrating practical multi-agent collaboration
* Providing a reusable CrewAI project template

---

## 🔧 Customization

### Add New Agents

Examples:

* Fact Checker Agent
* SEO Optimization Agent
* Social Media Agent
* Summarization Agent

### Modify Existing Tasks

Update prompts and task configurations inside:

```python
tasks.py
```

### Change LLM Provider

The architecture supports multiple providers:

* Groq
* OpenAI
* Anthropic
* Gemini
* Local LLMs

---

## 🔮 Future Enhancements

* Streamlit Web Interface
* Email Newsletter Delivery
* PDF Export Support
* Newsletter Templates
* Scheduled Generation
* Multi-language Support
* Advanced Fact Verification

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Built using **CrewAI** and **Large Language Models** to demonstrate real-world multi-agent collaboration for automated content generation.
