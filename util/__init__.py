
# pip install selenium
# pip install -U user_agent
# pip install user-agents
# pip install webdriver_manager
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
from user_agents import parse
from selenium import webdriver  # 자동화 툴
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tqdm import tqdm
import time  # 시간 지연
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import random


__all__={
    "pd","warnings","By","chrome_driver",
    "Service","webdriver","parse","generate_user_agent",
    "BeautifulSoup","tqdm","random"
}