import validators
import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader


## Streamlit App
st.set_page_config(page_title="Langchain: Summarize Text from YT or Website",page_icon="🦜")
st.title("🦜 Langchain: Summarize Text from YT or Website")
st.subheader('Summarize URL')


## Get the groq api key and url(YT or website) to be summarzed
# with st.sidebar:
#     groq_api_key = st.text_input("GROQ API Key",value="",type="password")

generic_url = st.text_input("URL",label_visibility="collapsed")



prompt_template = """
Provide a concise 300-word summary of the following content:
{text}
"""

prompt = PromptTemplate(template=prompt_template,input_variables=["text"])

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if  not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can may be a YT video or website URL")

    else:
        try:
            with st.spinner("Waiting...."):
                ## loading the website or yt video data

                llm = ChatGroq(model = "Gemma2-9b-It" ,api_key="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")

                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url,add_video_info=True,language="en")
                else:
                    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
                    loader = UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,headers=headers)

                data = loader.load()

                ## Chain for Summarization
                chain = load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary = chain.run(input_documents=data)

                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")