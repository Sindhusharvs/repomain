import requests
from bs4 import BeautifulSoup
import re
import logging
import os
# import sys
# sys.path.append("/root/central/PRE_CATS_OTTO/")
# from migration.db_class import Database_Manager
import datetime
from collections import defaultdict
# FERACK2 = Database_Manager('FERACK2','SOV')
# FERACK34 = Database_Manager('FERACK34','ISIN')

# try:
#     current_file_date=datetime.datetime.now().strftime('%Y%m%d')
#     #Create log folder if not available
#     path = '/root/central/PRE_CATS_OTTO/log_file/{}/new_issuance/'.format(current_file_date)
#     os.makedirs(os.path.dirname(path), exist_ok=True)
#     fileid = str(os.path.basename(__file__)).split('.')[0]
#     log_filename='/root/central/PRE_CATS_OTTO/log_file/'+current_file_date+'/new_issuance/'+fileid+'.log'

#     # Create and configure logger
#     logging.basicConfig(filename=log_filename,format='%(asctime)s %(message)s',filemode='a+',level = logging.INFO)
#     print('Check print statement in log file path -  {}'.format(log_filename))
            
# except (FileNotFoundError, PermissionError, FileExistsError) as e :
#     print(f"Error: {str(e)}")
    


data_urls = ['https://www.bankofcanada.ca/valet/observations/group/AUC_TBILL/csv','https://www.bankofcanada.ca/valet/observations/group/AUC_BOND/csv','https://www.bankofcanada.ca/valet/observations/group/AUC_TBILL_C/csv','https://www.bankofcanada.ca/valet/observations/group/AUC_BOND_U/csv','https://www.bankofcanada.ca/valet/observations/group/AUC_BOND_RR/csv','https://www.bankofcanada.ca/valet/observations/group/AUC_BOND_R/csv','https://www.bankofcanada.ca/valet/observations/group/AUC_BOND_S/csv']
# data_urls=['https://www.bankofcanada.ca/valet/observations/group/GREEN_BOND/csv']
urls = ['Historical_RegularTreasuryBills','Historical_NominalBonds','Historical_CashManagementBills','Historical_UltraLongBonds','Historical_RealReturnBonds','Historical_CashManagementBondBuybacks','Historical_BondSwitch']
try:
    for data_url,url in zip(data_urls,urls):
        logging.info(f'url-{data_url},  category - {url}')
        # main_url = f'https://www.bankofcanada.ca/markets/government-securities-auctions/calls-for-tenders-and-results/{url}/'
        response = requests.request('GET', data_url)
        # logging.info(f'Got response - {response} for the url -{main_url}')
        Key_mapping= {'tbill_id':'Description',
        'AUC_TBILL_ALLOTMENT_RATIO':'AllotmentRatio',
        'AUC_TBILL_AMOUNT':'Amount',
        'AUC_TBILL_AUCTION_DATE':'AuctionDate',
        'AUC_TBILL_AVG_PRICE':'AveragePrice',
        'AUC_TBILL_AVG_YIELD':'AverageYield',
        'AUC_TBILL_BID_DEADLINE':'BiddingDeadline',
        'AUC_TBILL_BOC_HELD':'OfWhichHeldByBankOfCanada',
        'AUC_TBILL_BOC_PURCHASE':'BankOfCanadaPurchase',
        'AUC_TBILL_COVERAGE':'Coverage',
        'AUC_TBILL_HIGH_YIELD':'HighYield',
        'AUC_TBILL_ISIN':'ISIN',
        'AUC_TBILL_ISSUE_DATE':'IssueDate',
        'AUC_TBILL_KEY':'AuctionKey',
        'AUC_TBILL_LOW_YIELD':'LowYield',
        'AUC_TBILL_MATURITY_DATE': 'MaturityDate',
        'AUC_TBILL_NON_COMPETE_AMOUNT':'TotalNonCompSubmittedByGSD',
        'AUC_TBILL_OUTSTANDING_AFTER':'OutstandingAfter',
        'AUC_TBILL_OUTSTANDING_PRIOR':'OutstandingPrior',
        'AUC_TBILL_STATUS':'Status',
        'AUC_TBILL_TAIL':'Tail',
        'AUC_TBILL_TERM_DAYS':'Term',
        'AUC_TBILL_TOTAL_AMOUNT':'TotalAmount',
        'AUC_TBILL_TOTAL_AMOUNT_MATURING':'TotalAmountMaturing ',
        'AUC_TBILL_TOTAL_SUBMITTED':'TotalSubmittedByGSD',
        'AUC_TBILL_BOC_MIN_PURCHASE':'BankOfCanadaMinimumPurchase',
        'AUC_TBILL_COUPON_RATE':'CouponRate',
        'AUC_TBILL_INTEREST_END_DATE':'AccruedInterestEndDate',
        'AUC_TBILL_INTEREST_RATE':'AccruedInterestRatePer_1000',
        'AUC_TBILL_INTEREST_START_DATE': 'AccruedInterestStartDate',
        'AUC_TBILL_OUTSTANDING_INC_RECONSTITUTED':'OutstandingIncludingReconstituted',
        'AUC_TBILL_TERM_YEARS':'Term',
        'AUC_TBILL_TYPE' : 'Type',
        'AUC_TBILL_ALLOTMENT_PRICE':'AllotmentPrice' ,
        'AUC_TBILL_CUTOFF_YIELD':'CutOffYield',
        'AUC_TBILL_MAX_TOTAL_PURCHASE':'MaximumTotalRepurchase',
        'AUC_TBILL_SETTLEMENT_DATE':'Settlement date',
        'AUC_TBILL_TOTAL_AMOUNT_REPURCHASED': 'TotalAmountRepurchased',
        'AUC_TBILL_MEDIAN_YIELD':'MedianYield',
        'AUC_TBILL_AMOUNT_REPURCHASED':'AmountRepurchased',
        'AUC_TBILL_INDEX_RATIO':'IndexRatio',
        'AUC_TBILL_CONVERSION_RATIO':'ConversionRatio',
        'AUC_TBILL_CUTOFF_SPREAD':'CutOffSpread',
        'AUC_TBILL_ISSUE_AMOUNT':'IssueAmount',
        'AUC_TBILL_MAX_REPLACEMENT_AMOUNT':'MaximumReplacementAmount ',
        'AUC_TBILL_TOTAL_REPLACEMENT_AMOUNT':'TotalReplacementAmount',
        'AUC_TBILL_ISSUE_PRICE':'IssuePrice',
        'AUC_TBILL_NOMINAL_AMOUNT':'NominalAmount',
        'AUC_TBILL_PRICE':'Price',
        'AUC_TBILL_TRADE_DATE':'TradeDate',
        'AUC_TBILL_BENCHMARK_YIELD':'BenchmarkYield',
        'AUC_TBILL_ALLOTMENT_YIELD':'AllotmentYield'}
        
        isin_counts = defaultdict(int)
        content = response.text.split('OBSERVATIONS')[1].split('\r\n')
        Headers = content[1].replace('"','').split(',')
        fields1 = {'Category':url,'Data_Link':data_url}
        for data in content[2:]:
            rows = data.replace('"','').split(',')
            fields2 = {}
            for header,row in zip(Headers,rows):
                print(header)
                try:
                    if header != 'tbill_id':
                        header = 'AUC_TBILL' + header.split(data_url.split('/group/')[1].split('/')[0])[1]
                    old_key = header
                    new_key = Key_mapping[old_key]
                    fields2[new_key] = row
                    if new_key.endswith('ISIN') :
                        isin_value = row
                        count = isin_counts[isin_value] + 1
                        isin_counts[isin_value] = count
                        fields2[new_key] = row
                        if str(fields2[new_key]) != '' :
                            fields2['Tranche'] =  count
                        else:
                            fields2['Tranche'] =''
                    else:
                        pass
                except :
                    pass
                
            fields={**fields1,**fields2}
            print(fields)
            logging.info(fields)
        logging.info('Link Completed')
    logging.info('Entire Extraction Completed')
        
