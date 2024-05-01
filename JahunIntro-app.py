# Buiilding a simple website in 12 mins with Streamlit via youtube https://www.youtube.com/watch?v=VqgUkExPvLY
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Setting the page config
st.set_page_config(page_title="Hello World!", 
                   page_icon=":nerd:", 
                   layout="wide",) 
# function to load animation using lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ---- Load animation ----
lottie_file = load_lottieurl("https://lottie.host/406ad3c8-313f-4425-b072-c7638580bed2/qIBM5r7C5c.json")
# ---- LOAD pictures ----
img_contract_form = Image.open("Images/Pychain.png")
img_famechain = Image.open("Images/famechain.png")
img_kasei = Image.open("Images/KaseiCoin.png")
img_kryptojobs = Image.open("Images/kryptojobs.png")
img_algospy = Image.open("Images/algospy.png")
img_venture = Image.open("Images/venturefunding.png")
img_tradebot = Image.open("Images/tradebot.png")
img_finacialplanning = Image.open("Images/financialplanning.png")
img_investinspect = Image.open("Images/investinspect.png")
img_rental = Image.open("Images/rental.png")
#img_lottie_animation = Image.open("Images/")

# Create a basic layout of the webapp and define the pages
def main():
    # creating a navigation bar on the left side of the webapp
    st.sidebar.title("Where to?")
    page = st.sidebar.radio("Go to", ("Welcome", "BlockChain Develpoment","Machine Learning / AI","Financial and Quantitative Analyst"))
    # defining the pages
    if page == "Welcome":
        welcome_page()
    elif page == "BlockChain Develpoment":
        blockchain_development_page()
    elif page == "Machine Learning / AI":
        machine_learning_ai_page()
    elif page == "Financial and Quantitative Analyst":
        financial_quantitive_analyst_page()

# ---- What I do in more detail ----
def welcome_page():
    # ---- Header Section ----
    with st.container():
        st.subheader("Hi, I am Jahun :wave:")
        st.title("Jr. Blockchain Developer from the Bluebonnet plains of Texas!")
        st.markdown("### I am passionate about learning all things Crypto/ Blockchain and Web3.")
        st.write("[Learn more about any of my past projects here. -->](https://github.com/Jahunm)")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        # ---- Left Column ----
        with left_column:
            st.header("What this is about")
            st.write("##")
            st.markdown(
                """**Welcome to my journey!** :rocket:

I'm thrilled you've stopped by to join me on this exciting voyage towards becoming a **Jr. Blockchain Developer** and **Web Developer**. My adventure began with a rigorous 6-month FinTech Bootcamp at SMU in Dallas, Texas, where I honed my skills in the intricate world of finance and technology.
But why stop there? I'm currently expanding my horizons at **HarvardX**, diving deep into the realms of **Artificial Intelligence** and **Blockchain technologies** through HyperLedger. Yes, it's a vast ocean of knowledge, and becoming a Full-stack developer is no small feat. But I'm committed to learning and growing every step of the way.
Though my quest has just begun, I'm already captivated by the endless possibilities that lie ahead. Each challenge I overcome is a triumph, a testament to the joy of mastering new skills.
Curious about my progress? Check out my **GitHub portfolio** in the link above, showcasing a collection of projects that mark my milestones. Your feedback is not just welcome—it's invaluable. As a newcomer to this field, my passion for learning is boundless, and I eagerly anticipate every new discovery.
Join me, and let's explore the future of technology together!

                """
            )
            st.write("[Github ->](https://github.com/Jahunm)")
        with st.container():
            st.write("---")
            st.header("Get In Touch With Me!")
            st.markdown("[LinkedIn Profile](www.linkedin.com/in/jahunm)")
        # ---- Right Column ----
        with right_column:
            st_lottie(lottie_file, height=300, key="file")
    
