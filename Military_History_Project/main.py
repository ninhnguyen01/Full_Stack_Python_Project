# Import package
import webbrowser as wb


# Webpage source
source = 'https://mronline.org/2022/09/16/u-s-launched-251-military-interventions-since-1991-and-469-since-1798/'
wb.open(source)

country = 'U.S.'
since_year_1991 = 251
since_year_1798 = 469

print()
print(f'The {country} launched {since_year_1991} military interventions since 1991 and {since_year_1798} since 1798 according to a report by the Congressional Research Service, a U.S. government institution that compiles information on behalf of Congress that have been acknowledged.\nThis data was published on March 8, 2022 by the Congressional Research Service (CRS), in a document titled “Instances of Use of United States Armed Forces Abroad, 1798-2022.” ')
print('\n')