except Exception as e:
    print(e)
    logging.info(e)
    logging.info('Failed to extracet')
        
        # logging.info(fields)
       
        
    # key_mapping = {'auctiondate': 'AuctionDate' ,
    # 'biddingdeadline': 'BiddingDeadline':,
    # 'issuedate': 'IssueDate':,
    # 'term':'Term':,
    # 'maturitydate': 'MaturityDate':,
    # 'couponrate' : 'CouponRate':,
    # 'isin': 'ISIN':,
    # 'amount': 'Amount':,
    # 'avgprice': 'AveragePrice':,
    # 'allotmentprice':'AllotmentPrice':,
    # 'allotmentyield':'AllotmentYield':,
    # 'low5%yield' :'LowYield':,
    # 'avgyield': 'AverageYield':,
    # 'medianyield':'MedianYield':,
    # 'type':'Type':,
    # 'lowyield': 'LowYield':,
    # 'highyield': 'HighYield':,
    # 'coverage': 'Coverage':,
    # 'tail': 'Tail':,
    # 'outstandingafter': 'OutstandingAfter':,
    # 'settlementdate':'SettlementDate':,
    # 'amountrepurchased':'AmountRepurchased':,
    # 'cutoffyield' : 'CutoffYield':,
    # 'allotmentratio' : 'AllotmentRatio':,
    # 'issueamount':'IssueAmount':,
    # 'price' : 'Price':,
    # 'totalamountrepurchased':'TotalAmountRepurchased':,
    # 'totalreplacementamount':'TotalReplacementAmount':,
    # 'cutoffspread':'CutOffSpread':,
    # 'conversionratio':'ConversionRatio':,
    # 'bankofcanadapurchase': 'BankOfCanadaPurchase':,
    # 'totalsubmittedbygsd': 'TotalSubmittedByGSD':,
    # 'totalnon-compsubmittedbygsd':'TotalNonCompSubmittedByGSD'}
    
    # for data in content[2:]:
    #     rows = data.replace('"','').split(',')
    #     fields2 = {}
    #     for header,row in zip(Headers,rows):
    #         print(header)
    #         try:
    #             if header != 'tbill_id':
    #                 header = 'AUC_TBILL' + header.split(data_url.split('/group/')[1].split('/')[0])[1]
    #             old_key = header
    #             new_key = Key_mapping[old_key]
    #             fields2[new_key] = row
    #             if new_key.endswith('ISIN'):
    #                 isin_value = row
    #                 isin_counts[isin_value] = isin_counts.get(isin_value, 0) + 1
    #                 repeated_isins = {isin: count for isin, count in isin_counts.items() if count > 1}
    #                 fields2['Tranche'] =  len(repeated_isins)
    #             else:
    #                 pass
    #         except :
    #             pass