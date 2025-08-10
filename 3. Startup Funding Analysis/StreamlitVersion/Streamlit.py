import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
#title of our page

st.set_page_config(layout="wide",page_title='Startup Analysis')


#file 

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file = os.path.join(BASE_DIR, "Analysis_Notebook", "Startup_Cleaned.csv")
df = pd.read_csv(file)

# file='../Analysis_Notebook/Startup_Cleaned.csv'
# df=pd.read_csv(file)


df_for_investor=df.copy()
df_for_investor['investor']=df_for_investor['investor'].str.split(",")
df_for_investor['Investor_num']=df_for_investor['investor'].apply(len)
df_for_investor['amount_per_investor']=df_for_investor['amount']/ df_for_investor['Investor_num']
df_for_investor=df_for_investor.explode('investor')
requirement=df_for_investor.groupby("investor")['amount_per_investor'].sum().sort_values(ascending=False)
top_10_investors=pd.DataFrame(requirement).sort_values(by='amount_per_investor',ascending=False).head()
least_10=pd.DataFrame(requirement[requirement>0]).sort_values(by="amount_per_investor").head()
df['startup']=df['startup'].apply(lambda x: x.strip().title())



#////////////////////////////////////////////////////////////////Starting of Session 2 (Overall ANalysis)
# Loading the Data Of Overall 2nd Session
def overall_analysis():
  st.subheader("Highest Funded Companies in India")
  fig,ax=plt.subplots(figsize=(8,8))
  ax=sns.barplot(df.groupby("startup")['amount'].sum().sort_values(ascending=False).reset_index().head(10),x='startup',y='amount',hue='startup',linewidth=2,edgecolor='red')

  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.xlabel("Amount In Cr")
  plt.ylabel("Company Names")
  plt.title("Top 10 Funded Companies(Startup)")

  for i in ax.patches:
    height=i.get_height()
    ax.text(
        i.get_x()+i.get_width()/2,
        height,
        f'{height:.0f}cr',
        va='bottom',ha='center',
        fontsize=11
    )
  st.pyplot(fig)
  st.subheader("Top 10 Investors ")
  df_for_investor=df.copy()
  df_for_investor['investor']=df_for_investor['investor'].str.split(",")
  df_for_investor['Investor_num']=df_for_investor['investor'].apply(len)
  df_for_investor['amount_per_investor']=df_for_investor['amount']/ df_for_investor['Investor_num']
  df_for_investor=df_for_investor.explode('investor')
  
  requirement=df_for_investor.groupby("investor")['amount_per_investor'].sum().sort_values(ascending=False)
  top_10_inverstors=pd.DataFrame(requirement.head(10))
  fig,ax=plt.subplots(figsize=(8,8))
  ax=sns.barplot(data=top_10_inverstors,edgecolor='red',linewidth=3,x='investor',y='amount_per_investor',hue='investor')

  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.xlabel("Amount In Cr")
  plt.ylabel("Investor Names")
  plt.title("Top 10 Investors ")

  for i in ax.patches:
    height=i.get_height()
    ax.text(
        i.get_x()+i.get_width()/2,
        height,
        f'{height:.0f}cr',
        va='bottom',ha='center',
        fontsize=11
    )
  st.pyplot(fig)
  st.subheader("Top 10 sectors (vertical) receiving the most funding.")
  fig,ax=plt.subplots(figsize=(8,8))
  ax=sns.barplot(df.groupby("vertical")['amount'].sum().sort_values(ascending=False).reset_index().head(10),x='vertical',y='amount',hue='vertical',linewidth=2,edgecolor='red')

  plt.xticks(rotation=90)
  plt.tight_layout()
  plt.xlabel("Sectors")
  plt.ylabel("Amount in Cr")
  plt.title("Top 10 Investors ")

  for i in ax.patches:
    height=i.get_height()
    ax.text(
        i.get_x()+i.get_width()/2,
        height,
        f'{height:.0f}cr',
        va='bottom',ha='center',
        fontsize=11
    )
  st.pyplot(fig)

  
  st.header("Monthly Investment Trends")
  selected=st.selectbox("Select Option",['Total Funding Amount per Month',"Number of Funding Deals per Month"])

  month_analysis=df.copy()
  month_analysis['Date']=pd.to_datetime(month_analysis['Date'],format='%Y-%m-%d')
  month_analysis['month']=month_analysis['Date'].dt.month
  month_analysis['year']=month_analysis['Date'].dt.year
  
  if selected=='Total Funding Amount per Month':
      st.subheader("Total Funding Amount per Month")
      st.write("This chart displays the total investment amount startups received each month, grouped by year.")

      
      fig,ax=plt.subplots(figsize=(16,5))
      ax=month_analysis.groupby(['year','month'])['amount'].sum().plot()
      st.pyplot(fig)
  elif selected=='Number of Funding Deals per Month':
      st.subheader("Number of Funding Deals per Month")
      st.write("This chart shows how frequently (Counts) startups received funding each month, grouped by year.")

      fig,ax=plt.subplots(figsize=(16,5))
      ax=month_analysis.groupby(['year','month'])['amount'].count().plot()
      st.pyplot(fig)

        
  st.markdown("### Total Invested Amount In India Startups")
  st.markdown(f"""
            <div style ='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
              '>
                    {df['amount'].sum():.4f} Cr
                      </div>""",unsafe_allow_html=True)
  st.markdown("### Average Invested Amount In India Startups")
  st.markdown(f"""
            <div style ='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
              '>
                    {df.groupby("startup")['amount'].sum().mean():.4f} Cr
                      </div>""",unsafe_allow_html=True)
