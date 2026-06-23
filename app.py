import time
from datetime import datetime

import streamlit as st
from crewai import Crew, Process

from agents import researcher, writer, proof_reader
from tasks import research_task, write_task, proof_read_task

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Multiagent Newsletter",
    page_icon="📰",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background: radial-gradient(circle at top left, #1b1f3b 0%, #0e1117 45%, #0e1117 100%);
    }

    /* Hero header */
    .hero {
        padding: 2.2rem 2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #6d5dfc 0%, #8b5cf6 45%, #ec4899 100%);
        box-shadow: 0 12px 40px rgba(109, 93, 252, 0.35);
        margin-bottom: 1.8rem;
    }
    .hero h1 {
        color: white;
        font-weight: 800;
        font-size: 2.1rem;
        margin-bottom: 0.3rem;
        letter-spacing: -0.5px;
    }
    .hero p {
        color: rgba(255,255,255,0.88);
        font-size: 1.02rem;
        margin: 0;
    }

    /* Section card */
    .card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1.2rem;
    }

    /* Buttons */
    div.stButton > button {
        border-radius: 10px;
        font-weight: 600;
        padding: 0.55rem 1.2rem;
        border: none;
        transition: all 0.15s ease;
    }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #6d5dfc, #8b5cf6);
        color: white;
    }
    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(139, 92, 246, 0.4);
    }

    div.stDownloadButton > button {
        border-radius: 10px;
        font-weight: 600;
        background: linear-gradient(135deg, #22c55e, #16a34a);
        color: white;
        border: none;
    }

    /* Text input */
    div[data-testid="stTextInput"] input {
        border-radius: 10px;
        padding: 0.6rem 0.9rem;
    }

    /* Badges */
    .badge {
        display: inline-block;
        background: rgba(139, 92, 246, 0.18);
        color: #c4b5fd;
        border: 1px solid rgba(139, 92, 246, 0.35);
        border-radius: 999px;
        padding: 0.15rem 0.7rem;
        font-size: 0.78rem;
        font-weight: 600;
        margin-right: 0.4rem;
    }

    .footer-note {
        text-align: center;
        color: rgba(255,255,255,0.35);
        font-size: 0.82rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Session state setup
# ----------------------------------------------------------------------------
defaults = {
    "result": "",
    "history": [],       # list of {"topic", "content", "timestamp"}
    "last_topic": "",
    "is_running": False,
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ Pipeline")
    st.markdown(
        """
        <span class="badge">🔎 Researcher</span>
        <span class="badge">✍️ Writer</span>
        <span class="badge">🧐 Proofreader</span>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Agents run sequentially: research → draft → polish.")

    st.divider()
    st.markdown("### 🕘 History")
    if st.session_state["history"]:
        for i, item in enumerate(reversed(st.session_state["history"])):
            with st.expander(f"{item['topic']}  ·  {item['timestamp']}"):
                st.markdown(item["content"][:300] + ("…" if len(item["content"]) > 300 else ""))
                if st.button("Restore", key=f"restore_{i}"):
                    st.session_state["result"] = item["content"]
                    st.rerun()
        if st.button("🗑️ Clear history", use_container_width=True):
            st.session_state["history"] = []
            st.rerun()
    else:
        st.caption("No newsletters generated yet.")

# ----------------------------------------------------------------------------
# Hero header
# ----------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>📰 Multiagent Newsletter Composer</h1>
        <p>Give the crew a topic — a researcher, writer, and proofreader will turn it into a polished newsletter.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Input card
# ----------------------------------------------------------------------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    topic = st.text_input(
        "Topic",
        key="topic_input",
        placeholder="e.g. The future of renewable energy storage",
        label_visibility="visible",
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        compose_clicked = st.button("🚀 Compose Newsletter", use_container_width=True)
    with col2:
        clear_clicked = st.button("🧹 Clear", use_container_width=True)
    with col3:
        rerun_clicked = st.button("🔁 Regenerate", use_container_width=True, disabled=not st.session_state["last_topic"])
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# Actions
# ----------------------------------------------------------------------------
def run_crew(active_topic: str):
    steps = ["Researching topic…", "Drafting newsletter…", "Proofreading & polishing…"]
    progress = st.progress(0, text=steps[0])
    status = st.empty()

    crew = Crew(
        agents=[researcher, writer, proof_reader],
        tasks=[research_task, write_task, proof_read_task],
        process=Process.sequential,
        verbose=True,
    )

    try:
        # Simulated step progress while the actual crew call runs synchronously.
        progress.progress(10, text=steps[0])
        result = crew.kickoff(inputs={"topic": active_topic})
        progress.progress(70, text=steps[1])
        time.sleep(0.2)
        progress.progress(90, text=steps[2])
        time.sleep(0.2)
        progress.progress(100, text="Done!")
        status.success("Newsletter composed successfully.")
        return str(result)
    except Exception as e:
        status.error(f"Error running agents: {e}")
        return ""
    finally:
        time.sleep(0.4)
        progress.empty()


if clear_clicked:
    st.session_state["result"] = ""
    st.session_state["last_topic"] = ""
    st.rerun()

if compose_clicked:
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Running agents — this may take a while…"):
            content = run_crew(topic)
        if content:
            st.session_state["result"] = content
            st.session_state["last_topic"] = topic
            st.session_state["history"].append(
                {
                    "topic": topic,
                    "content": content,
                    "timestamp": datetime.now().strftime("%b %d, %H:%M"),
                }
            )
        else:
            st.session_state["result"] = ""

if rerun_clicked and st.session_state["last_topic"]:
    with st.spinner("Regenerating — this may take a while…"):
        content = run_crew(st.session_state["last_topic"])
    if content:
        st.session_state["result"] = content
        st.session_state["history"].append(
            {
                "topic": st.session_state["last_topic"],
                "content": content,
                "timestamp": datetime.now().strftime("%b %d, %H:%M"),
            }
        )

# ----------------------------------------------------------------------------
# Output
# ----------------------------------------------------------------------------
if st.session_state["result"]:
    result_text = st.session_state["result"]
    word_count = len(result_text.split())
    read_time = max(1, round(word_count / 200))

    st.markdown('<div class="card">', unsafe_allow_html=True)

    head_col, m1, m2 = st.columns([2, 1, 1])
    with head_col:
        st.subheader("✅ Final Newsletter")
    with m1:
        st.metric("Words", word_count)
    with m2:
        st.metric("Read time", f"{read_time} min")

    tab_preview, tab_raw = st.tabs(["📖 Preview", "🔤 Raw markdown"])
    with tab_preview:
        st.markdown(result_text, unsafe_allow_html=True)
    with tab_raw:
        st.code(result_text, language="markdown")

    dl_col, save_col = st.columns([1, 1])
    with dl_col:
        st.download_button(
            "⬇️ Download (.md)",
            result_text,
            file_name="newsletter.md",
            mime="text/markdown",
            use_container_width=True,
        )
    with save_col:
        if st.button("💾 Save to workspace file", use_container_width=True):
            try:
                with open("newsletter.md", "w", encoding="utf-8") as f:
                    f.write(result_text)
                st.success("Saved to newsletter.md")
            except Exception as e:
                st.error(f"Error saving file: {e}")

    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Enter a topic above and click **Compose Newsletter** to get started.")

st.markdown('<p class="footer-note">Powered by CrewAI · researcher → writer → proofreader</p>', unsafe_allow_html=True)