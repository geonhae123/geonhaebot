import streamlit as st
import openai
import os
from datetime import datetime


def ask_gpt(prompt,model, apikey):
    client = openai.OpenAI(api_key = apikey)
    response = client.chat.completions.create(
        model= model, messages=prompt)
    gptResponse = response.choices[0].message.content
    return gptResponse
    
    

def main():
     
     st.set_page_config(
         page_title=" 비서 프로그램",
         layout="wide")
     
     st.header("비서 프로그램")
     
     
     st.markdown("--")
     
     with st.expander("비서 프로그램에 관하여", expanded=True):
         st.write(
             """
            -비서 프로그램의 UI는 스트림릿을 활용했습니다.
            
            -답변은 OpenAI의 GPT 모델을 활용했습니다.
            -TTS(Text-To-Speech)는 구글의 Google Translate TTS를 활용했습니다.
            """
         )
         st.markdown("")
         
         if "chat" not in st.session_state:
            st.session_state["chat"] = []
        
         if "OPENAI_API" not in st.session_state:
             st.session_state["OPENAI_API"]= ""
        
         if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "system", "content": "You are a thoutful. korea"}]
        
         if "check_audio" not in st.session_state:
            st.session_state["check_reset"] =False
                    
         
         
     with st.sidebar:
         
         st.session_state["OPENAI_API"] = st.text_input(label="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", placeholder="Enter Your API key", value="", type="password")
         
         st.markdown("")
         
         model = st.radio(label="GPT모델", options=["gpt-4", "gpt-3.5-turbo"])
         
         st.markdown("---")
         
         if st.button(label="초기화"):
        
           col1, col2 = st.colums(2)
           with col1:
            
             st.subheader("질문하기")
           
           with col2:
             st.subheader("질문/답변")
             
             st.session_state["chat"] = []
             st.seesion_state["check_reset"] = True
         
             st.session_state["message"] = st.session_state["messages"] + [{"role":"system", "content": response}]
             
             now = datetime.now().strftime("%H:%M")
             st.session_state["chat"] = st.session_state["chat"]+ [("bot", now, response)]
             
             response = ask_gpt(st.session_state["message"], model, st.session_state["OpenAI_API"]
                                )
             
             for sender, time, message in st.session_state["chat"]:

                if sender == "user":

                 st.write(f'<div style="display:flex;align-items:center;"><div style="background-color:#007AFF;color:white;border-radius:12px;padding:8px 12px;margin-right:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)

                 st.write("")

                else:

                 st.write(f'<div style="display:flex;align-items:center;justify-content:flex-end;"><div style="background-color:lightgray;border-radius:12px;padding:8px 12px;margin-left:8px;">{message}</div><div style="font-size:0.8rem;color:gray;">{time}</div></div>', unsafe_allow_html=True)

                st.write("")

                               
             
        
    
    
            
       
             
if __name__=="__main__":
                main()