
growth_data = """

"Ticker","Company","Sustainable Growth Rate","Sales QoQ Chg.","Eps QoQ Chg.","Sales Growth Next Year","EPS Next Year Chg (Est.%)","5-Year EPS Growth Estimate","Sales 1-Year Chg (%)","Sales 3-Year Avg (%)","Sales 5-Year Avg (%)","Sales 10-Year Avg (%)","EPS 1-Year Chg (%)","EPS 3-Year Avg (%)","EPS 5-Year Avg (%)","EPS 10-Year Avg (%)"
"ACAD","ACADIA Pharmaceuticals","-45.9%","4.4%","- ","21.2%","- ","25.0%","6.8%","15.1%","32.8%","59.3%","- ","- ","- ","- "
"APTV","Aptiv","6.0%","12.2%","1333.3%","12.5%","42.5%","34.3%","12.0%","6.8%","6.3%","1.2%","1.0%","-20.1%","-12.4%","-5.2%"
"AXTA","Axalta Coating Sys","13.2%","8.8%","-13.0%","3.9%","23.0%","9.2%","10.6%","2.9%","2.2%","- ","-24.6%","-6.7%","41.8%","- "
"BAM","Brookfield Asset Mgmt","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- "
"BG","Bunge","13.8%","-0.1%","45.4%","-2.8%","-6.6%","-5.4%","13.7%","17.8%","8.0%","1.0%","-22.9%","- ","63.8%","15.4%"
"BLMN","Bloomin Brands","19.3%","4.6%","3.4%","1.9%","6.1%","7.7%","7.1%","2.2%","0.9%","1.0%","-48.5%","-10.8%","0.2%","8.9%"
"BRK.B","Berkshire Hathaway","-4.7%","-17.6%","-53.3%","8.8%","12.9%","23.3%","-34.0%","-10.5%","-0.7%","3.7%","- ","- ","- ","- "
"BYND","Beyond Meat","179.9%","-20.6%","- ","11.0%","- ","10.0%","-9.8%","12.0%","- ","- ","- ","- ","- ","- "
"CARR","Carrier Global","37.0%","-0.5%","-11.1%","3.8%","10.9%","14.0%","-0.9%","3.1%","- ","- ","119.3%","26.4%","- ","- "
"CFLT","Confluent","-55.9%","40.6%","- ","28.4%","- ","100.1%","51.1%","- ","- ","- ","- ","- ","- ","- "
"CHRW","C.H. Robinson Worldwide","48.5%","-22.1%","-54.0%","2.3%","11.6%","1.0%","6.9%","17.2%","10.7%","8.1%","17.3%","20.8%","15.7%","7.3%"
"COIN","Coinbase Glb","-44.3%","-74.8%","- ","57.0%","- ","- ","-59.3%","- ","- ","- ","- ","- ","- ","- "
"CP","Canadian Pacific Railway","7.7%","20.7%","83.8%","10.3%","14.9%","9.0%","10.2%","4.2%","6.1%","4.5%","-9.8%","2.5%","2.8%","21.0%"
"CTLT","Catalent","8.3%","-5.6%","-15.4%","6.6%","11.4%","7.2%","6.1%","20.3%","15.6%","- ","-29.8%","39.4%","32.4%","- "
"DKS","Dick's Sporting Goods","35.3%","7.3%","-17.7%","2.0%","3.9%","5.9%","0.6%","12.2%","7.6%","7.8%","-22.3%","47.7%","29.0%","16.6%"
"DQ","Daqo New Energy","38.0%","108.2%","9.7%","-11.8%","-31.6%","74.9%","146.6%","127.5%","66.5%","47.1%","117.8%","275.0%","64.7%","- "
"EURN","Euronav","8.9%","137.3%","- ","9.5%","16.4%","-13.0%","43.9%","-12.9%","3.3%","6.5%","- ","- ","- ","- "
"EXPD","Expeditors Intl","36.6%","-36.2%","-48.1%","-3.8%","-6.4%","-18.3%","3.3%","27.8%","19.8%","11.0%","-0.1%","34.5%","25.1%","18.1%"
"FRO","Frontline","12.5%","122.4%","- ","-0.9%","-3.9%","-15.4%","48.6%","5.2%","11.5%","6.8%","- ","15.4%","- ","- "
"FTDR","Frontdoor","116.4%","0.3%","25.0%","7.6%","28.9%","13.3%","3.7%","6.8%","- ","- ","-42.0%","-21.5%","- ","- "
"HZNP","Horizon Therapeutics","10.3%","-7.1%","-28.8%","13.5%","23.6%","5.0%","12.5%","40.7%","28.0%","69.2%","-2.2%","-8.5%","- ","- "
"LAC","Lithium Americas","-14.7%","- ","- ","6333.8%","- ","- ","- ","- ","- ","- ","- ","- ","- ","- "
"LVS","Las Vegas Sands","47.2%","10.8%","- ","30.5%","97.8%","57.3%","-2.9%","-30.2%","-20.2%","-9.5%","- ","-10.2%","- ","- "
"MA","Mastercard","127.6%","11.5%","8.7%","13.6%","19.0%","19.5%","17.8%","9.6%","12.2%","11.6%","16.7%","8.8%","22.9%","16.6%"
"NKE","Nike","24.0%","17.2%","2.4%","7.3%","25.4%","8.6%","4.9%","6.0%","6.8%","6.7%","-6.6%","9.3%","26.8%","11.1%"
"NOW","ServiceNow","6.5%","20.2%","469.2%","22.0%","23.5%","23.7%","22.9%","27.9%","30.2%","40.4%","41.6%","-20.4%","- ","- "
"ROKU","Roku","-18.4%","0.2%","- ","16.1%","- ","43.0%","13.1%","40.3%","43.5%","- ","- ","- ","- ","- "
"RTX","Raytheon Technologies","2.8%","6.2%","108.7%","7.9%","16.2%","13.4%","4.2%","13.9%","2.3%","1.5%","36.0%","-4.6%","-9.2%","-4.1%"
"RVLV","Revolve Gr","15.5%","8.1%","-71.8%","14.3%","39.2%","-1.1%","23.6%","22.3%","- ","- ","-41.0%","- ","- ","- "
"SNN","Smith & Nephew","-2.0%","- ","- ","- ","- ","4.6%","0.1%","0.5%","1.8%","2.3%","-57.3%","-28.0%","-21.9%","-10.8%"
"SONO","Sonos","3.0%","1.2%","-34.5%","7.5%","181.3%","6.1%","1.4%","9.9%","- ","- ","-84.8%","- ","- ","- "
"STNG","Scorpio Tankers","24.5%","233.8%","- ","-10.9%","-35.5%","42.5%","189.0%","30.4%","25.0%","29.8%","- ","- ","- ","- "
"SYNH","Syneos Health","7.6%","-1.0%","-25.0%","2.2%","18.9%","0.3%","3.5%","4.9%","15.1%","- ","15.2%","27.3%","- ","- "
"T","AT&T","- ","0.8%","- ","1.2%","2.9%","0.8%","-9.9%","-12.6%","-5.5%","-0.5%","- ","- ","- ","- "
"TMO","Thermo Fisher Scientific","14.7%","7.0%","-3.8%","8.2%","12.7%","7.8%","14.5%","20.7%","16.5%","13.6%","-9.4%","24.3%","25.8%","17.8%"
"TSM","Taiwan Semiconductor","21.9%","47.9%","79.6%","21.5%","25.3%","21.5%","30.8%","24.7%","16.3%","15.1%","49.0%","35.5%","20.7%","18.7%"
"TWLO","Twilio","-11.6%","21.6%","- ","16.3%","51.6%","102.8%","34.6%","49.9%","57.1%","- ","- ","- ","- ","- "
"V","Visa","32.1%","12.4%","8.7%","11.1%","14.6%","15.5%","18.5%","8.7%","10.0%","10.9%","18.5%","9.3%","18.9%","23.0%"
"VRNS","Varonis Systems","-22.7%","12.7%","- ","10.6%","11.8%","46.8%","21.4%","23.0%","17.1%","- ","- ","- ","- ","- "
"VST","Vistra","- ","16.8%","- ","2.6%","14.2%","59.1%","13.7%","5.1%","20.4%","- ","- ","- ","- ","- "
"VXX","iPath Series B S&P 500 VIX Short-Term Futures ETN","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- "
"Z","Zillow Gr","-2.1%","-18.7%","- ","14.1%","69.5%","-21.0%","-8.2%","-10.6%","12.7%","32.5%","- ","- ","- ","- "
"Summary"," ","18.3%","18.2%","75.1%","172.1%","22.6%","19.4%","17.2%","14.7%","15.0%","15.3%","1.3%","19.4%","20.4%","11.0%"
"""

