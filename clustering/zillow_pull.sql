USE zillow;

-- SELECT parcelid, logerror, transactiondate
-- FROM predictions_2016
-- LIMIT 500;

-- SELECT transactiondate, pd.logerror, pd.parcelid, airconditioningtypeid, architecturalstyletypeid, basementsqft, bathroomcnt, bedroomcnt, buildingclasstypeid, buildingqualitytypeid, calculatedbathnbr, decktypeid, finishedfloor1squarefeet, calculatedfinishedsquarefeet, finishedsquarefeet12, finishedsquarefeet13, finishedsquarefeet15, finishedsquarefeet50, finishedsquarefeet6, fips, fireplacecnt, fullbathcnt, garagecarcnt, garagetotalsqft, hashottuborspa, heatingorsystemtypeid, latitude, longitude, lotsizesquarefeet, poolcnt, poolsizesum, pooltypeid10, pooltypeid2, pooltypeid7, propertycountylandusecode, propertylandusetypeid, propertyzoningdesc, rawcensustractandblock, regionidcity, regionidcounty, regionidneighborhood, regionidzip, roomcnt, storytypeid, threequarterbathnbr, typeconstructiontypeid, unitcnt, yardbuildingsqft17, yardbuildingsqft26, yearbuilt, numberofstories, fireplaceflag, structuretaxvaluedollarcnt, taxvaluedollarcnt, assessmentyear, landtaxvaluedollarcnt, taxamount, taxdelinquencyflag, taxdelinquencyyear, censustractandblock
-- FROM predictions_2016 pd 
-- LEFT JOIN properties_2016 p ON p.parcelid = pd.parcelid;

SELECT pred_prop.transactiondate
,pred_prop.logerror
,pred_prop.parcelid
,airconditioningdesc
,architecturalstyledesc
,basementsqft
,bathroomcnt
,bedroomcnt
,buildingclassdesc
,buildingqualitytypeid
,calculatedbathnbr
,decktypeid
,finishedfloor1squarefeet
,calculatedfinishedsquarefeet
,finishedsquarefeet12
,finishedsquarefeet13
,finishedsquarefeet15
,finishedsquarefeet50
,finishedsquarefeet6
,fips
,fireplacecnt
,fullbathcnt
,garagecarcnt
,garagetotalsqft
,hashottuborspa
,heatingorsystemdesc
,latitude
,longitude
,lotsizesquarefeet
,poolcnt
,poolsizesum
,pooltypeid10
,pooltypeid2
,pooltypeid7
,propertycountylandusecode
,propertylandusedesc
,propertyzoningdesc
,rawcensustractandblock
,regionidcity
,regionidcounty
,regionidneighborhood
,regionidzip
,roomcnt
,storydesc
,threequarterbathnbr
,typeconstructiondesc
,unitcnt
,yardbuildingsqft17
,yardbuildingsqft26
,yearbuilt
,numberofstories
,fireplaceflag
,structuretaxvaluedollarcnt
,taxvaluedollarcnt
,assessmentyear
,landtaxvaluedollarcnt
,taxamount
,taxdelinquencyflag
,taxdelinquencyyear
,censustractandblock
FROM (SELECT pd.transactiondate, pd.logerror, pd.parcelid, airconditioningtypeid, architecturalstyletypeid, basementsqft, bathroomcnt, bedroomcnt, buildingclasstypeid, buildingqualitytypeid, calculatedbathnbr, decktypeid, finishedfloor1squarefeet, calculatedfinishedsquarefeet, finishedsquarefeet12, finishedsquarefeet13, finishedsquarefeet15, finishedsquarefeet50, finishedsquarefeet6, fips, fireplacecnt, fullbathcnt, garagecarcnt, garagetotalsqft, hashottuborspa, heatingorsystemtypeid, latitude, longitude, lotsizesquarefeet, poolcnt, poolsizesum, pooltypeid10, pooltypeid2, pooltypeid7, propertycountylandusecode, propertylandusetypeid, propertyzoningdesc, rawcensustractandblock, regionidcity, regionidcounty, regionidneighborhood, regionidzip, roomcnt, storytypeid, threequarterbathnbr, typeconstructiontypeid, unitcnt, yardbuildingsqft17, yardbuildingsqft26, yearbuilt, numberofstories, fireplaceflag, structuretaxvaluedollarcnt, taxvaluedollarcnt, assessmentyear, landtaxvaluedollarcnt, taxamount, taxdelinquencyflag, taxdelinquencyyear, censustractandblock
	FROM predictions_2017 pd 
	LEFT JOIN properties_2017 p ON p.parcelid = pd.parcelid) AS pred_prop
