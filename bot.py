from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import OpenAI
from streamlit_chat import message
from langchain.schema import SystemMessage, HumanMessage, AIMessage

import pandas as pd
from langchain_openai import OpenAI


file='/Users/mhmh/Desktop/p2/abd/mov.csv'
df=pd.read_csv(file)

    
sample_promp1="give number of cars for each day , for the last 5 days"
sample_promp2="give number of cars of audi used for each week for last 5 weeks"

agent = create_pandas_dataframe_agent(OpenAI(temperature=0,api_key=""), df, verbose=False,return_intermediate_steps=True)
response_1 = agent.invoke(sample_promp1)
response_2 = agent.invoke(sample_promp2)

x1=response_1["intermediate_steps"]
x2=response_2["intermediate_steps"]


fg1=pd.DataFrame()
fg2=pd.DataFrame()


action_inputs_1=[action[0].tool_input for action in x1]
action_inputs_2=[action[0].tool_input for action in x2]
new1="fg1="+action_inputs_1[-1]
new2="fg2="+action_inputs_2[-1]


exec(new1)
exec(new2)
st.subheader("Prompt : give number of cars for each day , for the last 5 days ")
st.bar_chart(fg1)
st.subheader("Prompt : give number of cars of audi used for each week for last 5 weeks")
st.line_chart(fg2)


if True:

    
    with st.sidebar:
        input_file = st.file_uploader("File upload here", type="csv")
    st.header("Bot test (memory not yet added , is not coversational)")
    if input_file is not None:
        question = st.text_input("Ask me something")
        
        llm = OpenAI(temperature=0,api_key="")
        agent = create_csv_agent(llm, input_file)
    
        

        

        if question is not None and question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(question))

    
    
