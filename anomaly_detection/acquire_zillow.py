import env
import pandas as pd

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_2016_property_data():
    '''gets 2016 zillow properties & predictions data from zillow sql dbase'''
    return pd.read_sql('''SELECT pred_prop.transactiondate\
    ,pred_prop.logerror\
    ,pred_prop.parcelid\
    ,airconditioningdesc\
    ,architecturalstyledesc\
    ,basementsqft\
    ,bathroomcnt\
    ,bedroomcnt\
    ,buildingclassdesc\
    ,buildingqualitytypeid\
    ,calculatedbathnbr\
    ,decktypeid\
    ,finishedfloor1squarefeet\
    ,calculatedfinishedsquarefeet\
    ,finishedsquarefeet12\
    ,finishedsquarefeet13\
    ,finishedsquarefeet15\
    ,finishedsquarefeet50\
    ,finishedsquarefeet6\
    ,fips\
    ,fireplacecnt\
    ,fullbathcnt\
    ,garagecarcnt\
    ,garagetotalsqft\
    ,hashottuborspa\
    ,heatingorsystemdesc\
    ,latitude\
    ,longitude\
    ,lotsizesquarefeet\
    ,poolcnt\
    ,poolsizesum\
    ,pooltypeid10\
    ,pooltypeid2\
    ,pooltypeid7\
    ,propertycountylandusecode\
    ,propertylandusedesc\
    ,propertyzoningdesc\
    ,rawcensustractandblock\
    ,regionidcity\
    ,regionidcounty\
    ,regionidneighborhood\
    ,regionidzip\
    ,roomcnt\
    ,storydesc\
    ,threequarterbathnbr\
    ,typeconstructiondesc\
    ,unitcnt\
    ,yardbuildingsqft17\
    ,yardbuildingsqft26\
    ,yearbuilt\
    ,numberofstories\
    ,fireplaceflag\
    ,structuretaxvaluedollarcnt\
    ,taxvaluedollarcnt\
    ,assessmentyear\
    ,landtaxvaluedollarcnt\
    ,taxamount\
    ,taxdelinquencyflag\
    ,taxdelinquencyyear\
    ,censustractandblock\
    FROM (SELECT pd.transactiondate, pd.logerror, pd.parcelid, airconditioningtypeid, architecturalstyletypeid, basementsqft, bathroomcnt, bedroomcnt, buildingclasstypeid, buildingqualitytypeid, calculatedbathnbr, decktypeid, finishedfloor1squarefeet, calculatedfinishedsquarefeet, finishedsquarefeet12, finishedsquarefeet13, finishedsquarefeet15, finishedsquarefeet50, finishedsquarefeet6, fips, fireplacecnt, fullbathcnt, garagecarcnt, garagetotalsqft, hashottuborspa, heatingorsystemtypeid, latitude, longitude, lotsizesquarefeet, poolcnt, poolsizesum, pooltypeid10, pooltypeid2, pooltypeid7, propertycountylandusecode, propertylandusetypeid, propertyzoningdesc, rawcensustractandblock, regionidcity, regionidcounty, regionidneighborhood, regionidzip, roomcnt, storytypeid, threequarterbathnbr, typeconstructiontypeid, unitcnt, yardbuildingsqft17, yardbuildingsqft26, yearbuilt, numberofstories, fireplaceflag, structuretaxvaluedollarcnt, taxvaluedollarcnt, assessmentyear, landtaxvaluedollarcnt, taxamount, taxdelinquencyflag, taxdelinquencyyear, censustractandblock\
        FROM predictions_2016 pd\
        LEFT JOIN properties_2016 p ON p.parcelid = pd.parcelid) AS pred_prop\
    LEFT OUTER JOIN airconditioningtype act ON act.airconditioningtypeid = pred_prop.airconditioningtypeid\
    LEFT OUTER JOIN architecturalstyletype ast ON ast.architecturalstyletypeid = pred_prop.architecturalstyletypeid\
    LEFT OUTER JOIN buildingclasstype bct ON bct.buildingclasstypeid = pred_prop.buildingclasstypeid\
    LEFT OUTER JOIN heatingorsystemtype hst ON hst.heatingorsystemtypeid = pred_prop.heatingorsystemtypeid\
    LEFT OUTER JOIN propertylandusetype plu ON plu.propertylandusetypeid = pred_prop.propertylandusetypeid\
    LEFT OUTER JOIN storytype st ON st.storytypeid = pred_prop.storytypeid\
    LEFT OUTER JOIN typeconstructiontype tct ON tct.typeconstructiontypeid = pred_prop.typeconstructiontypeid;'''
    , get_connection('zillow'))

def write_2016_csv(df):
    '''creates csv of 2016 zillow info'''
    df.to_csv('properties_2016.csv')