quick_valuation_data = """
"Ticker","Company","Price / Earnings","P/E Adjusted","EV / EBITDA","EV / FCF","Earnings Yield","Greenblatt Earnings Yield","Price to Graham Number","Price to Lynch Fair Value","Cash Return","Yacktman Forward RoR","Margin of Safety (EPV)","EPS","EPS Diluted","EPS Next Year (Est.)","EPS Next Year Chg (Est.%)","Forward P/E","PEG Forward","Shiller PE","Price / Sales","Price / Sales Industry Decile","Price / Book","Price / Book Industry Decile","Shareholder Yield"
"ACAD","ACADIA Pharmaceuticals","- ","- ","-12.1","- ","-7.2%","-8.4%","- ","- ","-4.2%","- ","- ","-$1.34","-$1.34","$0.05","- ","373.7","- ","- ","5.8","2","7.6","8","-0.3%"
"APTV","Aptiv","56.3","68.4","17.9","75.5","1.8%","3.4%","8.2","236.6","1.7%","0.1%","-400.3%","$1.96","$1.96","$6.27","42.5%","17.6","0.8","26.2","1.7","8","3.4","8","0.0%"
"AXTA","Axalta Coating Sys","34.3","65.1","13.7","66.8","2.9%","4.1%","- ","32.9","2.6%","8.5%","- ","$0.86","$0.86","$1.82","23.0%","16.2","2.2","47.3","1.3","6","4.5","8","3.1%"
"BAM","Brookfield Asset Mgmt","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","10","- ","10","4.0%"
"BG","Bunge","9.0","13.2","6.5","- ","11.1%","13.3%","0.8","- ","-30.5%","10.7%","- ","$10.83","$10.51","$11.04","-6.6%","8.6","- ","24.0","0.2","2","1.5","6","4.0%"
"BLMN","Bloomin Brands","24.7","178.0","11.0","23.9","4.1%","5.0%","- ","13.7","5.1%","17.5%","-15.6%","$1.15","$1.03","$3.12","6.1%","8.2","1.1","31.2","0.6","3","8.2","7","8.7%"
"BRK.B","Berkshire Hathaway","- ","- ","-49.3","34.8","-3.4%","-3.5%","- ","- ","3.4%","- ","- ","-$10.36","-$10.36","$17.79","12.9%","17.1","0.8","22.2","2.9","7","1.4","5","1.2%"
"BYND","Beyond Meat","- ","- ","-6.1","- ","-36.8%","-18.2%","0.8","- ","-20.7%","- ","- ","-$5.75","-$5.75","-$2.76","- ","- ","- ","- ","2.4","7","- ","9","0.0%"
"CARR","Carrier Global","11.0","13.1","8.7","31.5","9.1%","10.6%","- ","- ","3.8%","- ","-210.8%","$4.19","$4.10","$2.84","10.9%","15.9","1.3","- ","1.9","8","4.9","8","5.3%"
"CFLT","Confluent","- ","- ","-12.7","- ","-7.2%","-8.0%","- ","- ","-3.1%","- ","- ","-$1.62","-$1.62","$0.08","- ","281.1","- ","- ","10.8","8","8.6","7","0.0%"
"CHRW","C.H. Robinson Worldwide","13.1","16.1","9.8","8.9","7.7%","9.5%","- ","0.1","12.0%","14.7%","- ","$7.48","$7.40","$5.19","11.6%","18.6","22.0","22.4","0.5","4","8.3","9","15.5%"
"COIN","Coinbase Glb","- ","- ","-4.6","- ","-18.4%","-22.7%","- ","- ","-11.8%","- ","- ","-$11.81","-$11.83","-$0.01","- ","- ","- ","- ","4.5","3","2.7","4","0.0%"
"CP","Canadian Pacific Railway","27.4","34.5","20.3","45.3","3.7%","4.2%","1.7","- ","2.7%","7.6%","-461.1%","$2.73","$2.72","$3.77","14.9%","20.0","2.6","37.5","10.9","10","2.5","7","0.7%"
"CTLT","Catalent","28.2","46.2","15.2","- ","3.6%","4.1%","4.7","0.5","-1.5%","18.6%","- ","$2.28","$2.28","$3.52","11.4%","18.2","2.5","45.9","2.4","6","2.4","6","0.0%"
"DKS","Dick's Sporting Goods","12.7","15.9","7.8","26.1","7.9%","10.2%","1.7","0.4","4.5%","24.4%","-87.2%","$13.43","$10.78","$13.97","3.9%","9.8","1.7","27.3","1.1","6","4.7","7","5.7%"
"DQ","Daqo New Energy","2.0","1.0","1.3","1.4","50.9%","76.2%","0.3","1.0","71.2%","25.1%","48.3%","$21.69","$21.24","$11.84","-31.6%","4.0","0.0","13.3","0.8","2","0.7","1","0.0%"
"EURN","Euronav","16.5","34.6","23.0","- ","6.1%","-0.8%","- ","- ","-3.1%","- ","- ","-$0.52","-$0.52","$2.62","16.4%","6.3","- ","70.3","3.9","8","1.5","4","0.7%"
"EXPD","Expeditors Intl","13.0","11.7","7.8","7.2","7.7%","12.4%","1.8","- ","13.9%","23.6%","-57.8%","$8.33","$8.26","$5.12","-6.4%","20.9","- ","27.0","1.0","7","5.3","8","10.3%"
"FRO","Frontline","7.4","16.5","11.4","109.8","13.6%","6.0%","1.0","- ","2.7%","12.3%","- ","$1.20","$1.20","$2.46","-3.9%","6.6","- ","- ","2.4","6","1.6","4","24.9%"
"FTDR","Frontdoor","31.3","36.3","16.5","25.2","3.2%","4.8%","- ","- ","5.0%","- ","-25.9%","$0.87","$0.87","$1.65","28.9%","16.5","1.6","- ","1.3","4","36.5","7","2.7%"
"HZNP","Horizon Therapeutics","49.1","49.4","25.3","22.3","2.0%","2.4%","9.6","- ","4.8%","- ","- ","$2.28","$2.22","$6.59","23.6%","16.6","4.3","- ","7.1","9","4.9","7","1.0%"
"LAC","Lithium Americas","- ","- ","-41.9","- ","-3.3%","-2.4%","- ","- ","-1.7%","- ","- ","-$0.70","-$0.70","$0.87","- ","24.5","- ","- ","- ","2","4.2","6","0.0%"
"LVS","Las Vegas Sands","- ","- ","126.9","- ","-2.6%","-1.3%","3.3","- ","-2.2%","- ","- ","-$1.40","-$1.40","$2.75","97.8%","19.9","0.9","27.8","10.2","9","10.8","8","0.0%"
"MA","Mastercard","35.1","35.9","26.9","34.6","2.9%","3.5%","- ","1.8","3.0%","15.2%","-337.4%","$10.26","$10.22","$14.51","19.0%","24.7","1.6","64.7","15.7","8","54.2","8","3.2%"
"NKE","Nike","34.5","35.1","25.6","105.5","2.9%","3.4%","4.5","1.1","0.9%","9.8%","-266.2%","$3.59","$3.54","$4.05","25.4%","29.5","4.2","51.8","3.7","9","12.8","8","3.7%"
"NOW","ServiceNow","278.5","271.5","101.5","40.0","0.4%","0.5%","16.5","1.0","2.5%","- ","-876.3%","$1.61","$1.60","$11.35","23.5%","38.7","2.1","- ","12.4","8","17.8","7","0.0%"
"ROKU","Roku","- ","- ","-19.1","- ","-5.9%","-6.6%","- ","- ","-1.9%","- ","-1070.5%","-$3.62","-$3.62","-$2.67","- ","- ","- ","- ","2.7","6","3.2","6","0.0%"
"RTX","Raytheon Technologies","27.8","34.4","14.8","39.3","3.6%","4.3%","- ","19.8","3.3%","-4.0%","-206.7%","$3.54","$3.51","$5.82","16.2%","16.7","1.5","19.5","2.2","7","2.0","4","4.2%"
"RVLV","Revolve Gr","32.6","29.5","21.5","92.4","3.1%","4.4%","2.7","- ","1.1%","- ","-58.4%","$0.80","$0.79","$1.10","39.2%","23.3","- ","- ","1.7","7","5.0","7","0.0%"
"SNN","Smith & Nephew","54.4","68.6","16.8","135.0","1.8%","2.2%","5.3","- ","1.4%","-9.1%","- ","$0.51","$0.51","$0.00","- ","- ","11.8","- ","2.3","3","2.3","4","4.0%"
"SONO","Sonos","126.9","108.6","22.4","- ","0.8%","2.5%","5.5","- ","-4.0%","- ","-353.3%","$0.15","$0.15","$0.45","181.3%","42.2","- ","- ","1.5","7","3.8","8","7.0%"
"STNG","Scorpio Tankers","5.3","10.2","4.8","7.1","18.8%","16.5%","0.6","0.7","17.1%","14.5%","-1104.7%","$11.49","$10.34","$6.63","-35.5%","8.3","0.1","78.3","2.2","6","1.3","3","6.4%"
"SYNH","Syneos Health","13.7","59.6","10.0","19.2","7.3%","6.2%","- ","0.0","6.3%","27.2%","- ","$2.59","$2.58","$3.97","18.9%","8.9","41.2","29.5","0.7","2","1.0","3","4.1%"
"T","AT&T","- ","150.8","13.6","23.1","-5.8%","1.1%","1.0","0.1","5.6%","16.9%","- ","-$1.10","-$1.10","$2.51","2.9%","7.6","10.4","9.9","1.2","5","1.4","4","6.5%"
"TMO","Thermo Fisher Scientific","31.7","35.8","20.2","34.7","3.2%","3.5%","- ","0.5","3.2%","22.0%","-341.1%","$17.75","$17.63","$26.75","12.7%","20.9","3.2","58.6","4.9","6","4.9","6","1.6%"
"TSM","Taiwan Semiconductor","14.2","13.7","9.1","25.5","7.0%","7.6%","1.9","1.1","4.1%","21.7%","-218.7%","$5.64","$5.64","$6.93","25.3%","13.3","0.8","35.3","6.4","7","4.9","7","1.9%"
"TWLO","Twilio","- ","- ","-11.9","- ","-10.8%","-11.5%","- ","- ","-3.8%","- ","- ","-$6.86","-$6.86","$1.88","51.6%","33.5","0.5","- ","3.0","6","1.1","3","0.0%"
"V","Visa","30.9","31.5","23.9","26.7","3.2%","4.0%","- ","2.1","3.8%","12.4%","-239.1%","$7.16","$7.16","$9.67","14.6%","22.9","1.7","54.2","15.6","9","12.6","8","3.1%"
"VRNS","Varonis Systems","- ","- ","-23.3","4,813.7","-4.6%","-4.8%","- ","- ","0.1%","- ","- ","-$1.14","-$1.14","$0.38","11.8%","64.6","3.1","- ","5.7","7","5.3","6","2.1%"
"VST","Vistra","- ","16.5","22.3","- ","-13.8%","-4.3%","1.3","6.6","-1.6%","- ","- ","-$3.26","-$3.26","$3.37","14.2%","7.0","0.3","- ","0.7","4","3.1","8","24.9%"
"VXX","iPath Series B S&P 500 VIX Short-Term Futures ETN","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","0.0%"
"Z","Zillow Gr","- ","- ","65.2","2.0","-0.8%","-0.6%","- ","- ","51.2%","- ","- ","-$0.36","-$0.36","$1.61","69.5%","26.5","- ","- ","5.3","7","2.2","5","9.5%"
"Summary"," ","57.6","32.1","13.5"," ","1.7%","3.3%","1.4","0.1","3.7%","1.9%","-330.7%","$2.36","$2.23","$4.97","22.6%","16.7","4.6","54.2","1.6","6","2.9","6","4.0%"
"""

