
USE zillow;

SELECT p17.id
,pd17.id
,p17.parcelid #AS parcelid
,pd17.parcelid #AS parcelid
,pd17.logerror AS logerror
,yearbuilt 
,calculatedfinishedsquarefeet
,bedroomcnt
,bathroomcnt
,fullbathcnt
,garagecarcnt
,roomcnt
,taxamount
,taxvaluedollarcnt
FROM predictions_2017 pd17
JOIN properties_2017 p17 ON pd17.parcelid = p17.parcelid 
LIMIT 10;



-- FROM properties_2017 p17
-- JOIN predictions_2017 pd17 ON p17.parcelid = pd17.parcelid

# swap out the calendar years on this to grab the 2017 data, but use existing query structure.

# DESCRIBE properties_2016;