# ---- PROJECTS ~ use your top 3 ----
def blockchain_development_page():
    with st.container():
        st.write("---")
        st.header("My Blockchain Projects")
        st.write("##")
        # Project 1
        image_column, text_column = st.columns((1,2))    

        with image_column:
            st.image(img_famechain)
        with text_column:
            st.subheader("FameChain Ballot - Decentralized Voting system")
            st.write(
                '''
                Here is my capstone project for my final grade at SMU. I created a complete full-stack Dapp, using remix and solidity for the smart contract. 
                Deployed using Ganache as the blockchain to test. Python was used as backend using Web3 and Streamlit to deploy the Front-end interactive dApp.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/FameChain_dApp)")
        # Project 2
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))    

        with image_column:
            st.image(img_kasei)
        with text_column:
            st.subheader("Using Solidity smart contracts to create a crowdsale to fund the Martian Token ~ KaseiCoin")
            st.write(
                '''
                This was a really fun project, I thought. A new cryptocurrency designed for the burgeoning Martian economy and backed by a global collaboration. 
                This ERC-20 compliant token is launched through a crowdsale, inviting future Martians to invest in the Red Planet’s economy. 
                The initiative is supported by three smart contracts developed using Solidity and the Remix IDE, demonstrating the project’s viability with evidence from the entire crowdsale process.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/KaseiCoin_Martian_Token_Crowdsale)")
        # Project 3
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))    

        with image_column:
            st.image(img_kryptojobs) 
        with text_column:
            st.subheader("KryptoJobs2Go")
            st.write(
                '''
                KryptoJobs2Go is developed using Python for its flexibility and extensive libraries suitable for web and blockchain development. 
                The platform utilizes Ganache for simulating Ethereum blockchain transactions, Web3.js for smart contract interaction, 
                and Streamlit to build an interactive interface for user transactions and navigation.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/KryptoJobs2Go/tree/main)")


def machine_learning_ai_page():
    with st.container():
        st.write("---")
        st.header("My Machince Learning Projects")
        st.write("##")
        # Project 1
        image_column, text_column = st.columns((1,2))    
        with image_column:
            st.image(img_algospy)
        with text_column:
            st.subheader("Algorithmic Spy")
            st.write(
                '''
                As a team for a group project we created an algorithmic trading bot, trading the SPY. 
                Algorithmic Spy is a program used to explore several models to determine which algorithmic trading model has better accuracy. 
                In this case, we will use Neural Networks, Prophet, and SGDRegressor functions to determine whether to Sell or Buy the stock with a trading bot.
                We used Alpaca API to make live buy and sell orders as soon as the AlgoBot made the decision to do so. Needs more tweaking to be profitable.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/AlgorithmicSpy/tree/main)")
        # Project 2
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))    

        with image_column:
            st.image(img_venture)
        with text_column:
            st.subheader("Venture Funding with Deep Learning")
            st.write(
                '''
                In this project I was tasked using deep learning tools to develope a predictive model to assess the success potential of startups seeking funding. 
                Utilizing a dataset of over 34,000 previously funded organizations, you employ machine learning and neural networks to create a binary classifier. 
                This model will analyze various data points to predict the likelihood of an applicant’s business success.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/Venture_funding_with_deep_learning/tree/main)")
        st.write("---")
        # Project 3
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))    

        with image_column:
            st.image(img_tradebot) 
        with text_column:
            st.subheader("Machine Learning Trading Bot")
            st.write(
                '''
                This project evaluates a machine learning trading bot, testing various configurations and models to enhance algorithmic trading. 
                The most effective model used a 50-day low and 100-day high Simple Moving Average (SMA) with a 3-month training window, outperforming others in strategy returns. 
                The Support Vector Machine (SVM) classifier consistently delivered the best results, with longer SMA durations proving more accurate than shorter ones.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/machine_learning_trading_bot)")
       
def financial_quantitive_analyst_page():
    with st.container():
        st.write("---")
        st.header("Quantitive and Data analysis for financial innovation")
        st.write("##")
        # Project 1
        image_column, text_column = st.columns((1,2))    
        with image_column:
            st.image(img_investinspect)
        with text_column:
            st.subheader("InvestInspect")
            st.write(
                '''
                InvestInspect is a comprehensive financial analysis application that uses Python’s yfinance library to help users optimize their stock performance. 
                It provides a GUI (kTinker) for users to input stock symbols and share amounts, and offers a range of analytical tools. 
                These include calculating portfolio allocation, tracking daily and cumulative returns against market benchmarks, analyzing expected annual returns versus risks, and evaluating portfolio efficiency with Sharpe ratios. The application also uses a correlation matrix to understand asset interdependence and diversification benefits, and employs Monte Carlo simulation to predict long-term investment performance. This robust toolset aids users in making informed and confident investment decisions.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/InvestInspect)")
        # Project 2
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))    

        with image_column:
            st.image(img_finacialplanning)
        with text_column:
            st.subheader("Financial Planning with Monte Carlo Simulation")
            st.write(
                '''
                The program is a personal finance planner that manages crypto assets and investments in stocks and bonds, performs savings health analysis, and retirement planning. 
                It fetches current prices of Bitcoin and Ethereum, computes the portfolio value, and uses the Alpaca API to fetch current closing prices for SPY and AGG. 
                It analyzes savings health by creating a DataFrame to store the total value of crypto assets and shares, and validates if the savings are enough for an emergency fund. 
                For retirement planning, it fetches historical closing prices for a retirement portfolio and uses the MCForecastTools toolkit to create Monte Carlo simulations to project the portfolio performance at 30 years. It also provides an option to adjust the retirement plan for an earlier retirement by either including more risk or having a larger initial investment.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/financial_planning)")
        st.write("---")
        # Project 3
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1,2))    

        with image_column:
            st.image(img_rental) 
        with text_column:
            st.subheader("San Francisco Housing Rental Analysis")
            st.write(
                '''
                The program is a comprehensive data analysis tool that uses Python libraries to analyze housing trends. 
                It groups data by year and plots housing units as a bar chart, showing a steady increase from 2010 to 2016. 
                It calculates and plots average prices per square foot, revealing a drop in price but an increase in gross rent from 2010 to 2011. 
                The program also compares average prices by neighborhood, showing a drop in the average sale price per square foot for the Anza Vista neighborhood from 2012 to 2016. It builds an interactive neighborhood map, indicating that Merced Heights had the highest gross rent and Union Square District was the most expensive neighborhood to purchase per square foot. 
                The program suggests that it is more profitable to buy homes in less expensive neighborhoods for a higher ROI.
                '''
            )
            st.markdown("[Link to the Github Repo...],(https://github.com/Jahunm/whale_portfolio)")       
        # ---- CONTACT INFO ----
        

# call our function
if __name__ == "__main__":
    main()
            