# Currently being used to calculate market share for sectors
income_data = """
"Ticker","Company","Sales","Cost of Sales","Research and Development","SG&A","Depreciation and Amortization","Cap Ex","Maintenance Cap Ex","Operating Income","Interest Expense","Dividends Cash Flow","Net Income","Net Margin","Diluted Shares"
"ACAD","ACADIA Pharmaceuticals","517","10","362","369","2","0","0","-224","0","0","-216","-41.8%","162"
"APTV","Aptiv","17,489","14,854","- ","1,138","762","844","844","1,348","219","63","594","3.4%","271"
"AXTA","Axalta Coating Sys","4,884","3,466","66","772","303","151","151","423","140","0","192","3.9%","222"
"BAM","Brookfield Asset Mgmt","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- "
"BG","Bunge","67,232","63,550","- ","1,369","408","555","555","2,313","403","349","1,610","2.4%","153"
"BLMN","Bloomin Brands","4,417","3,676","- ","235","170","220","220","336","53","50","102","2.3%","99"
"BRK.B","Berkshire Hathaway","234,190","0","- ","25,056","10,899","15,464","- ","- ","4,352","0","-22,819","-9.7%","2,203"
"BYND","Beyond Meat","419","443","62","240","33","73","- ","-326","4","0","-366","-87.4%","64"
"CARR","Carrier Global","20,421","14,957","539","2,512","380","353","- ","2,413","302","509","3,534","17.3%","861"
"CFLT","Confluent","586","202","264","582","8","14","14","-463","0","0","-453","-77.2%","280"
"CHRW","C.H. Robinson Worldwide","24,697","22,826","- ","603","93","129","64","1,267","100","285","941","3.8%","127"
"COIN","Coinbase Glb","3,194","630","2,326","2,111","154","64","- ","-2,669","89","0","-2,625","-82.2%","222"
"CP","Canadian Pacific Railway","6,496","3,113","- ","0","629","1,148","1,148","2,512","481","707","2,592","39.9%","933"
"CTLT","Catalent","4,757","3,201","- ","855","401","700","433","655","144","0","410","8.6%","180"
"DKS","Dick's Sporting Goods","12,368","8,084","- ","2,805","365","364","327","1,463","95","163","1,043","8.4%","99"
"DQ","Daqo New Energy","4,140","1,161","9","320","0","0","0","2,646","0","0","1,628","39.3%","76"
"EURN","Euronav","604","632","- ","43","251","527","527","-60","86","24","-104","-17.2%","202"
"EXPD","Expeditors Intl","17,071","14,900","- ","24","57","87","11","1,824","23","214","1,357","8.0%","164"
"FRO","Frontline","1,114","877","- ","37","156","482","482","208","80","0","252","22.7%","209"
"FTDR","Frontdoor","1,662","952","- ","521","34","40","34","155","31","0","71","4.3%","82"
"HZNP","Horizon Therapeutics","3,629","920","438","1,541","390","126","96","730","84","0","521","14.4%","235"
"LAC","Lithium Americas","0","0","- ","22","2","7","- ","-67","22","0","-98","- ","130"
"LVS","Las Vegas Sands","4,110","2,460","143","1,171","1,091","780","- ","-783","702","0","1,832","44.6%","764"
"MA","Mastercard","22,237","5,263","- ","3,502","750","1,097","452","12,722","471","1,903","9,930","44.7%","971"
"NKE","Nike","49,107","27,211","- ","15,517","958","896","528","6,379","122","1,924","5,634","11.5%","1,591"
"NOW","ServiceNow","7,245","1,573","1,768","3,549","433","550","550","355","27","0","325","4.5%","204"
"ROKU","Roku","3,127","1,685","789","1,183","104","162","69","-531","5","0","-498","-15.9%","138"
"RTX","Raytheon Technologies","67,074","53,406","2,711","5,663","4,108","2,775","1,586","5,414","1,300","3,128","5,197","7.8%","1,486"
"RVLV","Revolve Gr","1,101","509","- ","519","5","5","5","73","0","0","59","5.3%","75"
"SNN","Smith & Nephew","5,215","1,540","345","2,880","548","358","356","450","91","327","223","4.3%","437"
"SONO","Sonos","1,760","996","272","449","40","55","53","43","1","0","19","1.1%","135"
"STNG","Scorpio Tankers","1,563","623","- ","88","207","34","34","851","152","23","637","40.8%","64"
"SYNH","Syneos Health","5,393","4,139","- ","547","247","93","71","460","82","0","267","4.9%","103"
"T","AT&T","120,741","50,848","- ","28,961","18,021","19,626","- ","22,911","6,108","9,859","-8,524","-7.1%","7,587"
"TMO","Thermo Fisher Scientific","44,915","25,944","1,471","8,993","3,381","2,243","577","8,507","726","455","6,950","15.5%","394"
"TSM","Taiwan Semiconductor","68,804","29,377","5,000","1,959","14,590","32,810","32,810","32,439","351","9,451","29,247","42.5%","5,186"
"TWLO","Twilio","3,826","2,013","1,079","1,765","279","80","80","-1,031","0","0","-1,256","-32.8%","183"
"V","Visa","30,187","5,933","- ","3,176","890","1,046","1,046","20,188","541","3,339","15,177","50.3%","2,122"
"VRNS","Varonis Systems","474","70","178","347","12","11","11","-121","3","0","-125","-26.3%","109"
"VST","Vistra","13,728","12,046","- ","1,189","2,047","1,301","1,301","-1,103","562","453","-1,227","-8.9%","422"
"VXX","iPath Series B S&P 500 VIX Short-Term Futures ETN","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- "
"Z","Zillow Gr","1,958","367","498","1,162","180","140","- ","-69","35","0","-101","-5.2%","242"
"Summary"," ","882,453","384,457","18,320","123,778"," ","85,410","44,437","121,639","17,986","33,226","51,933","1.1%"," "

"""