def get_2017_property_data():
    '''gets 2017 zillow properties & predictions data from zillow sql dbase'''
    return pd.read_sql('''SELECT pred_prop.transactiondate\
    ,pred_prop.logerror\
    ,pred_prop.parcelid\
    ,airconditioningdesc\
    ,architecturalstyledesc\
    ,basementsqft\
    ,bathroomcnt\
    ,bedroomcnt\
    ,buildingclassdesc\
    ,buildingqualitytypeid\
    ,calculatedbathnbr\
    ,decktypeid\
    ,finishedfloor1squarefeet\
    ,calculatedfinishedsquarefeet\
    ,finishedsquarefeet12\
    ,finishedsquarefeet13\
    ,finishedsquarefeet15\
    ,finishedsquarefeet50\
    ,finishedsquarefeet6\
    ,fips\
    ,fireplacecnt\
    ,fullbathcnt\
    ,garagecarcnt\
    ,garagetotalsqft\
    ,hashottuborspa\
    ,heatingorsystemdesc\
    ,latitude\
    ,longitude\
    ,lotsizesquarefeet\
    ,poolcnt\
    ,poolsizesum\
    ,pooltypeid10\
    ,pooltypeid2\
    ,pooltypeid7\
    ,propertycountylandusecode\
    ,propertylandusedesc\
    ,propertyzoningdesc\
    ,rawcensustractandblock\
    ,regionidcity\
    ,regionidcounty\
    ,regionidneighborhood\
    ,regionidzip\
    ,roomcnt\
    ,storydesc\
    ,threequarterbathnbr\
    ,typeconstructiondesc\
    ,unitcnt\
    ,yardbuildingsqft17\
    ,yardbuildingsqft26\
    ,yearbuilt\
    ,numberofstories\
    ,fireplaceflag\
    ,structuretaxvaluedollarcnt\
    ,taxvaluedollarcnt\
    ,assessmentyear\
    ,landtaxvaluedollarcnt\
    ,taxamount\
    ,taxdelinquencyflag\
    ,taxdelinquencyyear\
    ,censustractandblock\
    FROM (SELECT pd.transactiondate, pd.logerror, pd.parcelid, airconditioningtypeid, architecturalstyletypeid, basementsqft, bathroomcnt, bedroomcnt, buildingclasstypeid, buildingqualitytypeid, calculatedbathnbr, decktypeid, finishedfloor1squarefeet, calculatedfinishedsquarefeet, finishedsquarefeet12, finishedsquarefeet13, finishedsquarefeet15, finishedsquarefeet50, finishedsquarefeet6, fips, fireplacecnt, fullbathcnt, garagecarcnt, garagetotalsqft, hashottuborspa, heatingorsystemtypeid, latitude, longitude, lotsizesquarefeet, poolcnt, poolsizesum, pooltypeid10, pooltypeid2, pooltypeid7, propertycountylandusecode, propertylandusetypeid, propertyzoningdesc, rawcensustractandblock, regionidcity, regionidcounty, regionidneighborhood, regionidzip, roomcnt, storytypeid, threequarterbathnbr, typeconstructiontypeid, unitcnt, yardbuildingsqft17, yardbuildingsqft26, yearbuilt, numberofstories, fireplaceflag, structuretaxvaluedollarcnt, taxvaluedollarcnt, assessmentyear, landtaxvaluedollarcnt, taxamount, taxdelinquencyflag, taxdelinquencyyear, censustractandblock\
        FROM predictions_2017 pd\
        LEFT JOIN properties_2017 p ON p.parcelid = pd.parcelid) AS pred_prop\
    LEFT OUTER JOIN airconditioningtype act ON act.airconditioningtypeid = pred_prop.airconditioningtypeid\
    LEFT OUTER JOIN architecturalstyletype ast ON ast.architecturalstyletypeid = pred_prop.architecturalstyletypeid\
    LEFT OUTER JOIN buildingclasstype bct ON bct.buildingclasstypeid = pred_prop.buildingclasstypeid\
    LEFT OUTER JOIN heatingorsystemtype hst ON hst.heatingorsystemtypeid = pred_prop.heatingorsystemtypeid\
    LEFT OUTER JOIN propertylandusetype plu ON plu.propertylandusetypeid = pred_prop.propertylandusetypeid\
    LEFT OUTER JOIN storytype st ON st.storytypeid = pred_prop.storytypeid\
    LEFT OUTER JOIN typeconstructiontype tct ON tct.typeconstructiontypeid = pred_prop.typeconstructiontypeid;'''
    , get_connection('zillow'))

def write_2017_csv(df):
    '''creates csv of 2017 zillow info'''
    df.to_csv('properties_2017.csv')


def all_zillow_data():
    zillow_chunks = [get_2016_property_data(),get_2017_property_data()]
    all_zillow = pd.concat(zillow_chunks, ignore_index=True)
    all_zillow.dropna(subset=['latitude', 'longitude'], inplace=True)
    all_zillow.to_csv('zillow.csv')
    return all_zillow


def peekatdata(df):
    print("\n \n SHAPE:")
    print(df.shape)

    print("\n \n COLS:")
    print(df.columns)

    print("\n \n INFO:")
    print(df.info())

    print("\n \n Missing Values:")
    missing_vals = df.columns[df.isnull().any()]
    print(df.isnull().sum())

    print("\n \n DESCRIBE:")
    print(df.describe())

    print('\n \n HEAD:')
    print(df.head(5))

    print('\n \n TAIL:' )
    print(df.tail(5))