# ////////////////////////////////////////////////////////////////////////////////////////////End Of Session 4 (Investor) 


#////////////////////////////////////////////////////////////////Starting of Session 3 (Startups)
# Loading the Data Of Startups 3th Session
def load_startup_Details(startup):
  st.header("Sartups Details : ")
  st.markdown(f"""
        <div style='
            background-color: #1f1f1f;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-size: 24px;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        '>
            {startup}
        </div>
    """, unsafe_allow_html=True)
  st.subheader("Most Recent Fundings")
  startup_details=df[df['amount']!=0][df['startup']==startup].sort_values(by='Date').reset_index()
  st.dataframe(startup_details.loc[:,['Date','startup','city','vertical','investor','amount']])
  startup_details['cleaned_investor']=startup_details['investor'].str.split(",")
  startup_details['Investor_no']=startup_details['cleaned_investor'].apply(len)
  startup_details['Amount_per_investor']=startup_details['amount']/startup_details['Investor_no']
  particular_startup=startup_details.explode("cleaned_investor").sort_values(by='Amount_per_investor',ascending=False).head(10)
  def bar_chart():
        
        # Required Information 
        # First chart of Highest Fundings
        st.subheader("Top Investors Invested In Startup")
        st.success("Note: We Are Assuming Group Investors Invest Equal Amount in Startups")
        
        fig=plt.figure(figsize=(10,5))
        
        
        ax=sns.barplot(data=particular_startup,x='cleaned_investor',y='Amount_per_investor',hue='cleaned_investor',linewidth=2,edgecolor='red')
        ax.set_xlabel('Investor Name')
        ax.set_ylabel('Amount In Cr')
        ax.set_title(f'Investors Invested in {startup}',fontsize=30)
        for i in ax.patches:
            height=i.get_height()
            ax.text(
            i.get_x() + i.get_width()/2 ,
            height + 0.01*height,
            f'{height:.2f}Cr',
            fontsize=10,
            color='black',
            ha='center',
            va='bottom'
        )
        plt.xticks(rotation=30)
        st.pyplot(fig)
    
  try:
    bar_chart()
  except Exception as e:
    print("No Data FOund",e)
 
  st.header("Year Wise Analysis")
  particular_startup['Date']=pd.to_datetime(particular_startup['Date'],format='%Y-%m-%d')
  particular_startup['Year']=particular_startup['Date'].dt.year
  year_wise=particular_startup.groupby('Year')["amount"].sum()
 
  st.dataframe(year_wise.apply(lambda x:f"{x:.3f} Cr"))
  st.line_chart(particular_startup.groupby('Year')["amount"].sum())
 

  most_invested_year=year_wise[year_wise==year_wise.max()].index[0]
  st.success(f"Year with the highest investment: {most_invested_year}")
    
  st.header("Key Analysis About Startup")
  highest_investment= startup_details['amount'].max()
  sector=startup_details.groupby("vertical")['amount'].sum().sort_values(ascending=False).index[0]
  Citywise_group=startup_details.groupby("city")['amount'].sum().sort_values(ascending=False)
  if highest_investment>0:
        st.markdown("### Highest Investment Amount")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                ₹ {highest_investment:.6f} Crore
            </div>
        """, unsafe_allow_html=True)
        st.markdown("### Most Invested Startup Sector")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {sector} 
            </div>
        """, unsafe_allow_html=True)
        st.markdown("### Highest Invested Startup City")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {Citywise_group.index[0]} 
            </div>
        """, unsafe_allow_html=True)
        st.markdown("### Highest Invested Year")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {most_invested_year} 
            </div>
        """, unsafe_allow_html=True)
  else:
        st.markdown(f"""
            <div style ='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
              '>
                      No Investment Records
                      </div>""",unsafe_allow_html=True)
        st.markdown("### Highest Investment")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                Record Not Present
            </div>
        """, unsafe_allow_html=True)

# ////////////////////////////////////////////////////////////////////////////////////////////End Of Session 3 Startups) 





#////////////////////////////////////////////////////////////////Starting of Session 4 (investor)
# Loading the Data Of INvester 4th Session
def load_investor_Details(investor):
  st.header("Investor Details : ")
  st.markdown(f"""
        <div style='
            background-color: #1f1f1f;
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-size: 24px;
            font-weight: bold;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        '>
            {investor}
        </div>
    """, unsafe_allow_html=True)


  investor_details=df[df['investor'].str.contains(investor)].loc[:,['Date','startup','city','investor','amount']].sort_values(by='Date',ascending=False)

  investor_update=investor_details.copy()
  investor_update['amount']=investor_update['amount'].apply(lambda x:f"{x} Cr")
  st.subheader("Most Recent Investments")
  st.dataframe(investor_update.reset_index(drop=True))
  
  st.header("Investment Details")
  def bar_chart():
    # Required Information 
    startup_wiseGroup=investor_details.groupby("startup")['amount'].sum().sort_values(ascending=False)
    funding_wiseGroup=df[df['investor'].str.contains(investor)].groupby('round')['amount'].sum().sort_values(ascending=False)
    Citywise_group=df[df['investor'].str.contains(investor)].groupby("city")['amount'].sum().sort_values(ascending=False)
    Sector_wiseGroup=df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum().sort_values(ascending=False)

  # First chart of Highest Investment
    col1,col2=st.columns(2)
    with col1:
     st.subheader("highest Investments")
    #  st.dataframe(startup_wiseGroup.apply(lambda x : f"{x} Cr"))
     
     fig=plt.figure(figsize=(10,9))
     x=startup_wiseGroup.head(10).reset_index()
     x.columns=['A','B']
     ax=sns.barplot(x,x='A',y='B',hue="A",linewidth=2,edgecolor='red')
     ax.set_xlabel('Amount In Crore')
     ax.set_ylabel('Starups Name')
     ax.set_title("Top Investments",fontsize=30)
     for i in ax.patches:
      height=i.get_height()
      ax.text(
          i.get_x() + i.get_width()/2 ,
          height + 0.01*height,
          f'{height:.2f}Cr',
          fontsize=10,
          color='black',
          ha='center',
          va='bottom'
      )
     plt.xticks(rotation=30)
     st.pyplot(fig)




     
    # second Chart of Funding Round
     st.subheader(f"Funding Round of Invester")
    #  st.dataframe(funding_wiseGroup)
     # for Investor Round 
     if not (funding_wiseGroup.empty):
        fig=plt.figure(figsize=(10,15))
        funding_wiseGroup.head(4).plot(
          kind='pie',autopct=lambda p:'{:.0f}%'.format(p) if p>0 else '',textprops={'fontsize': 18})
        plt.ylabel("")
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)
     else:
       pass
     

    with col2:
      # third Chart of Sector wise
      st.subheader("Sector-Wise Investments")
      # st.dataframe(df[df['investor'].str.contains(investor)].groupby("vertical")['amount'].sum().sort_values(ascending=False).apply(lambda x:f"{x} Cr"))
      
      
      fig,ax=plt.subplots(figsize=(10,9))  # Increase the figure size
      plt.title("Sector-wise Investment ", fontsize=20)  # Add a title with larger font size

      if not Sector_wiseGroup.empty:

      # Plot the pie chart with better spacing and larger font sizes
          Sector_wiseGroup.head(3).plot(
              kind='pie',
              autopct=lambda p: '{:.0f}%'.format(p) if p>0 else "",
              textprops={'fontsize': 20},  
              startangle=90,  
              wedgeprops={'linewidth': 1, 'edgecolor': 'black'}  
          )

          plt.ylabel('')  # Remove the default y-axis label
          plt.tight_layout() 
          st.pyplot(fig)
      else:
        st.write("No data available to display the bar chart!")



      # Fourth Chart of City wise
      if not Citywise_group.empty:
        st.subheader("City-Wise Investments")
        # st.dataframe(Citywise_group.apply(lambda x:f"{x} Cr"))
      
        fig,ax=plt.subplots(figsize=(10,9))  # Increase the figure size
        plt.title("City-wise Investment ", fontsize=20)  # Add a title with larger font size
        # Plot the pie chart with better spacing and larger font sizes
        Citywise_group.head(3).plot(
            kind='pie',
            autopct=lambda p: '{:.0f}%'.format(p) if p>0 else "",
            textprops={'fontsize': 20},  
            startangle=90,  
            wedgeprops={'linewidth': 1, 'edgecolor': 'black'}  
        )

        plt.ylabel('')  # Remove the default y-axis label
        plt.tight_layout() 
        st.pyplot(fig)
      else:
        st.info("No Citywise Data Available!")


    st.header("Year Wise Analysis")
    df['Date']=pd.to_datetime(df['Date'],format='%Y-%m-%d')
    date_wise_investor=df[df['investor'].str.contains(investor)].sort_values(by='Date')
    date_wise_investor['Year']=date_wise_investor['Date'].dt.year
    st.dataframe(date_wise_investor.groupby('Year')['amount'].sum().apply(lambda x:f"{x:.3f} Cr").reset_index())
    st.line_chart(date_wise_investor.groupby('Year')['amount'].sum())
    most_invested_year=date_wise_investor.groupby('Year')['amount'].sum().sort_values(ascending=False).index[0]
    st.success(f"Year with the highest investment: {most_invested_year}")

    st.header("Key Analysis About Investor")
    highest_investment=investor_details.groupby('startup')['amount'].sum().sort_values(ascending=False).iloc[0]
    investment=investor_details.groupby('startup')['amount'].sum().sort_values(ascending=False).index[0]
    sector=df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum().sort_values(ascending=False).index[0]
    if highest_investment>0:
        st.markdown("### Highest Startup Investment ")
        st.markdown(f"""
            <div style ='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
              '>
                    {investment}
                      </div>""",unsafe_allow_html=True)
        st.markdown("### Highest Investment Amount")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                ₹ {highest_investment:.6f} Crore
            </div>
        """, unsafe_allow_html=True)
        st.markdown("### Highest Invested Sector")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {sector} 
            </div>
        """, unsafe_allow_html=True)
        st.markdown("### Highest Invested City")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {Citywise_group.index[0]} 
            </div>
        """, unsafe_allow_html=True)
        st.markdown("### Investor Contribution Type")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {funding_wiseGroup.index[0]} 
            </div>
        """, unsafe_allow_html=True)
        st.markdown("### Highest Invested Year")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                {most_invested_year} 
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style ='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
              '>
                      No Investment Records
                      </div>""",unsafe_allow_html=True)
        st.markdown("### Highest Investment")
        st.markdown(f"""
            <div style='
                background-color: #1f1f1f;
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                color: white;
                font-size: 24px;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            '>
                Record Not Present
            </div>
        """, unsafe_allow_html=True)

    st.header("Similar Investors")
    similar_criteria=df[(df['city']==Citywise_group.index[0]) & (df['vertical']==sector ) & df['amount']!=0].sort_values(by="amount",ascending=False).reset_index(drop=True)
    
    if not similar_criteria.empty:
        st.dataframe(similar_criteria[['investor', 'startup', 'city', 'vertical','amount']].head())
        
    else:
        st.warning("No similar investors found based on city and sector.") 
  try:
   bar_chart()
  except Exception as e:
    st.info(f" Investor Data Not Found ")