balance_data = """
Ticker	Company	Cash	Current Assets	Net PP&E	Intangibles	Total Assets	Current Liabilities	Long Term Debt	Total Debt	Total Liabilities	Equity	Tangible Equity	Cash & Short‑term %	Net PP&E %	Intangibles %
AACTF	Aurora Solar Technologies	2	6	0	2	9	2	0	0	2	6	4	23.2%	5.5%	27.6%
ACU.V	Aurora Solar Technologies	3	8	1	3	12	3	0	0	3	9	5	23.2%	5.5%	27.6%
ANTGF	Advantagewon Oil	0	1	0	0	1	0	0	0	1	0	0	0.5%	9.0%	- 
AOC.CN	Advantagewon Oil	0	1	0	0	1	1	0	0	1	0	0	0.5%	9.0%	- 
ARRY	Array Technologies	134	831	23	803	1,706	465	720	770	1,282	424	-2,313	7.9%	1.4%	47.0%
ASTI	Ascent Solar Technologies	11	12	5	0	19	5	9	10	14	5	5	61.5%	26.1%	0.4%
BEEM	Beam Glb	5	25	3	15	43	12	1	2	13	30	15	10.9%	7.9%	34.6%
CBLU.V	Clear Blue Technologies	1	6	0	4	11	5	7	10	13	-2	-6	6.2%	3.3%	39.5%
CBUTF	Clear Blue Technologies	0	4	0	3	8	3	5	7	9	-2	-5	6.2%	3.3%	39.5%
CHJI	China Changjiang Mining	0	0	0	0	0	1	0	0	4	-4	-4	- 	- 	- 
CSIQ	Canadian Solar	1,083	5,753	1,646	80	8,661	4,930	1,187	3,981	6,545	1,785	1,706	12.5%	19.0%	0.9%
CSSXF	China Shuifa Singyes	123	1,479	796	18	2,415	1,034	573	1,054	1,648	641	623	5.1%	33.0%	0.7%
CVUEF	ClearVue Technologies	0	0	0	0	0	0	0	0	0	0	0	- 	- 	- 
EBODF	New Energy Exchange	10	29	1	2	34	26	0	0	27	8	- 	29.9%	1.5%	5.9%
EDYYF	Net Zero Renewable Energy	1	2	1	11	14	15	1	5	16	-2	-13	3.8%	6.1%	78.2%
ENPH	Enphase Energy	1,613	2,264	133	313	3,084	638	1,199	1,296	2,259	826	512	52.3%	4.3%	10.2%
FLDI	Folkup Development	2	6	0	0	7	9	2	4	10	-3	- 	27.3%	6.5%	- 
FSLR	First Solar	2,578	3,791	3,636	46	8,251	1,038	225	234	2,415	5,836	5,790	31.2%	44.1%	0.6%
FTCI	FTC Solar	44	119	3	9	134	60	1	1	68	66	58	33.0%	2.1%	6.4%
GCPEF	GCL Tech Hldgs	871	4,900	3,965	24	10,886	3,931	744	1,520	4,885	5,287	5,262	8.0%	36.4%	0.2%
GRMZF	Gremz	43	96	14	1	122	34	16	22	53	70	69	35.1%	11.3%	0.8%
HYSR	SunHydrogen	56	56	0	0	59	26	0	1	27	32	32	94.5%	0.2%	0.1%
ISUN	iSun	4	24	9	52	97	29	2	8	34	64	11	3.9%	9.1%	53.7%
JKS	JinkoSolar Holding Co	2,114	10,650	4,575	267	16,296	9,791	2,428	8,447	12,503	2,278	2,068	13.0%	28.1%	1.6%
MAXN	Maxeon Solar Technologies	303	791	398	0	1,260	576	396	450	1,212	42	42	24.1%	31.6%	0.0%
NOVA	Sunnova Energy Intl	360	948	3,785	176	8,337	542	5,195	5,412	6,449	1,273	1,097	4.3%	45.4%	2.1%
NTAC	New Technology	0	0	0	0	0	0	0	0	0	0	- 	78.9%	- 	- 
NXT	NEXTracker	100	954	8	267	1,260	605	0	0	1,163	96	-170	7.9%	0.6%	21.2%
PEGY	Pineapple Energy	0	0	0	4	5	0	5	5	7	-2	- 	- 	- 	89.8%
PPRW	Premier Power Renewable	1	24	0	7	32	28	0	1	30	2	- 	3.6%	0.6%	21.2%
PSWW	PSWW	0	2	13	0	15	14	0	8	14	1	- 	1.8%	87.0%	- 
PTOS	P2 Solar	0	0	0	0	0	1	0	0	1	-1	- 	6.9%	- 	- 
PXPC	Phoenix Plus	1	1	0	0	1	0	0	0	0	1	1	94.5%	1.1%	- 
QCLSY	Global PVQ	0	0	0	0	0	0	0	0	0	0	- 	- 	- 	- 
RUN	Sunrun	741	2,098	11,161	4,288	19,269	1,155	8,548	8,765	11,090	6,708	2,420	3.8%	57.9%	22.3%
SAENF	Solar Alliance Energy	1	2	1	0	3	3	0	0	3	0	0	29.6%	31.1%	- 
SEDG	SolarEdge Technologies	1,024	2,900	607	51	4,266	890	716	732	2,090	2,176	2,125	24.0%	14.2%	1.2%
SEHLF	Solargiga Energy Hldgs	74	704	323	0	1,032	759	102	398	916	55	55	7.1%	31.3%	- 
SHLS	Shoals Technologies Gr	9	154	17	127	595	53	237	239	294	291	165	1.5%	2.8%	21.3%
SING	SinglePoint	1	7	2	12	21	21	3	11	24	-3	-15	5.2%	7.4%	57.3%
SIRC	Solar Integrated Roofing	- 	- 	- 	- 	- 	- 	- 	- 	- 	- 	- 	- 	- 	- 
SMTGF	SMA Solar Tech	241	802	198	89	1,171	427	0	0	723	448	359	20.6%	16.9%	7.6%
SMTGY	SMA Solar Tech	241	802	198	89	1,171	427	0	0	723	448	359	20.6%	16.9%	7.6%
SOL	Emeren Group	208	286	161	1	500	31	37	48	68	390	389	41.6%	32.1%	0.2%
SOLR.V	Solar Alliance Energy	1	2	1	0	4	4	0	0	4	0	0	29.6%	31.1%	- 
SPI	SPI Energy	6	83	49	8	224	180	18	73	200	18	10	2.7%	21.7%	3.5%
SPRQ.V	SPARQ Systems	6	8	0	0	8	1	0	0	1	8	8	71.3%	1.6%	- 
SPRQF	SPARQ Systems	4	6	0	0	6	1	0	0	1	6	6	71.3%	1.6%	- 
SPRU	Spruce Power Holding	240	316	9	160	918	59	492	519	591	314	170	26.1%	1.0%	17.4%
SPWR	SunPower	510	1,269	153	151	1,780	1,050	38	559	1,204	575	424	28.6%	8.6%	8.5%
SRWRF	SolarWorld	116	399	294	23	727	206	341	413	598	129	- 	16.0%	40.4%	3.1%
SUNW	Sunworks	8	75	7	37	120	51	3	5	56	64	26	6.5%	6.2%	31.3%
VSOL.CN	Three Sixty Solar	1	3	0	0	4	1	0	0	1	3	3	25.6%	3.1%	- 
VSOLF	Three Sixty Solar	1	3	0	0	3	1	0	0	1	2	2	25.6%	3.1%	- 
VVPR	Vivopower Intl	3	17	4	41	67	28	22	32	51	16	-25	4.8%	5.6%	60.9%
XISHY	Xinyi Solar Holdings	892	2,557	3,645	3	6,302	1,269	424	1,000	1,742	3,835	3,832	14.2%	57.8%	0.1%
XNYIF	Xinyi Solar Holdings	892	2,557	3,645	3	6,302	1,269	424	1,000	1,742	3,835	3,833	14.2%	57.8%	0.1%
"""

