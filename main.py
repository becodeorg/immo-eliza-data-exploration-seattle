import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv("./datasets/Kangaroo.csv")
'''
    Rows:
        Indexes 5591 - 440319 is duplicate id: 20663057.0
    Columns:
        0 index
        1 id
        2 url
        4 subtype
        12 monthlyCost
        34 hasBalcony
        35 hasGarden
        38 parkingCountIndoor
        39 parkingCountOutdoor
        50 accessibleDisabledPeople
'''
# Remove rows
data.drop_duplicates(subset=['id'], keep='last', inplace=True)
data.dropna(subset=['price'], how='all', inplace=True)
# Remove columns
data.drop(data.columns[[0, 1, 2, 4, 12, 34, 35, 38, 39, 50]], axis=1, inplace=True)
# Replace strange values in epcScore column with NaN
data.loc[data['epcScore'].isin(['C_A', 'F_C', 'G_C', 'D_C', 'F_D', 'E_C', 'G_E', 'E_D', 'C_B', 'X', 'G_F']), 'epcScore'] = np.nan
# Replace outlier value in toiletCount column with 2
data.loc[data['toiletCount'] == 1958, 'toiletCount'] = 2
# Functions to clean data
to_int = lambda x : 0 if np.isnan(x) else int(x)
round_float = lambda x : 0 if np.isnan(x) else round(float(x), 2)
bool_to_int = lambda x : 1 if x == True else 0
# for flood zone replace missing values with NON_FLOOD_ZONE
flood_zone_replace_nan = lambda x : 'NON_FLOOD_ZONE' if pd.isnull(x) else x
# for kitchen type 0 if not equipped, 0.5 if semi-equipped, 1 if equipped
kitchen_type_cleaner = lambda x : 0 if pd.isnull(x) or "NOT" in x or "UN" in x else 0.5 if "SEMI" in x else 1
# for type 0 if APARTMENT, 1 if HOUSE
type_to_int = lambda x : 0 if x == 'APARTMENT' else 1
# Clean columns
# data.id = data.id.apply(to_int)
data.type = data.type.apply(type_to_int)
data.bedroomCount = data.bedroomCount.apply(to_int)
data.bathroomCount = data.bathroomCount.apply(to_int)
data.roomCount = data.roomCount.apply(to_int)
data.hasAttic = data.hasAttic.apply(bool_to_int)
data.hasBasement = data.hasBasement.apply(bool_to_int)
data.hasDressingRoom = data.hasDressingRoom.apply(bool_to_int)
data.hasDiningRoom = data.hasDiningRoom.apply(bool_to_int)
data.hasLift = data.hasLift.apply(bool_to_int)
data.hasHeatPump = data.hasHeatPump.apply(bool_to_int)
data.hasPhotovoltaicPanels = data.hasPhotovoltaicPanels.apply(bool_to_int)
data.hasThermicPanels = data.hasThermicPanels.apply(bool_to_int)
data.hasLivingRoom = data.hasLivingRoom.apply(bool_to_int)
# data.hasGarden = data.hasGarden.apply(bool_to_int)
data.hasAirConditioning = data.hasAirConditioning.apply(bool_to_int)
data.hasArmoredDoor = data.hasArmoredDoor.apply(bool_to_int)
data.hasVisiophone = data.hasVisiophone.apply(bool_to_int)
data.hasOffice = data.hasOffice.apply(bool_to_int)
data.hasSwimmingPool = data.hasSwimmingPool.apply(bool_to_int)
data.hasFireplace = data.hasFireplace.apply(bool_to_int)
data.hasTerrace = data.hasTerrace.apply(bool_to_int)
data.habitableSurface = data.habitableSurface.apply(to_int)
data.diningRoomSurface = data.diningRoomSurface.apply(to_int)
data.kitchenSurface = data.kitchenSurface.apply(to_int)
data.landSurface = data.landSurface.apply(to_int)
data.livingRoomSurface = data.livingRoomSurface.apply(to_int)
data.gardenSurface = data.gardenSurface.apply(to_int)
data.terraceSurface = data.terraceSurface.apply(to_int)
data.buildingConstructionYear = data.buildingConstructionYear.apply(to_int)
data.facedeCount = data.facedeCount.apply(to_int)
data.floorCount = data.floorCount.apply(to_int)
data.toiletCount = data.toiletCount.apply(to_int)
data.streetFacadeWidth = data.streetFacadeWidth.apply(round_float)
# data.parkingCountIndoor = data.parkingCountIndoor.apply(to_int)
# data.parkingCountOutdoor = data.parkingCountOutdoor.apply(to_int)
data.floodZoneType = data.floodZoneType.apply(flood_zone_replace_nan)
data.kitchenType = data.kitchenType.apply(kitchen_type_cleaner)
# Create columns from dictionaries
# 'buildingCondition', , 'epcScore'
# 'condition', , 'epcScore'
data = pd.get_dummies(data, columns=['floodZoneType', 'heatingType', 'gardenOrientation', 'terraceOrientation'], 
                      prefix = ['', 'heating', 'garden', 'terrace'], dtype=int)
# Create region column based on province
data['region'] = data.apply(lambda row : 1 if row.province in ['West Flanders', 'East Flanders', 'Antwerp', 'Flemish Brabant', 'Brussels', 'Limburg'] else 0, axis = 1)
# Remove province and lovality and NON_FLOOD_ZONE column as we have replaced NaNs with NON_FLOOD_ZONE before)
data.drop(columns=['province', 'locality', '_NON_FLOOD_ZONE'], inplace=True)