LEFT OUTER JOIN airconditioningtype act ON act.airconditioningtypeid = pred_prop.airconditioningtypeid
LEFT OUTER JOIN architecturalstyletype ast ON ast.architecturalstyletypeid = pred_prop.architecturalstyletypeid
LEFT OUTER JOIN buildingclasstype bct ON bct.buildingclasstypeid = pred_prop.buildingclasstypeid
LEFT OUTER JOIN heatingorsystemtype hst ON hst.heatingorsystemtypeid = pred_prop.heatingorsystemtypeid
LEFT OUTER JOIN propertylandusetype plu ON plu.propertylandusetypeid = pred_prop.propertylandusetypeid
LEFT OUTER JOIN storytype st ON st.storytypeid = pred_prop.storytypeid
LEFT OUTER JOIN typeconstructiontype tct ON tct.typeconstructiontypeid = pred_prop.typeconstructiontypeid
;






-- SELECT id
-- ,up.parcelid
-- ,airconditioningdesc
-- ,architecturalstyledesc
-- ,basementsqft
-- ,bathroomcnt
-- ,bedroomcnt
-- ,buildingclassdesc
-- ,buildingqualitytypeid
-- ,calculatedbathnbr
-- ,decktypeid
-- ,finishedfloor1squarefeet
-- ,calculatedfinishedsquarefeet
-- ,finishedsquarefeet12
-- ,finishedsquarefeet13
-- ,finishedsquarefeet15
-- ,finishedsquarefeet50
-- ,finishedsquarefeet6
-- ,fips
-- ,fireplacecnt
-- ,fullbathcnt
-- ,garagecarcnt
-- ,garagetotalsqft
-- ,hashottuborspa
-- ,heatingorsystemdesc
-- ,latitude
-- ,longitude
-- ,lotsizesquarefeet
-- ,poolcnt
-- ,poolsizesum
-- ,pooltypeid10
-- ,pooltypeid2
-- ,pooltypeid7
-- ,propertycountylandusecode
-- ,propertylandusedesc
-- ,propertyzoningdesc
-- ,rawcensustractandblock
-- ,regionidcity
-- ,regionidcounty
-- ,regionidneighborhood
-- ,regionidzip
-- ,roomcnt
-- ,storydesc
-- ,threequarterbathnbr
-- ,typeconstructiondesc
-- ,unitcnt
-- ,yardbuildingsqft17
-- ,yardbuildingsqft26
-- ,yearbuilt
-- ,numberofstories
-- ,fireplaceflag
-- ,structuretaxvaluedollarcnt
-- ,taxvaluedollarcnt
-- ,assessmentyear
-- ,landtaxvaluedollarcnt
-- ,taxamount
-- ,taxdelinquencyflag
-- ,taxdelinquencyyear
-- ,censustractandblock
-- FROM properties_2017 p
-- LEFT OUTER JOIN airconditioningtype act ON act.airconditioningtypeid = p.airconditioningtypeid
-- LEFT OUTER JOIN architecturalstyletype ast ON ast.architecturalstyletypeid = p.architecturalstyletypeid
-- LEFT OUTER JOIN buildingclasstype bct ON bct.buildingclasstypeid = p.buildingclasstypeid
-- LEFT OUTER JOIN heatingorsystemtype hst ON hst.heatingorsystemtypeid = p.heatingorsystemtypeid
-- LEFT OUTER JOIN propertylandusetype plu ON plu.propertylandusetypeid = p.propertylandusetypeid
-- LEFT OUTER JOIN storytype st ON st.storytypeid = p.storytypeid
-- LEFT OUTER JOIN typeconstructiontype tct ON tct.typeconstructiontypeid = p.typeconstructiontypeid
-- LEFT OUTER JOIN unique_properties up ON up.parcelid = p.parcelid
-- LIMIT 500;



