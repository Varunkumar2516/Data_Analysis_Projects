import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="Titanic Survival Analysis",
    page_icon="🚢",
    layout="wide"
)

# --- Data Loading ---
# Use caching to improve performance
@st.cache_data
def load_data(file_path):
    """Loads the Titanic dataset from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        # Basic data cleaning for age
        df['Age'].fillna(df['Age'].median(), inplace=True)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file '{file_path}' was not found. Please make sure it's in the same directory.")
        return None

# Load the dataset
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = os.path.join(BASE_DIR, "DATASET", "datasets",'train.csv')
df = pd.read_csv(file)


# --- Main Application ---
if df is not None:
    # --- Header ---
    st.title("🚢 Titanic Survival Analysis")
    st.markdown("""
    An interactive dashboard to explore the factors that influenced passenger survival aboard the Titanic. 
    Use the filters in the sidebar to dynamically explore the data.
    """)

    # --- Sidebar for Filters ---
    st.sidebar.header("Filters")
    
    # Gender filter
    gender_options = ['All'] + list(df['Sex'].unique())
    selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

    # Passenger Class filter
    pclass_options = ['All'] + sorted(list(df['Pclass'].unique()))
    selected_pclass = st.sidebar.selectbox("Select Passenger Class", pclass_options)

    # --- Data Filtering ---
    # Apply filters to the dataframe
    filtered_df = df.copy()
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df['Sex'] == selected_gender]
    if selected_pclass != 'All':
        filtered_df = filtered_df[filtered_df['Pclass'] == selected_pclass]

    # --- Key Performance Indicators (KPIs) ---
    st.markdown("### Key Metrics")
    total_passengers = filtered_df.shape[0]
    survival_rate = (filtered_df['Survived'].sum() / total_passengers) * 100 if total_passengers > 0 else 0
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Passengers in Selection", value=f"{total_passengers}")
    with col2:
        st.metric(label="Survival Rate", value=f"{survival_rate:.2f}%")

    st.markdown("---")


    # --- Charts ---
    st.markdown("### Visualizations")
    col1, col2 = st.columns(2)

    with col1:
        # Survival by Gender Chart
        st.subheader("Survival by Gender")
        if not filtered_df.empty:
            gender_survival = filtered_df.groupby('Sex')['Survived'].value_counts(normalize=True).unstack().fillna(0) * 100
            gender_survival = gender_survival.rename(columns={0: 'Did not Survive', 1: 'Survived'})
            fig_gender = px.bar(gender_survival, barmode='stack',
                                labels={'value': 'Percentage', 'Sex': 'Gender'},
                                title="Survival Percentage by Gender",
                                color_discrete_map={'Survived': '#0d9488', 'Did not Survive': '#64748b'})
            st.plotly_chart(fig_gender, use_container_width=True)
        else:
            st.warning("No data available for the selected filters.")

    with col2:
        # Survival by Passenger Class Chart
        st.subheader("Survival by Passenger Class")
        if not filtered_df.empty:
            pclass_survival = filtered_df.groupby('Pclass')['Survived'].value_counts(normalize=True).unstack().fillna(0) * 100
            pclass_survival = pclass_survival.rename(columns={0: 'Did not Survive', 1: 'Survived'})
            fig_pclass = px.bar(pclass_survival, barmode='stack',
                                labels={'value': 'Percentage', 'Pclass': 'Passenger Class'},
                                title="Survival Percentage by Class",
                                color_discrete_map={'Survived': '#0d9488', 'Did not Survive': '#64748b'})
            st.plotly_chart(fig_pclass, use_container_width=True)
        else:
            st.warning("No data available for the selected filters.")


    # Age Distribution Chart
    st.subheader("Age Distribution")
    if not filtered_df.empty:
        fig_age = px.histogram(filtered_df, x="Age", color="Survived",
                               marginal="box", # or violin
                               hover_data=df.columns,
                               title="Age Distribution by Survival Status",
                               color_discrete_map={1: '#0d9488', 0: '#64748b'})
        st.plotly_chart(fig_age, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")

else:
    st.info("Please upload the `train.csv` file to begin the analysis.")
