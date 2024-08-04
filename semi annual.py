def coupon_frequency_cleaning(given_string):
    coupon_frequency_sets = ({"jan", "jul"}, {"feb", "aug"}, {"mar", "sep"}, {"apr", "oct"}, {"may", "nov"}, {"jun", "dec"}, {"january", "july"}, {"february", "august"}, {"march", "september"}, {"april", "october"}, {"may", "november"}, {
                             "june", "december"}, {"january", "april", "july", "october"}, {"jan", "apr", "jul", "oct"}, {"february", "may", "august", "november"}, {"feb", "may", "aug", "nov"}, {"march", "june", "september", "december"}, {"mar", "jun", "sep", "dec"})

    month_keyword_sets = {"january": {"january", "jan"}, "february": {"february", "feb"}, "march": {"march", "mar"}, "april": {"april", "apr"}, "may": {"may"}, "june": {"june", "jun"}, "july": {"july", "jul"},
                          "august": {"august", "aug"}, "september": {"september", "sep", "sept"}, "october": {"october", "oct"}, "november": {"november", "nov"}, "december": {"december", "dec"}}
    
    lower_string=given_string.lower().split()
    month_list=lower_string
    for each_string in month_list:
        match= each_string in coupon_frequency_cleaning

coupon_frequency_cleaning('Interest Payment Dates: June 1 and December 1, commencing June 1, 2018Benchmark Treasury: 2.250% due November 15, 2027Benchmark Treasury Price and 98-16+; 2.419%Yield:Spread to Benchmark Treasury: +105 basis pointsYield to Maturity: 3.469%')