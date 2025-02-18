migration_url = 'https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/muutl/statfin_muutl_pxt_11a5.px'
migration_query = {
    "query": [
        {
            "code": "Vuosi",
            "selection": {
                "filter": "item",
                "values": [
                    "2002",
                    "2003",
                    "2004",
                    "2005",
                    "2006",
                    "2007",
                    "2008",
                    "2009",
                    "2010",
                    "2011",
                    "2012",
                    "2013",
                    "2014",
                    "2015",
                    "2016",
                    "2017",
                    "2018",
                    "2019",
                    "2020",
                    "2021",
                    "2022"
                ]
            }
        },
        {
            "code": "Tulomaakunta",
            "selection": {
                "filter": "item",
                "values": [
                    "MK01",
                    "MK02",
                    "MK04",
                    "MK05",
                    "MK06",
                    "MK07",
                    "MK08",
                    "MK09",
                    "MK10",
                    "MK11",
                    "MK12",
                    "MK13",
                    "MK14",
                    "MK15",
                    "MK16",
                    "MK17",
                    "MK18",
                    "MK19",
                    "MK21"
                ]
            }
        },
        {
            "code": "Lähtömaakunta",
            "selection": {
                "filter": "item",
                "values": [
                    "MK01",
                    "MK02",
                    "MK04",
                    "MK05",
                    "MK06",
                    "MK07",
                    "MK08",
                    "MK09",
                    "MK10",
                    "MK11",
                    "MK12",
                    "MK13",
                    "MK14",
                    "MK15",
                    "MK16",
                    "MK17",
                    "MK18",
                    "MK19",
                    "MK21"
                ]
            }
        },
        {
            "code": "Syntyperä",
            "selection": {
                "filter": "item",
                "values": [
                    "11",
                    "12",
                    "22",
                    "21"
                ]
            }
        },
        {
            "code": "Sukupuoli",
            "selection": {
                "filter": "item",
                "values": [
                    "1",
                    "2"
                ]
            }
        }
    ],
    "response": {
        "format": "json"
    }
}

age_values = {
    "code": "Ikä",
    "selection": {
        "filter": "item",
        "values": [
            "0-17",
            "18-24",
            "25-34",
            "35-44",
            "45-54",
            "55-64",
            "65-74",
            "75-"
        ]
    }
}

employment_url = 'https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/tyokay/statfin_tyokay_pxt_115i.px'
employment_query = {
    "query": [
        {
            "code": "Alue",
            "selection": {
                "filter": "agg:_Regions 2023.agg",
                "values": [
                    "MK01",
                    "MK02",
                    "MK04",
                    "MK05",
                    "MK06",
                    "MK07",
                    "MK08",
                    "MK09",
                    "MK10",
                    "MK11",
                    "MK12",
                    "MK13",
                    "MK14",
                    "MK15",
                    "MK16",
                    "MK17",
                    "MK18",
                    "MK19",
                    "MK21"
                ]
            }
        },
        {
            "code": "Toimiala",
            "selection": {
                "filter": "item",
                "values": [
                    "A",
                    "B",
                    "C",
                    "D",
                    "E",
                    "F",
                    "G",
                    "H",
                    "I",
                    "J",
                    "K",
                    "L",
                    "M",
                    "N",
                    "O",
                    "P",
                    "Q",
                    "R",
                    "S",
                    "T",
                    "U",
                    "X"
                ]
            }
        },
        {
            "code": "Sukupuoli",
            "selection": {
                "filter": "item",
                "values": [
                    "1",
                    "2"
                ]
            }
        }
    ],
    "response": {
        "format": "json"
    }
}