def bar_chart1():
  col1,col2=st.columns(2)
  Startup_10=df.groupby("startup")['amount'].sum().sort_values(ascending=False)
  with col1:   
    st.header("Top 5 Startups (in crore)")
    st.bar_chart(data=Startup_10.head())
  with col2:
   st.header("Details")
   top_10_investors['amount_per_investor']=top_10_investors['amount_per_investor'].apply(lambda x: f"{x} crore")
   st.dataframe(Startup_10.head())

def bar_chart2():
 col1,col2=st.columns(2)
 Startup_10=df[df['amount']!=0].groupby("startup")['amount'].sum().sort_values()
 with col1:
    st.header("Least 5 Startups (in crore)")
    st.bar_chart(data=Startup_10.head())
 with col2: 
  st.header("Details")
  least_10['amount_per_investor']=least_10['amount_per_investor'].apply(lambda x: f"{x:.5f} crore")
  st.dataframe(Startup_10.head())

def bar_chart3():
  col1,col2=st.columns(2)
  with col1:
    
    st.header("Top 5 Investor (in crore)")
    st.bar_chart(data=top_10_investors)
  with col2:
   
   st.header("Details")
   top_10_investors['amount_per_investor']=top_10_investors['amount_per_investor'].apply(lambda x: f"{x} crore")
   st.dataframe(top_10_investors)

