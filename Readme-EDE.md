# ImmoEliza - Data Analysis

### Step 1 : Data Cleaning
- The Kangaroo data set has 80368 rows and  53 columns. We cleaned our data as follows:
1. No duplicates
2. No blank spaces in string
3. Delete the unneccessary columns, namely URL and Unnamed: 0
3. After considering sum of missing values, we found there is 3998 rows without price, we delete all the rows without price. So the size of the data set now is : (76370, 51)
4. After checking the percentages of missing values, there are a lot columns missing more than 90% values, we used different methods (mean, Spearman correlation, statistical test) to check whether the swimming pool should keep for the future analysis. So we chose to remove all columns that missed more thann 90% but still keep "hasSwimmingPool" column. Now the size of data set is: (76370, 40). (We can presence the boxplot of swimmingpool&price.png with assumption missing values = 0 (False))
the list of removed columns (withouthasSwimmingPool )
accessibleDisabledPeople    100.000000
hasBalcony                  100.000000
monthlyCost                 100.000000
hasAirConditioning           98.601433
hasSwimmingPool              97.740394
hasDressingRoom              96.730042
hasFireplace                 96.212423
hasThermicPanels             96.127812
hasArmoredDoor               95.398666
gardenOrientation            93.030808
diningRoomSurface            91.413249
hasHeatPump                  90.701523

5. In the comparison of missing values, hasGarden  and gardenSurface has the same value, we can detete "hasGarden" column

#### IF ALL OF YOU HAS ANOTHER CLEANING DATA? WRITE IT HERE AND WE CAN PLOT DIFFERENCE PLOTS TO COMPARE FOR EACH CLEANING TO SEE HOW IT CHANGES !!!!!!!!

### Step 2: Data analysis
1. Compute Pearson correlation of every numeric column with price
2. Compute correlation matrix to plot heatmap (see heatmap.png)
3. From the heatmap;
-  Top 7 most influential: ['bedroomCount', 'terraceSurface', 'landSurface', 'facedeCount', 'bathroomCount', 'gardenSurface']
- Top 7 least influential: ['floorCount', 'parkingCountIndoor', 'parkingCountOutdoor', 'streetFacadeWidth', 'kitchenSurface', 'livingRoomSurface', 'buildingConstructionYear']
4. Qualitative and Quantitative variables: 
- Quantitative (24): ['id', 'bedroomCount', 'bathroomCount', 'postCode', 'habitableSurface', 'roomCount', 'monthlyCost', 'diningRoomSurface', 'buildingConstructionYear', 'facedeCount', 'floorCount', 'streetFacadeWidth', 'kitchenSurface', 'landSurface', 'livingRoomSurface', 'hasBalcony', 'gardenSurface', 'parkingCountIndoor', 'parkingCountOutdoor', 'toiletCount', 'terraceSurface', 'accessibleDisabledPeople', 'price', 'swimmingPool_missing']
- Qualitative (28): ['type', 'subtype', 'province', 'locality', 'hasAttic', 'hasBasement', 'hasDressingRoom', 'hasDiningRoom', 'buildingCondition', 'hasLift', 'floodZoneType', 'heatingType', 'hasHeatPump', 'hasPhotovoltaicPanels', 'hasThermicPanels', 'kitchenType', 'hasLivingRoom', 'hasGarden', 'gardenOrientation', 'hasAirConditioning', 'hasArmoredDoor', 'hasVisiophone', 'hasOffice', 'hasSwimmingPool', 'hasFireplace', 'hasTerrace', 'terraceOrientation', 'epcScore']


### Step 3: 