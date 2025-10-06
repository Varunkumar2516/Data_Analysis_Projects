import pandas as pd
import streamlit as st
import plotly.express as px

# ----------------- App Configuration -----------------
st.set_page_config(
    page_title="COVID-19 India Dashboard",
    page_icon="🦠",
    layout="wide"
)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file1 = os.path.join(BASE_DIR,"Datasets",'covid_19_india.csv')
file2 = os.path.join(BASE_DIR, "Datasets",'covid_vaccine_statewise.csv')



# ----------------- Data Loading and Caching -----------------
# Cache data loading to improve performance
@st.cache_data
def load_data():
    """Loads, cleans, and preprocesses the COVID-19 and vaccination data."""
    
    # Load COVID-19 case data
    covid_df = pd.read_csv(file1)
    
    # Load vaccination data
    vaccine_df = pd.read_csv(file2)

    # --- Preprocessing COVID-19 Data ---
    covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], axis=1, inplace=True)
    covid_df['Date'] = pd.to_datetime(covid_df['Date'], format='%Y-%m-%d')
    covid_df.dropna(inplace=True)
    covid_df['Active_Cases'] = covid_df['Confirmed'] - (covid_df['Cured'] + covid_df['Deaths'])
    
    # Statewise pivot table for latest stats
    statewise = pd.pivot_table(covid_df, values=["Confirmed", "Deaths", "Cured"], index="State/UnionTerritory", aggfunc='max')
    statewise["Recovery_Rate"] = statewise["Cured"] * 100 / statewise["Confirmed"]
    statewise["Death_Rate"] = statewise["Deaths"] * 100 / statewise["Confirmed"]
    statewise = statewise.sort_values(by='Confirmed', ascending=False)

    # --- Preprocessing Vaccination Data ---
    vaccine_df.rename(columns={"Updated On": "Vaccine_Date"}, inplace=True)
    vaccine_df.rename(columns={'Total Individuals Vaccinated': 'Total'}, inplace=True)
    vaccine_df = vaccine_df[vaccine_df["State"] != "India"] # Remove aggregate 'India' rows
    
    # Calculate Male vs Female vaccination totals
    male_vaccinated = vaccine_df["Male(Individuals Vaccinated)"].sum()
    female_vaccinated = vaccine_df["Female(Individuals Vaccinated)"].sum()

    # Most and least vaccinated states
    max_vac = vaccine_df.groupby('State')['Total'].sum().to_frame('Total').sort_values('Total', ascending=False)
    min_vac = max_vac.sort_values('Total', ascending=True)

    return covid_df, statewise, vaccine_df, male_vaccinated, female_vaccinated, max_vac, min_vac

# Load the processed data
covid_df, statewise, vaccine_df, male_vaccinated, female_vaccinated, max_vac, min_vac = load_data()

# ----------------- UI Layout and Dashboard -----------------

# --- Main Title ---
st.title("🦠 COVID-19 India Dashboard")
st.markdown("An interactive dashboard to analyze COVID-19 case and vaccination trends across India.")

# --- Key Metrics ---
st.header("Nationwide Overview")
total_confirmed = statewise["Confirmed"].sum()
total_cured = statewise["Cured"].sum()
total_deaths = statewise["Deaths"].sum()
total_active = total_confirmed - (total_cured + total_deaths)
total_vaccinated = vaccine_df['Total'].sum()

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Confirmed Cases", f"{total_confirmed:,.0f}")
col2.metric("Active Cases", f"{total_active:,.0f}")
col3.metric("Cured", f"{total_cured:,.0f}")
col4.metric("Deaths", f"{total_deaths:,.0f}")
col5.metric("Total Vaccinated", f"{total_vaccinated:,.0f}")

st.markdown("---")

# --- Visualizations Section ---
st.header("Deep Dive Analysis")

# --- Top 10 States by Active Cases and Deaths ---
col1, col2 = st.columns(2)

with col1:
    top_10_active_cases = covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by='Active_Cases', ascending=False).reset_index().head(10)
    fig_active = px.bar(top_10_active_cases, 
                        x="State/UnionTerritory", 
                        y="Active_Cases", 
                        color="State/UnionTerritory",
                        title="Top 10 States with Most Active Cases",
                        labels={'Active_Cases': 'Total Active Cases', 'State/UnionTerritory': 'State'})
    st.plotly_chart(fig_active, use_container_width=True)

with col2:
    top_10_deaths = covid_df.groupby(by='State/UnionTerritory').max()[['Deaths', 'Date']].sort_values(by='Deaths', ascending=False).reset_index().head(10)
    fig_deaths = px.bar(top_10_deaths, 
                        x="State/UnionTerritory", 
                        y="Deaths", 
                        color="State/UnionTerritory",
                        title="Top 10 States with Highest Deaths",
                        labels={'Deaths': 'Total Deaths', 'State/UnionTerritory': 'State'})
    st.plotly_chart(fig_deaths, use_container_width=True)

st.markdown("---")

# --- Growth Trend of Top 5 Affected States ---
st.subheader("Growth Trend in Top 5 Affected States")
top_5_states = statewise.head(5).index.tolist()
growth_trend_df = covid_df[covid_df['State/UnionTerritory'].isin(top_5_states)]

fig_growth = px.line(growth_trend_df,
                     x='Date', 
                     y='Active_Cases', 
                     color='State/UnionTerritory',
                     title='Active Cases Growth Trend in Top 5 States',
                     labels={'Active_Cases': 'Active Cases', 'Date': 'Date'})
st.plotly_chart(fig_growth, use_container_width=True)

st.markdown("---")

# --- Vaccination Insights ---
st.header("💉 Vaccination Insights")

col1, col2 = st.columns(2)

# --- Male vs Female Vaccination ---
with col1:
    gender_fig = px.pie(names=["Male Vaccinated", "Female Vaccinated"], 
                        values=[male_vaccinated, female_vaccinated],
                        title="Male vs. Female Vaccination Distribution",
                        hole=0.3)
    st.plotly_chart(gender_fig, use_container_width=True)

# --- Most Vaccinated States ---
with col2:
    fig_max_vac = px.bar(max_vac.head(5), 
                         x=max_vac.head(5).index, 
                         y="Total", 
                         color=max_vac.head(5).index,
                         title="Top 5 Most Vaccinated States",
                         labels={'Total': 'Total Individuals Vaccinated', 'State': 'State'})
    st.plotly_chart(fig_max_vac, use_container_width=True)

# --- Least Vaccinated States ---
st.subheader("Least Vaccinated States")
fig_min_vac = px.bar(min_vac.head(5), 
                     x=min_vac.head(5).index, 
                     y="Total",
                     color=min_vac.head(5).index,
                     title="Top 5 Least Vaccinated States",
                     labels={'Total': 'Total Individuals Vaccinated', 'State': 'State'})
st.plotly_chart(fig_min_vac, use_container_width=True)


st.markdown("---")
st.info("This dashboard provides a high-level analysis based on the provided datasets. All visualizations are interactive.")