def bar_chart4():
 col1,col2=st.columns(2)
 with col1:
    st.header("Least 5 Investor (in crore)")
    st.bar_chart(data=least_10)
 with col2: 
  st.header("Details")
  least_10['amount_per_investor']=least_10['amount_per_investor'].apply(lambda x: f"{x:.5f} crore")
  st.dataframe(least_10)


# ////////////////////////////////////////////////////////////////////////////////////////////End Of Session 4 (Investor) 


# main session

st.markdown(
    """
    <style>
        [data-testid="stSidebarUserContent"] {
            padding-top: 0rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
#sidebar
with st.sidebar:
    st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
    <h3 style="
        text-align:center;
        font-size: 40px;
        font-family: 'Pacifico', cursive;
        background: linear-gradient(to right, green, yellow, orange, red, pink, blue);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: normal;
        ">
        Welcome
    </h1>
    """,
    unsafe_allow_html=True
)
    Option = option_menu(
        menu_title="Menu",
        options=["Data Overview", "Overall Analysis", "Startup", "Investor"],
        icons=["table", "bar-chart", "rocket", "person"],
        menu_icon="list",
        default_index=0,
        styles={
            "container": {"background-color": "#0e1117"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {
                "color": "white",
                "font-size": "18px",
                "text-align": "left",
                "margin": "5px"
            },
            "nav-link-selected": {"background-color": "#ff4b4b"},
        }
    )
    
st.markdown("""
<style>
div[data-baseweb="select"] > div {
    background-color: #1e1e1e;  /* Match your sidebar background */
    color: white;
    border-radius: 8px;
    border: 1px solid #555;
}
div[data-baseweb="select"] svg {
    fill: white; /* Dropdown arrow color */
}
</style>
""", unsafe_allow_html=True)



# According to sidebar selection
# First data Overview Session
if Option.lower()=='data overview':
 st.title("Startup Funding Analysis")
 st.header("Data OverView")
 st.dataframe(df)
 st.subheader("About the Dataset")
 st.write(""" Startup Funding in India
This dataset, titled "startup_funding.csv," gives a real-world look into how startups in India have been funded over the years. It includes 2,372 records, each capturing key details like:
            When the funding happened,The name of the startup,What industry and sub-industry it's in,The city it's based in,Who invested in it,The type of investment,How much funding was raised (in USD),And any extra notes

""")
 st.write("""Startups in the data come from a wide range of industries—from tech and consumer internet to more niche areas like digital marketing agencies and predictive care platforms. Most of the funding activity is centered around big cities like Bangalore, Mumbai, and New Delhi, which isn’t surprising since they’re known as startup hubs.The types of investment vary, with a lot of activity around seed funding and private equity. The investors listed include both individuals and major firms, showing how diverse the Indian startup investment scene is.It’s also worth noting that some entries are incomplete—especially in the AmountInUSD column. That could mean the amount wasn’t disclosed or just wasn’t recorded.

In short, this dataset is a solid starting point for understanding how startups in India are being funded—where the money's going, who’s investing, and what kinds of businesses are getting backed.
""")

# Overall Analysis Session
elif Option.lower()=='overall analysis':
 st.title("Overall Analysis")
 overall_analysis()




# Startup  Infromation SEssion
elif Option.lower()=='startup':


 x=list(df['startup'].sort_values().unique())
 x.append(x[0])
 x[0]="Default View"
 selected=st.sidebar.selectbox("Select Startup",x)  
     
 but1=st.sidebar.button("Find Startup Details ")
 
 if selected=='Default View':
     st.title("Startup Analysis")
     bar_chart1()
     bar_chart2()

 # on pressing button Further work
 else:
    if selected or but1:
        load_startup_Details(selected)




# investor Analysis Session
elif Option.lower()=='investor':


 x=sorted(set(df['investor'].str.split(',').sum()))
 x[0]='Default Analysis'
 investor_Selected=st.sidebar.selectbox("Select Investor",x)

 but2=st.sidebar.button("Find investor Details")


 
 # on pressing button 
 def display(investor_Selected):
  if investor_Selected=='Default Analysis':
    st.title("investors Analysis")
    st.toast(f"Select the Investor and Press the Button For Details", icon="🎈")
    bar_chart3()
    
    bar_chart4()
  else:
    if investor_Selected or but2:
      load_investor_Details(investor_Selected)
 display(investor_Selected)
    

   
