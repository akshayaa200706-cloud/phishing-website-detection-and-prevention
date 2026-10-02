
import sys
import os
import streamlit as st


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

SRC_PATH = os.path.join(PROJECT_ROOT, "src")

sys.path.append(SRC_PATH)

from prediction import predict_url


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="PhishGuard",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PAGE STYLE
# ============================================================

st.markdown(
    """
    <style>

    /* Background */

    .stApp {
        background:
        linear-gradient(
            135deg,
            #eef6ff,
            #f8faff,
            #eef2ff
        );
    }


    /* Main container */

    .block-container {
        max-width: 850px;
        padding-top: 40px;
        padding-bottom: 50px;
    }


    /* Hide Streamlit branding */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* Title */

    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 800;
        color: #172554;
        margin-bottom: 5px;
    }


    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #64748b;
        margin-bottom: 30px;
    }


    /* Shield */

    .shield {
        text-align: center;
        font-size: 65px;
        margin-bottom: 5px;
    }


    /* Input */

    div[data-testid="stTextInput"] input {
        height: 58px;
        border-radius: 14px;
        border: 2px solid #dbeafe;
        background: white;
        font-size: 16px;
        padding-left: 18px;
    }


    div[data-testid="stTextInput"] input:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 3px rgba(99,102,241,0.15);
    }


    /* Scan button */

    .stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 14px;
        border: none;
        background: linear-gradient(
            90deg,
            #4f46e5,
            #6366f1
        );
        color: white;
        font-size: 17px;
        font-weight: 700;
        box-shadow: 0 8px 20px rgba(79,70,229,0.25);
    }


    .stButton > button:hover {
        background: linear-gradient(
            90deg,
            #4338ca,
            #4f46e5
        );
        color: white;
    }


    /* Footer */

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 45px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="shield">🛡️</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">PhishGuard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Check before you click.</div>',
    unsafe_allow_html=True
)


# ============================================================
# INTRODUCTION
# ============================================================

st.info(
    "🔐 Protect yourself from suspicious websites. "
    "Enter a URL below to check it before you interact with it."
)


# ============================================================
# URL INPUT
# ============================================================

url = st.text_input(
    "Website URL",
    placeholder="🔗  Enter website address...",
    label_visibility="collapsed"
)


scan = st.button(
    "🔍  SCAN WEBSITE"
)


# ============================================================
# ANALYSIS
# ============================================================

if scan:

    if not url.strip():

        st.warning(
            "⚠️ Please enter a website address first."
        )

    else:

        with st.spinner(
            "🔎 Checking website security..."
        ):

            try:

                result = predict_url(
                    url.strip()
                )

                prediction = result["result"]


                # ==================================================
                # PHISHING RESULT
                # ==================================================

                if prediction == "PHISHING":

                    st.write("")

                    st.error(
                        "🚨  DANGER — PHISHING WEBSITE DETECTED"
                    )

                    st.write("")

                    st.subheader(
                        "🛑 Stop! Do not continue."
                    )

                    st.warning(
                        "This website appears suspicious and "
                        "may be attempting to steal your information."
                    )

                    st.write("")

                    st.markdown(
                        "### 🔐 Protect your information"
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        st.info(
                            "🔑 **Do not enter passwords**"
                        )

                        st.info(
                            "📱 **Do not enter OTPs**"
                        )

                    with col2:

                        st.info(
                            "💳 **Do not enter bank details**"
                        )

                        st.info(
                            "👤 **Do not share personal information**"
                        )

                    st.write("")

                    st.error(
                        "🚪 Recommended action: Leave this website."
                    )


                # ==================================================
                # LEGITIMATE RESULT
                # ==================================================

                else:

                    st.write("")

                    st.success(
                        "🟢  WEBSITE CHECK COMPLETE"
                    )

                    st.write("")

                    st.subheader(
                        "🛡️ This website appears safe"
                    )

                    st.info(
                        "✅ No phishing indicators were detected "
                        "by the security system."
                    )

                    st.write("")

                    st.success(
                        "You may continue, but always stay alert "
                        "when sharing sensitive information online."
                    )


            except Exception:

                st.error(
                    "⚠️ We couldn't check this website."
                )

                st.info(
                    "Please check the URL and try again."
                )


# ============================================================
# HOW IT PROTECTS YOU
# ============================================================

st.write("")

st.subheader(
    "✨ Why use PhishGuard?"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        "🤖\n\n"
        "**Smart Detection**\n\n"
        "Identifies suspicious website patterns."
    )

with col2:

    st.info(
        "⚡\n\n"
        "**Quick Check**\n\n"
        "Analyze a URL before you click."
    )

with col3:

    st.info(
        "🛡️\n\n"
        "**Stay Protected**\n\n"
        "Receive a clear warning when a website looks dangerous."
    )


# ============================================================
# SAFETY TIP
# ============================================================

st.write("")

with st.container(border=True):

    st.subheader(
        "💡 Online Safety Tip"
    )

    st.write(
        "Never enter passwords, OTPs, banking information, "
        "or personal details on a website unless you are "
        "sure it is trustworthy."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🛡️ PhishGuard<br>
    Phishing Website Detection & Prevention<br>
    Built with Machine Learning

    </div>
    """,
    unsafe_allow_html=True
)