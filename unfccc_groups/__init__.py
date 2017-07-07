"""
unfccc_groups
-------------

"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


ANNEX_ONE = [
    "AUS",
    "AUT",
    "BEL",
    "BGR",
    "BLR",
    "CAN",
    "CHE",
    "CYP",
    "CZE",
    "DEU",
    "DNK",
    "ESP",
    "EST",
    "EUU",
    "FIN",
    "FRA",
    "GBR",
    "GRC",
    "HRV",
    "HUN",
    "IRL",
    "ISL",
    "ITA",
    "JPN",
    "LIE",
    "LTU",
    "LUX",
    "LVA",
    "MCO",
    "MLT",
    "NLD",
    "NOR",
    "NZL",
    "POL",
    "PRT",
    "ROU",
    "RUS",
    "SVK",
    "SVN",
    "SWE",
    "TUR",
    "UKR",
    "USA"
]

EU_MEMBERS = [
    "AUT",
    "BEL",
    "BGR",
    "CYP",
    "CZE",
    "DEU",
    "DNK",
    "ESP",
    "EST",
    "FIN",
    "FRA",
    "GBR",
    "GRC",
    "HRV",
    "HUN",
    "IRL",
    "ITA",
    "LTU",
    "LUX",
    "LVA",
    "MLT",
    "NLD",
    "POL",
    "PRT",
    "ROU",
    "SVK",
    "SVN",
    "SWE"
]

G20 = [
    "ARG",
    "AUS",
    "BRA",
    "CAN",
    "CHN",
    "DEU",
    "EUU",
    "FRA",
    "GBR",
    "IDN",
    "IND",
    "ITA",
    "JPN",
    "KOR",
    "MEX",
    "RUS",
    "SAU",
    "TUR",
    "USA",
    "ZAF"
]

G7 = [
    "CAN",
    "DEU",
    "EUU",
    "FRA",
    "GBR",
    "ITA",
    "JPN",
    "USA"
]

GRADUATED_LDCS = [
    "BWA",
    "CPV",
    "GNQ",
    "MDV",
    "WSM"
]

LDCS = [
    "AFG",
    "AGO",
    "BDI",
    "BEN",
    "BFA",
    "BGD",
    "BTN",
    "CAF",
    "COD",
    "COM",
    "DJI",
    "ERI",
    "ETH",
    "GIN",
    "GMB",
    "GNB",
    "HTI",
    "KHM",
    "KIR",
    "LAO",
    "LBR",
    "LSO",
    "MDG",
    "MLI",
    "MMR",
    "MOZ",
    "MRT",
    "MWI",
    "NER",
    "NPL",
    "RWA",
    "SDN",
    "SEN",
    "SLB",
    "SLE",
    "SOM",
    "SSD",
    "STP",
    "TCD",
    "TGO",
    "TLS",
    "TUV",
    "TZA",
    "UGA",
    "VUT",
    "YEM",
    "ZMB"
]

NON_ANNEX_ONE = [
    "AFG",
    "AGO",
    "ALB",
    "AND",
    "ARE",
    "ARG",
    "ARM",
    "ATG",
    "AZE",
    "BDI",
    "BEN",
    "BFA",
    "BGD",
    "BHR",
    "BHS",
    "BIH",
    "BLZ",
    "BOL",
    "BRA",
    "BRB",
    "BRN",
    "BTN",
    "BWA",
    "CAF",
    "CHL",
    "CHN",
    "CIV",
    "CMR",
    "COD",
    "COG",
    "COK",
    "COL",
    "COM",
    "CPV",
    "CRI",
    "CUB",
    "DJI",
    "DMA",
    "DOM",
    "DZA",
    "ECU",
    "EGY",
    "ERI",
    "ETH",
    "FJI",
    "FSM",
    "GAB",
    "GEO",
    "GHA",
    "GIN",
    "GMB",
    "GNB",
    "GNQ",
    "GRD",
    "GTM",
    "GUY",
    "HND",
    "HTI",
    "IDN",
    "IND",
    "IRN",
    "IRQ",
    "ISR",
    "JAM",
    "JOR",
    "KAZ",
    "KEN",
    "KGZ",
    "KHM",
    "KIR",
    "KNA",
    "KOR",
    "KWT",
    "LAO",
    "LBN",
    "LBR",
    "LBY",
    "LCA",
    "LKA",
    "LSO",
    "MAR",
    "MDA",
    "MDG",
    "MDV",
    "MEX",
    "MHL",
    "MKD",
    "MLI",
    "MMR",
    "MNE",
    "MNG",
    "MOZ",
    "MRT",
    "MUS",
    "MWI",
    "MYS",
    "NAM",
    "NER",
    "NGA",
    "NIC",
    "NIU",
    "NPL",
    "NRU",
    "OMN",
    "PAK",
    "PAN",
    "PER",
    "PHL",
    "PLW",
    "PNG",
    "PRK",
    "PRY",
    "PSE",
    "QAT",
    "RWA",
    "SAU",
    "SDN",
    "SEN",
    "SGP",
    "SLB",
    "SLE",
    "SLV",
    "SMR",
    "SOM",
    "SRB",
    "SSD",
    "STP",
    "SUR",
    "SWZ",
    "SYC",
    "SYR",
    "TCD",
    "TGO",
    "THA",
    "TJK",
    "TKM",
    "TLS",
    "TON",
    "TTO",
    "TUN",
    "TUV",
    "TZA",
    "UGA",
    "URY",
    "UZB",
    "VCT",
    "VEN",
    "VNM",
    "VUT",
    "WSM",
    "YEM",
    "ZAF",
    "ZMB",
    "ZWE"
]

SIDS = [
    "ATG",
    "BHS",
    "BLZ",
    "BRB",
    "COM",
    "CPV",
    "CUB",
    "DMA",
    "DOM",
    "FJI",
    "FSM",
    "GNB",
    "GRD",
    "GUY",
    "HTI",
    "JAM",
    "KIR",
    "KNA",
    "LCA",
    "MDV",
    "MHL",
    "MUS",
    "NRU",
    "PLW",
    "PNG",
    "SGP",
    "SLB",
    "STP",
    "SUR",
    "SYC",
    "TLS",
    "TON",
    "TTO",
    "TUV",
    "VCT",
    "VUT",
    "WSM"
]

UNFCCC = [
    "AFG",
    "AGO",
    "ALB",
    "AND",
    "ARE",
    "ARG",
    "ARM",
    "ATG",
    "AUS",
    "AUT",
    "AZE",
    "BDI",
    "BEL",
    "BEN",
    "BFA",
    "BGD",
    "BGR",
    "BHR",
    "BHS",
    "BIH",
    "BLR",
    "BLZ",
    "BOL",
    "BRA",
    "BRB",
    "BRN",
    "BTN",
    "BWA",
    "CAF",
    "CAN",
    "CHE",
    "CHL",
    "CHN",
    "CIV",
    "CMR",
    "COD",
    "COG",
    "COK",
    "COL",
    "COM",
    "CPV",
    "CRI",
    "CUB",
    "CYP",
    "CZE",
    "DEU",
    "DJI",
    "DMA",
    "DNK",
    "DOM",
    "DZA",
    "ECU",
    "EGY",
    "ERI",
    "ESP",
    "EST",
    "ETH",
    "EUU",
    "FIN",
    "FJI",
    "FRA",
    "FSM",
    "GAB",
    "GBR",
    "GEO",
    "GHA",
    "GIN",
    "GMB",
    "GNB",
    "GNQ",
    "GRC",
    "GRD",
    "GTM",
    "GUY",
    "HND",
    "HRV",
    "HTI",
    "HUN",
    "IDN",
    "IND",
    "IRL",
    "IRN",
    "IRQ",
    "ISL",
    "ISR",
    "ITA",
    "JAM",
    "JOR",
    "JPN",
    "KAZ",
    "KEN",
    "KGZ",
    "KHM",
    "KIR",
    "KNA",
    "KOR",
    "KWT",
    "LAO",
    "LBN",
    "LBR",
    "LBY",
    "LCA",
    "LIE",
    "LKA",
    "LSO",
    "LTU",
    "LUX",
    "LVA",
    "MAR",
    "MCO",
    "MDA",
    "MDG",
    "MDV",
    "MEX",
    "MHL",
    "MKD",
    "MLI",
    "MLT",
    "MMR",
    "MNE",
    "MNG",
    "MOZ",
    "MRT",
    "MUS",
    "MWI",
    "MYS",
    "NAM",
    "NER",
    "NGA",
    "NIC",
    "NIU",
    "NLD",
    "NOR",
    "NPL",
    "NRU",
    "NZL",
    "OMN",
    "PAK",
    "PAN",
    "PER",
    "PHL",
    "PLW",
    "PNG",
    "POL",
    "PRK",
    "PRT",
    "PRY",
    "PSE",
    "QAT",
    "ROU",
    "RUS",
    "RWA",
    "SAU",
    "SDN",
    "SEN",
    "SGP",
    "SLB",
    "SLE",
    "SLV",
    "SMR",
    "SOM",
    "SRB",
    "SSD",
    "STP",
    "SUR",
    "SVK",
    "SVN",
    "SWE",
    "SWZ",
    "SYC",
    "SYR",
    "TCD",
    "TGO",
    "THA",
    "TJK",
    "TKM",
    "TLS",
    "TON",
    "TTO",
    "TUN",
    "TUR",
    "TUV",
    "TZA",
    "UGA",
    "UKR",
    "URY",
    "USA",
    "UZB",
    "VCT",
    "VEN",
    "VNM",
    "VUT",
    "WSM",
    "YEM",
    "ZAF",
    "ZMB",
    "ZWE"
]

