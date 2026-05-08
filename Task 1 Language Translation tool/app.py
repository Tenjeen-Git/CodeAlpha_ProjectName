import streamlit as st
from translator import translate_text

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Marathi": "mr",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it"
}

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #1f2937;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .result-box {
        background: black;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
        font-size: 18px;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: #9ca3af;
        font-size: 14px;
    }

    div.stButton > button {
        width: 100%;
        height: 48px;
        border-radius: 12px;
        font-size: 18px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>🌍 Language Translator</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Translate text instantly with a clean and simple interface</div>",
    unsafe_allow_html=True
)

with st.container():
    input_text = st.text_area(
        "Enter text",
        height=170,
        placeholder="Type something to translate..."
    )

    col1, col2 = st.columns(2)

    with col1:
        source_language_name = st.selectbox(
            "From",
            list(LANGUAGES.keys()),
            index=0
        )

    with col2:
        target_language_name = st.selectbox(
            "To",
            list(LANGUAGES.keys()),
            index=1
        )

    source_language = LANGUAGES[source_language_name]
    target_language = LANGUAGES[target_language_name]

    translate_clicked = st.button("Translate ✨")

if translate_clicked:
    if not input_text.strip():
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("Please select two different languages.")

    else:
        with st.spinner("Translating..."):
            try:
                translated_text = translate_text(
                    input_text,
                    source_language,
                    target_language
                )

                st.success("Translation complete")

                st.markdown("### Translated Text")
                st.markdown(
                    f"<div class='result-box'>{translated_text}</div>",
                    unsafe_allow_html=True
                )

                st.download_button(
                    label="Download Translation",
                    data=translated_text,
                    file_name="translation.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(str(e))

st.markdown(
    "<div class='footer'>Built with Streamlit · Clean UI Translation Tool</div>",
    unsafe_allow_html=True
)