profitability = """
"Ticker","Company","Return on Assets","Return on Equity","ROIC","Greenblatt ROC","Gross Profit / Total Assets","Gross Margin","Operating Margin","Net Margin","EBITDA Margin","Operating Margin vs Industry","Net Margin vs Industry","Profitability Industry Decile"
"ACAD","ACADIA Pharmaceuticals","-36.7%","-53.9%","-41.2%","-50.4%","0.9","98.0%","-43.2%","-41.8%","-42.8%","-51.1%","-41.1%","5"
"APTV","Aptiv","2.7%","6.0%","4.5%","17.6%","0.1","15.1%","7.7%","3.4%","11.3%","2.3%","0.4%","5"
"AXTA","Axalta Coating Sys","2.7%","13.2%","5.6%","15.3%","0.2","29.1%","8.7%","3.9%","14.3%","-3.6%","-4.5%","5"
"BAM","Brookfield Asset Mgmt","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","10"
"BG","Bunge","6.6%","17.5%","13.1%","20.9%","0.2","5.5%","3.4%","2.4%","4.3%","-2.4%","-1.8%","3"
"BLMN","Bloomin Brands","3.1%","37.6%","6.3%","10.2%","0.2","16.8%","7.6%","2.3%","8.5%","-6.0%","-5.6%","3"
"BRK.B","Berkshire Hathaway","-2.4%","-4.8%","-3.1%","-13.3%","0.3","0.0%","- ","-9.7%","-6.5%","- ","-13.2%","6"
"BYND","Beyond Meat","-34.5%","179.9%","-36.6%","-35.7%","0.0","-5.7%","-77.7%","-87.4%","-74.1%","-88.4%","-93.7%","3"
"CARR","Carrier Global","13.6%","45.6%","21.8%","68.3%","0.2","26.8%","11.8%","17.3%","24.4%","0.5%","9.0%","1"
"CFLT","Confluent","-19.3%","-58.8%","-23.5%","-25.2%","0.2","65.5%","-79.0%","-77.2%","-77.7%","-102.5%","-93.0%","7"
"CHRW","C.H. Robinson Worldwide","15.8%","69.5%","25.7%","158.8%","0.3","7.6%","5.1%","3.8%","5.5%","-2.7%","-2.1%","1"
"COIN","Coinbase Glb","-2.9%","-48.1%","-27.1%","-50.7%","0.0","80.3%","-83.6%","-82.2%","-88.3%","-112.6%","-102.5%","9"
"CP","Canadian Pacific Railway","4.8%","9.0%","7.2%","21.2%","0.1","52.1%","38.7%","39.9%","47.3%","20.4%","26.8%","2"
"CTLT","Catalent","3.7%","8.3%","5.6%","13.0%","0.1","32.7%","13.8%","8.6%","22.1%","3.5%","10.2%","1"
"DKS","Dick's Sporting Goods","11.6%","41.3%","16.7%","25.6%","0.5","34.6%","11.8%","8.4%","14.9%","5.9%","5.3%","2"
"DQ","Daqo New Energy","23.6%","38.0%","38.0%","45.1%","0.4","72.0%","63.9%","39.3%","64.0%","34.9%","16.1%","1"
"EURN","Euronav","-2.6%","-5.3%","-0.5%","-1.1%","0.0","-4.6%","-10.0%","-17.2%","35.2%","-22.3%","-24.4%","5"
"EXPD","Expeditors Intl","24.3%","43.7%","35.7%","53.5%","0.4","12.7%","10.7%","8.0%","11.2%","2.8%","2.0%","2"
"FRO","Frontline","5.6%","12.5%","7.6%","8.6%","0.1","21.3%","18.7%","22.7%","44.3%","6.4%","15.5%","2"
"FTDR","Frontdoor","6.6%","116.4%","13.7%","161.0%","0.7","42.7%","9.3%","4.3%","9.5%","-2.6%","-0.7%","1"
"HZNP","Horizon Therapeutics","5.7%","10.3%","8.1%","20.1%","0.3","74.6%","20.1%","14.4%","27.6%","-5.9%","-6.0%","5"
"LAC","Lithium Americas","-9.3%","-12.4%","-7.3%","-10.0%","0.0","- ","- ","- ","- ","- ","- ","3"
"LVS","Las Vegas Sands","8.3%","47.2%","11.9%","-4.2%","0.1","40.2%","-19.0%","44.6%","9.9%","-21.8%","44.9%","1"
"MA","Mastercard","25.6%","157.7%","49.7%","274.8%","0.4","76.3%","57.2%","44.7%","58.3%","21.7%","23.4%","1"
"NKE","Nike","14.2%","36.9%","20.7%","25.6%","0.6","44.6%","13.0%","11.5%","14.9%","3.5%","4.2%","2"
"NOW","ServiceNow","2.4%","6.5%","4.3%","17.9%","0.4","78.3%","4.9%","4.5%","11.9%","5.8%","13.2%","3"
"ROKU","Roku","-11.3%","-18.8%","-14.9%","-17.8%","0.3","46.1%","-17.0%","-15.9%","-12.2%","-24.9%","-17.4%","8"
"RTX","Raytheon Technologies","3.3%","7.2%","5.9%","36.0%","0.1","20.4%","8.1%","7.8%","17.1%","0.8%","3.6%","3"
"RVLV","Revolve Gr","10.1%","15.5%","16.1%","19.8%","1.0","53.8%","6.6%","5.3%","7.1%","4.1%","6.7%","1"
"SNN","Smith & Nephew","2.2%","4.2%","3.5%","9.1%","0.4","70.5%","8.6%","4.3%","16.8%","-2.4%","0.0%","2"
"SONO","Sonos","1.6%","3.0%","3.0%","9.7%","0.6","43.4%","2.5%","1.1%","5.1%","-17.2%","-15.1%","4"
"STNG","Scorpio Tankers","14.0%","25.4%","15.4%","19.8%","0.2","60.1%","54.5%","40.8%","63.7%","42.2%","33.6%","1"
"SYNH","Syneos Health","3.3%","7.6%","5.2%","60.5%","0.2","23.3%","8.5%","4.9%","11.9%","-7.0%","-2.3%","2"
"T","AT&T","-2.1%","-8.9%","-1.6%","2.0%","0.2","57.9%","19.0%","-7.1%","17.4%","3.3%","-11.4%","7"
"TMO","Thermo Fisher Scientific","7.2%","15.8%","9.6%","48.9%","0.2","42.2%","18.9%","15.5%","26.6%","3.4%","8.3%","2"
"TSM","Taiwan Semiconductor","19.0%","32.2%","24.7%","27.5%","0.3","57.3%","47.2%","42.5%","69.6%","22.2%","21.0%","2"
"TWLO","Twilio","-10.0%","-11.9%","-10.4%","-22.6%","0.1","47.4%","-26.9%","-32.8%","-19.6%","-45.8%","-50.4%","6"
"V","Visa","17.8%","41.1%","27.4%","159.7%","0.3","80.4%","66.9%","50.3%","65.1%","31.4%","29.0%","1"
"VRNS","Varonis Systems","-11.9%","-24.8%","-15.0%","-13.9%","0.4","85.3%","-25.6%","-26.3%","-20.2%","-49.1%","-42.1%","6"
"VST","Vistra","-3.7%","-28.1%","-5.7%","-7.5%","0.1","12.3%","-8.0%","-8.9%","7.6%","-8.4%","-5.1%","6"
"VXX","iPath Series B S&P 500 VIX Short-Term Futures ETN","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- ","- "
"Z","Zillow Gr","-1.5%","-2.2%","-1.0%","-1.3%","0.2","81.3%","-3.5%","-5.2%","6.6%","-22.3%","-22.8%","4"
"Summary"," ","2.8%","19.3%","5.5%","27.4%","0.3","43.5%","4.0%","1.1%","10.6%","-10.1%","-7.2%","4"
"""