columns_to_keep = [
'type',
'region',
'kitchenType',
'bedroomCount',
'hasTerrace',
'hasGarden',
'habitableSurface',
'buildingCondition',
# 'condition_AS_NEW',         #6
# 'condition_GOOD',           #5
# 'condition_JUST_RENOVATED', #4
# 'condition_TO_BE_DONE_UP',  #3
# 'condition_TO_RENOVATE',    #2
# 'condition_TO_RESTORE',     #1
'epcScore',
# 'epcScore_A',               #9
# 'epcScore_A+',              #8
# 'epcScore_A++',             #7
# 'epcScore_B',               #6   
# 'epcScore_C',               #5
# 'epcScore_D',               #4
# 'epcScore_E',               #3
# 'epcScore_F',               #2
# 'epcScore_G',               #1
'price']
data.drop(columns=[col for col in data if col not in columns_to_keep], inplace=True)
data['buildingCondition'] = data.apply(lambda row : 0 if pd.isnull(row.buildingCondition) else 
                                       6 if 'AS_NEW' in row.buildingCondition else
                                        5 if 'GOOD' in row.buildingCondition else
                                         4 if 'JUST_RENOVATED' in row.buildingCondition else
                                          3 if 'TO_BE_DONE_UP' in row.buildingCondition else
                                           2 if 'TO_RENOVATE' in row.buildingCondition else 1, axis = 1)
data['epcScore'] = data.apply(lambda row : 0 if pd.isnull(row.epcScore) else 
                                       7 if 'A' == row.epcScore else
                                        8 if 'A+' == row.epcScore else
                                         9 if 'A++' == row.epcScore else
                                          6 if 'B' == row.epcScore else
                                           5 if 'C' == row.epcScore else 
                                           4 if 'D' == row.epcScore else
                                           3 if 'E' == row.epcScore else
                                           2 if 'F' == row.epcScore else 1, axis = 1)
# print(data.shape)

# print(data.floorCount.astype(str).str.extract('\\.(.*)')[0].unique())
# print(data.streetFacadeWidth.astype(str).str.extract('\\.(.*)')[0].unique())
# print(data.parkingCountIndoor.apply(to_int).unique())  # ?????
# print(data.parkingCountOutdoor.apply(to_int).unique()) # ?????
# print(data.type.unique())
# print(data.groupby("kitchenType").size())
# print(data.loc[data['toiletCount'] >= 10, ['id', 'toiletCount']].sort_values('toiletCount', ascending=False).head(10))
# print(data.loc[(data['gardenOrientation'].isnull()) & (data['gardenSurface'] > 0), ['id', 'gardenOrientation', 'gardenSurface']])
# print(data.loc[(data['terraceOrientation'].isnull()) & (data['hasTerrace'] == 1), ['id', 'terraceOrientation', 'terraceSurface', 'hasTerrace']])
# print(data.loc[(data['gardenSurface'] == 0) & (data['hasGarden'] == 1), ['id', 'gardenSurface', 'hasGarden']]) # empty - hasGarden can be removed
# print(data.loc[(data['terraceSurface'] == 0) & (data['hasTerrace'] == 1), ['id', 'terraceSurface', 'hasTerrace']])
# print(data.loc[(data['diningRoomSurface'] == 0) & (data['hasDiningRoom'] == 1), ['id', 'diningRoomSurface', 'hasDiningRoom']])
# print(data.loc[(data['livingRoomSurface'] == 0) & (data['hasLivingRoom'] == 1), ['id', 'livingRoomSurface', 'hasLivingRoom']])
# print(data.loc[data['toiletCount'] == 58, ['id']])

# data.info()
# print(data.describe())

# print(data.duplicated(subset=['id']))
# print(data.isnull().sum())

#create a histogram

# fig1 = px.histogram(data, x='parkingCountIndoor')
# fig2 = px.histogram(data, x='parkingCountOutdoor')

# fig1.show()
# fig2.show()

#create a box plot

# fig1 = px.box(data, y='habitableSurface')
# fig2 = px.box(data, y='parkingCountOutdoor')

# fig1.show()
# fig2.show()


# correlation = data.corr()

# # Create a heatmap with enhanced color scale
# sns.heatmap(
#     correlation, 
#     annot=True,            # Show correlation values
#     fmt=".2f",             # Limit decimals for better readability
#     cmap='coolwarm',       # Diverging colormap for contrast
#     center=0,              # Center at 0 for diverging colors
#     vmin=-1, vmax=1,       # Explicitly set the color range
#     linewidths=0.5,        # Add gridlines between cells
#     cbar_kws={"shrink": 0.8}  # Adjust color bar size
# )

# # Add title for context
# plt.title("Enhanced Correlation Heatmap")
# plt.xticks(rotation=45)  # Rotate x-axis labels for readability
# plt.yticks(rotation=0)   # Keep y-axis labels horizontal
# plt.tight_layout()       # Adjust layout to prevent label cutoff
# plt.show()

counts_surface = data.habitableSurface.value_counts().sort_index()
print(counts_surface.tail(25))
plt.bar(counts_surface.index, counts_surface.values, color='blue')
plt.xlabel('Square meters')
plt.ylabel('Properties count')
plt.title('Livable surface to properties count')
plt.xlim(0, 500)
plt.ylim(0, 1500)
plt.show()
