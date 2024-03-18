import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

### CONFIG
st.set_page_config(
    page_title="Get around Dashboard",
    page_icon="🚗",
    layout="wide"
)


### TITLE AND TEXT
st.title("Dashboard Get Around 🕰️🚗")

st.markdown("""
    # Optimization car reservation delay with Get Around

Welcome to our interactive analytics app dedicated to optimizing car booking wait times for the Get Around business.
This application has been specially designed to help you analyze and improve the booking experience of Get Around vehicles.
""")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df_delay = pd.read_csv(uploaded_file)

# Run the below code if the check is checked ✅
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df_delay)
    
st.markdown("<br><br>", unsafe_allow_html=True)


### SHOW GRAPH PLOTLY + STREAMLIT

#1
col1, col2 = st.columns(2)

with col1:
    st.subheader("Number of delays at checkout")

    fig = px.histogram(df_delay, x='checkout_status', color='checkout_status', text_auto=True)
    fig.update_layout(bargap=0.2)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Percentage of cancellations based on different checkout status")

    with st.form('status_form'):
        checkout_status = df_delay['checkout_status'].unique()
        checkout_status = st.selectbox("Sélectionnez un statut de checkout", checkout_status)
        submit_button = st.form_submit_button("Confirmer")

        if submit_button:
            canceled_data = df_delay[df_delay['state'] == 'canceled']
            canceled_by_status = canceled_data.groupby('checkout_status').size()
            total_canceled = canceled_data.shape[0]
            if checkout_status in canceled_by_status:
                av_canceled = canceled_by_status[checkout_status] / total_canceled
                st.metric("Moyenne des annulations", np.round(av_canceled*100, 2))
            else:
                st.metric("Moyenne des annulations", 0.0)


#2
mask = df_delay['state'] == 'canceled'
df_canceled = df_delay.loc[mask,:]

st.subheader("Cancelation according to the checkin_type")
fig = px.pie(data_frame = df_canceled, names = 'checkin_type')
fig.update_layout(bargap=0.2)
st.plotly_chart(fig, use_container_width=True)


st.subheader("Checkout delay according to the checkin_type")
fig = px.histogram(df_delay, x='checkout_status', color='checkin_type', histnorm='percent',
                height=350)
fig.update_layout(bargap=0.2)
st.plotly_chart(fig, use_container_width=True)


#3
col1, col2 = st.columns(2)

with col1:
    fig = px.pie(data_frame = df_delay, names = 'checkin_type', title = 'Pie chart checkin type')
    st.plotly_chart(fig, use_container_width=True)
    
with col2:
    fig = px.pie(data_frame = df_canceled, names = 'checkin_type', title = 'Cancelation according to the checkin_type')
    st.plotly_chart(fig)
    
    
#4    
st.subheader("Status according to delay(checkout_status) and checkin type")   
fig = px.histogram(df_delay, x='state', color = 'checkout_status', facet_col= 'checkin_type')
st.plotly_chart(fig, use_container_width=True)
    

def main():
    print("")

if __name__ == "__main__":
    main()