financial_health = """
"Ticker","Company","Morningstar Financial Health Grade","Solvency Ratio","Financial Safety Industry Decile","Piotroski F Score","Beneish M-Score","Altman Z-Score","Sloan Ratio","Cash Per Share","Debt Per Share","Net Cash Per Share","Net Cash as a % of Market Cap","Debt / Equity","Long Term Debt / Total Capital","Current Ratio","Quick Ratio","Interest Coverage"
"ACAD","ACADIA Pharmaceuticals","B","-120%","5","3","-2.50","4.6","-29.8%","$2.58","$0.38","$2.19","12%","0.2","0.1","4.0","4.0","- "
"APTV","Aptiv","C","12%","7","4","-1.97","2.9","20.6%","$5.65","$25.70","-$20.05","-18%","0.8","0.4","1.6","1.1","5.5"
"AXTA","Axalta Coating Sys","B","10%","9","6","-2.45","2.0","0.1%","$2.90","$16.84","-$13.93","-47%","2.6","0.7","1.9","1.4","2.8"
"BAM","Brookfield Asset Mgmt","- ","- ","9","- ","- ","- ","- ","- ","- ","$0.00","- ","- ","- ","- ","- ","- "
"BG","Bunge","C","12%","5","3","-2.37","4.6","2.7%","$7.99","$37.81","-$29.83","-31%","0.6","0.3","1.8","0.9","6.1"
"BLMN","Bloomin Brands","C","9%","7","5","-2.59","1.6","-2.6%","$0.86","$22.31","-$21.45","-86%","7.3","0.9","0.4","0.3","3.9"
"BRK.B","Berkshire Hathaway","B","-10%","1","3","-2.88","- ","2.9%","$57.79","$55.17","$2.63","1%","0.3","0.2","- ","- ","-6.0"
"BYND","Beyond Meat","D","-26%","9","2","-5.68","-0.5","3.9%","$4.87","$18.76","-$13.89","-88%","- ","1.2","8.0","4.9","-86.5"
"CARR","Carrier Global","B","26%","8","5","-2.09","2.8","0.2%","$4.09","$11.11","-$7.02","-16%","1.2","0.5","1.6","1.2","15.2"
"CFLT","Confluent","C","-29%","7","4","-2.18","2.2","24.3%","$6.88","$3.99","$2.89","12%","1.5","0.6","5.2","5.2","- "
"CHRW","C.H. Robinson Worldwide","B","23%","9","8","-3.11","7.7","-10.8%","$1.71","$18.78","-$17.07","-19%","1.7","0.5","1.1","1.1","12.7"
"COIN","Coinbase Glb","F","-3%","8","2","-3.72","0.2","-0.4%","$23.78","$15.70","$8.08","12%","0.6","0.4","1.1","1.1","-33.5"
"CP","Canadian Pacific Railway","A","20%","3","7","-2.12","2.2","1.2%","$0.36","$15.79","-$15.43","-20%","0.5","0.3","0.6","0.5","7.4"
"CTLT","Catalent","C","14%","6","3","-2.69","2.0","12.5%","$2.61","$27.14","-$24.54","-38%","1.0","0.5","1.9","1.3","4.5"
"DKS","Dick's Sporting Goods","C","22%","6","5","-2.66","4.1","5.7%","$19.39","$54.14","-$34.76","-19%","1.7","0.6","1.9","0.8","15.5"
"DQ","Daqo New Energy","C","179%","3","8","-1.87","4.6","8.5%","$40.44","$0.00","$40.44","88%","0.0","- ","5.2","5.1","- "
"EURN","Euronav","- ","7%","2","6","4.38","1.2","3.8%","$1.01","$9.74","-$8.73","-52%","1.0","0.5","2.1","1.8","-0.4"
"EXPD","Expeditors Intl","B","57%","2","7","-3.48","9.4","-12.2%","$12.37","$3.18","$9.19","9%","0.2","0.1","2.2","2.2","79.9"
"FRO","Frontline","C","16%","3","7","-3.93","1.4","8.3%","$1.63","$11.26","-$9.63","-56%","1.2","0.5","1.6","1.6","4.2"
"FTDR","Frontdoor","B","11%","6","7","-3.02","3.4","-3.3%","$3.56","$7.67","-$4.10","-15%","10.3","0.9","0.9","0.9","4.0"
"HZNP","Horizon Therapeutics","B","26%","5","7","-2.65","4.8","-6.6%","$10.12","$11.26","-$1.13","-1%","0.5","0.3","3.9","3.6","7.3"
"LAC","Lithium Americas","B","-38%","7","3","-2.27","7.4","27.7%","$3.08","$1.88","$1.20","5%","0.3","0.2","52.1","52.1","-3.5"
"LVS","Las Vegas Sands","B","16%","7","6","-1.71","1.7","-7.0%","$8.26","$20.91","-$12.65","-23%","4.1","0.8","1.7","1.7","-1.0"
"MA","Mastercard","A","38%","5","7","-2.64","10.0","0.5%","$7.63","$14.49","-$6.86","-2%","2.2","0.7","1.2","1.2","25.9"
"NKE","Nike","B","30%","5","5","-2.22","7.0","8.6%","$6.68","$7.98","-$1.31","-1%","0.8","0.4","2.7","1.8","52.3"
"NOW","ServiceNow","B","9%","6","7","-2.36","7.2","1.4%","$21.03","$11.08","$9.95","2%","0.4","0.3","1.1","1.1","15.8"
"ROKU","Roku","C","-24%","2","4","-2.61","3.7","-7.0%","$14.25","$5.22","$9.03","15%","0.3","0.2","2.7","2.6","-94.4"
"RTX","Raytheon Technologies","B","13%","4","8","-2.71","2.0","0.5%","$4.19","$22.70","-$18.52","-19%","0.5","0.3","1.1","0.8","5.6"
"RVLV","Revolve Gr","C","32%","2","5","-3.24","9.4","7.0%","$3.15","$0.33","$2.82","11%","0.1","0.1","2.9","1.7","- "
"SNN","Smith & Nephew","A","17%","6","7","-2.57","3.2","2.3%","$0.80","$6.59","-$5.79","-21%","0.6","0.3","2.3","1.0","3.6"
"SONO","Sonos","C","12%","2","4","-2.43","4.6","16.5%","$3.20","$0.26","$2.94","16%","0.1","0.0","1.9","1.2","81.5"
"STNG","Scorpio Tankers","C","41%","1","8","10.95","2.0","-15.4%","$5.93","$34.84","-$28.90","-48%","0.8","0.4","1.5","1.4","5.2"
"SYNH","Syneos Health","C","11%","6","8","-2.55","1.4","-0.7%","$1.08","$28.15","-$27.07","-76%","0.8","0.5","1.1","1.1","4.8"
"T","AT&T","C","5%","5","4","-3.08","0.6","-3.7%","$0.49","$21.59","-$21.10","-111%","1.6","0.6","0.6","0.5","0.5"
"TMO","Thermo Fisher Scientific","B","22%","6","6","-2.57","3.9","0.0%","$21.63","$87.98","-$66.35","-12%","0.8","0.4","1.5","1.2","11.8"
"TSM","Taiwan Semiconductor","B","79%","5","8","-2.49","6.5","10.2%","$9.70","$5.59","$4.11","5%","0.3","0.2","2.5","2.2","94.9"
"TWLO","Twilio","C","-49%","2","3","-2.24","3.6","-3.1%","$22.71","$6.77","$15.93","25%","0.1","0.1","6.2","6.2","- "
"V","Visa","A","40%","3","8","-2.74","7.3","0.8%","$7.60","$9.86","-$2.26","-1%","0.6","0.4","1.4","1.4","34.7"
"VRNS","Varonis Systems","C","-21%","5","4","-2.86","3.1","22.8%","$6.70","$2.90","$3.81","16%","0.6","0.4","4.0","4.0","-34.0"
"VST","Vistra","C","4%","5","6","-2.27","0.4","-1.4%","$1.08","$31.57","-$30.49","-143%","2.7","0.7","1.1","1.0","-1.8"
"VXX","iPath Series B S&P 500 VIX Short-Term Futures ETN","- ","- ","- ","- ","- ","- ","- ","- ","- ","$0.00","- ","- ","- ","- ","- ","- "
"Z","Zillow Gr","C","4%","4","6","-2.71","3.4","-46.8%","$14.10","$7.83","$6.27","15%","0.4","0.3","13.3","13.3","-1.4"
"Summary"," "," ","12%","5","5","-2.17","3.8","1.0%","$9.35","$17.38","-$7.65","-18%","1.3","0.4","3.8","3.5","6.9"
"""

