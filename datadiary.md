# ![alt text](https://www.shareicon.net/data/32x32/2016/02/13/718311_read_512x512.png) Data Diary 
***********************************************************************
> ### [Data-Used](#Data-used)

> ### [Dict](#Dict)

> ### [Goals](#Goals)

> ### [Steps](#Steps)

> ### [Notes](#Notes)
************************************************************************


## Data used

File (copy) | Source | Description | Nick in diary
--- | --- | ---
 [contracts_all.csv](./contracts_all.csv)| EP FOIA| Contracts EP has taken since '10 | EP
 [whd_whisard_copy.csv](./whd_whisard_copy.csv)| [W&H Compliance Action](https://enforcedata.dol.gov/views/data_catalogs.php) | Concluded WHD compliance actions since FY '05 | W&H
 [copy_wage_theft_database.csv](./copy_wage_theft_database.csv) | EP FOIA| EP Database kept by city management | WTD
 
**************************************************************************
## Dict
**************************************************************************
## Goals

**************************************************************************
## Steps

* Added all EP contracts into one csv with python script [combine_csv.py](./combine_csv.py)

* Combined datasets on legal name and contractor using pd.merge

* Some matched on NAN, removed those. There might be some trades who do
  not have a legal name in the W&H data that are in the EP data.

* Obtained 70 rows of matching columns.

* No EP matching anything from W&H since the ordinance was passed.

* Combined on trade name and contractor using pd.merge - got different results than legal name. 


***********************************************************************
## Notes



* The data will not include all contractors for the following reasons:
	* There is no guarantee that the contracts have the same name on
	  the EP contract as the W&H data, a typo might change it all.
	* Some lines contain multiple contractors, and I do not know how
	  to get soft matching yet. So those lines will automatically be
	  excluded.
    * User error


* All entries in WTD has them before the ordinance, not sure why.
* The merged variable should only be seen to find out if there are
  contracts used by the city. The repeated number of violations is just
  how python merged legal name of the business. 