per_share = """
"Ticker","Company","EPS","EPS Diluted","Cash Flow Per Share","Free Cash Flow Per Share","Dividend Per Share","Cash Per Share","Debt Per Share","Net Cash Per Share","Sales Per Share","Operating Income Per Share","Equity Per Share","Tangible Equity Per Share"
"ACAD","ACADIA Pharmaceuticals","-$1.34","-$1.34","-$0.71","-$0.71","- ","$2.58","$0.38","$2.19","$3.20","-$1.38","$2.47","$2.47"
"APTV","Aptiv","$1.96","$1.96","$4.66","$1.55","- ","$5.65","$25.70","-$20.05","$64.49","$4.97","$32.50","$4.12"
"AXTA","Axalta Coating Sys","$0.86","$0.86","$1.32","$0.64","- ","$2.90","$16.84","-$13.93","$21.97","$1.91","$6.58","-$5.23"
"BAM","Brookfield Asset Mgmt","- ","- ","- ","- ","$1.28","- ","- ","$0.00","- ","- ","- ","- "
"BG","Bunge","$10.83","$10.51","-$36.24","-$39.86","$2.50","$7.99","$37.81","-$29.83","$439.04","$15.42","$61.52","$55.99"
"BLMN","Bloomin Brands","$1.15","$1.03","$3.97","$1.74","$0.96","$0.86","$22.31","-$21.45","$44.83","$3.86","$3.10","-$5.40"
"BRK.B","Berkshire Hathaway","-$10.36","-$10.36","$16.89","$9.88","- ","$57.79","$55.17","$2.63","$106.29","- ","$216.33","$167.18"
"BYND","Beyond Meat","-$5.75","-$5.75","-$5.03","-$6.19","- ","$4.87","$18.76","-$13.89","$6.58","-$5.08","-$3.18","-$3.18"
"CARR","Carrier Global","$4.19","$4.10","$2.02","$1.61","$0.74","$4.09","$11.11","-$7.02","$23.71","$2.89","$9.29","-$4.26"
"CFLT","Confluent","-$1.62","-$1.62","-$0.56","-$0.61","- ","$6.88","$3.99","$2.89","$2.09","-$1.59","$2.64","$2.64"
"CHRW","C.H. Robinson Worldwide","$7.48","$7.40","$12.98","$11.97","$2.44","$1.71","$18.78","-$17.07","$194.23","$10.88","$11.62","-$2.32"
"COIN","Coinbase Glb","-$11.81","-$11.83","-$7.13","-$7.42","- ","$23.78","$15.70","$8.08","$14.37","-$11.52","$23.56","$18.34"
"CP","Canadian Pacific Railway","$2.73","$2.72","$3.25","$2.03","$0.57","$0.36","$15.79","-$15.43","$6.92","$2.70","$30.59","$30.29"
"CTLT","Catalent","$2.28","$2.28","$1.82","-$2.06","- ","$2.61","$27.14","-$24.54","$26.37","$3.64","$27.28","$3.62"
"DKS","Dick's Sporting Goods","$13.43","$10.78","$9.29","$5.62","$2.46","$19.39","$54.14","-$34.76","$124.59","$17.09","$29.49","$25.91"
"DQ","Daqo New Energy","$21.69","$21.24","$31.92","$31.92","- ","$40.44","$0.00","$40.44","$59.62","$35.22","$64.65","$63.58"
"EURN","Euronav","-$0.52","-$0.52","$1.27","-$1.41","$0.12","$1.01","$9.74","-$8.73","$4.23","-$0.30","$10.77","$10.69"
"EXPD","Expeditors Intl","$8.33","$8.26","$12.95","$12.42","$1.34","$12.37","$3.18","$9.19","$103.82","$11.81","$20.14","$20.08"
"FRO","Frontline","$1.20","$1.20","$1.73","$0.25","$4.28","$1.63","$11.26","-$9.63","$6.68","$0.94","$10.19","$9.68"
"FTDR","Frontdoor","$0.87","$0.87","$1.73","$1.24","- ","$3.56","$7.67","-$4.10","$20.27","$1.90","$0.75","-$7.24"
"HZNP","Horizon Therapeutics","$2.28","$2.22","$5.35","$4.81","- ","$10.12","$11.26","-$1.13","$15.43","$3.19","$22.20","$2.57"
"LAC","Lithium Americas","-$0.70","-$0.70","-$0.52","-$0.57","- ","$3.08","$1.88","$1.20","$0.00","-$0.44","$5.11","$5.11"
"LVS","Las Vegas Sands","-$1.40","-$1.40","-$1.04","-$2.06","- ","$8.26","$20.91","-$12.65","$5.38","-$1.02","$5.08","$4.99"
"MA","Mastercard","$10.26","$10.22","$11.53","$10.40","$2.28","$7.63","$14.49","-$6.86","$22.90","$13.35","$6.61","-$5.33"
"NKE","Nike","$3.59","$3.54","$1.70","$1.13","$1.36","$6.68","$7.98","-$1.31","$32.05","$4.10","$9.37","$9.01"
"NOW","ServiceNow","$1.61","$1.60","$13.38","$10.68","- ","$21.03","$11.08","$9.95","$35.60","$1.75","$24.79","$19.59"
"ROKU","Roku","-$3.62","-$3.62","$0.09","-$1.09","- ","$14.25","$5.22","$9.03","$22.71","-$3.79","$18.89","$15.23"
"RTX","Raytheon Technologies","$3.54","$3.51","$4.82","$2.96","$2.20","$4.19","$22.70","-$18.52","$45.14","$3.70","$49.64","-$12.32"
"RVLV","Revolve Gr","$0.80","$0.79","$0.31","$0.25","- ","$3.15","$0.33","$2.82","$14.78","$1.00","$5.17","$5.12"
"SNN","Smith & Nephew","$0.51","$0.51","$1.07","$0.25","$0.75","$0.80","$6.59","-$5.79","$11.95","$1.01","$12.04","$2.27"
"SONO","Sonos","$0.15","$0.15","-$0.19","-$0.60","- ","$3.20","$0.26","$2.94","$13.03","$0.34","$4.97","$3.59"
"STNG","Scorpio Tankers","$11.49","$10.34","$12.11","$11.57","$0.80","$5.93","$34.84","-$28.90","$24.61","$14.43","$42.46","$42.32"
"SYNH","Syneos Health","$2.59","$2.58","$4.13","$3.22","- ","$1.08","$28.15","-$27.07","$52.12","$4.45","$33.85","-$20.18"
"T","AT&T","-$1.10","-$1.10","$4.22","$1.63","$1.11","$0.49","$21.59","-$21.10","$15.91","$3.22","$13.67","-$14.00"
"TMO","Thermo Fisher Scientific","$17.75","$17.63","$23.23","$17.54","$1.40","$21.63","$87.98","-$66.35","$114.00","$22.07","$114.10","-$38.04"
"TSM","Taiwan Semiconductor","$5.64","$5.64","$10.29","$3.33","$1.79","$9.70","$5.59","$4.11","$14.47","$6.50","$18.82","$18.66"
"TWLO","Twilio","-$6.86","-$6.86","-$1.39","-$1.83","- ","$22.71","$6.77","$15.93","$20.91","-$5.50","$56.38","$23.63"
"V","Visa","$7.16","$7.16","$8.85","$8.36","$1.80","$7.60","$9.86","-$2.26","$14.23","$9.60","$17.57","-$3.52"
"VRNS","Varonis Systems","-$1.14","-$1.14","$0.11","$0.00","- ","$6.70","$2.90","$3.81","$4.33","-$1.13","$4.67","$4.43"
"VST","Vistra","-$3.26","-$3.26","$1.15","-$1.93","$0.79","$1.08","$31.57","-$30.49","$32.50","-$2.89","$7.61","-$4.30"
"VXX","iPath Series B S&P 500 VIX Short-Term Futures ETN","- ","- ","- ","- ","- ","- ","- ","$0.00","- ","- ","- ","- "
"Z","Zillow Gr","-$0.36","-$0.36","$18.60","$18.02","- ","$14.10","$7.83","$6.27","$8.09","-$0.30","$19.13","$8.34"
"Summary"," ","$2.36","$2.23","$4.35","$2.72","$1.55","$9.35","$17.38","-$7.65","$44.84","$4.28","$26.31","$11.35"

"""