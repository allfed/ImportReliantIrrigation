# ImportReliantIrrigation

## Introduction

Multiple sources of data are used to estimate the fraction of irrigated cropland that is reliant on electricity or diesel:
 - aquastat: includes government level census data with information about the country's irrigated cropland area technologies, including the amount of land that is supplied by pumps (source), and how that water is then applied to the cropland (scheme).
 - gmiav5: includes global 5 minute resolution data including the total area equipped for irrigation, the total surface water irrigation, and the total groundwater irrigation.  
 - pandas "naturalearth_lowres": a low resolution map including shapefiles for all country boundaries, identified by country code.


A complex series of data manipulations were required to come to a reasonable estimate of the irrigation, and it should be considered a first pass with low confidence in any particular region.

Available data from aquastat includes the following country level data 
	spate_area
	lowland_area
	sprinkler_area
	localized_area
	surface_area
	power_area
	surface_water_area
	ground_water_area
	total_irrigated_area

Unfortunately, some of the census data is inghjv,hjThe percent reliant 

assign total irrigated area to the maximum of total area, scheme area, or power area

 The aquastat data is first used to 

 estimate_reliant_scheme_sw
	 assume lowland and spate schemes are allocated first to surface water irrigated regions
	 #if surface water area is defined, and nonzero
	 #remove unreliant surface water irrigation area from consideration, and assume remaining sprinkler, localized, and surface irrigation are evenly split between ground and surface water irrigated area
	 if(nonsw_area == 0):

	 #elif(unreliant_sw_area>sw_area)
		 #if(reliant_scheme_area<nonsw_area)
			 #no surface water area assigned reliant
			 #reliant area all assigned to nonsw_area
		#else:
			#this case is unlikely and hard to work with, so forget about surface water
	else:#simple case, unreliant_sw_area < sw_area
		#now, even splitting of each, but will need to multiply out by multiplier to get back to original total fraction
	else: #surface water isn't defined, so we just use the assumed value


	def estimate_source_reliance(power_area,total_irrigated_area,max_area,sw_area):

	# we assume the source is reliant 
	# if power_area is greatest area
	else:
		reliant_source = power_area/max_area
		reliant_source_assumed=reliant_source
		#determine fraction of reliance that is likely surface water vs ground water
		#assume pumped electricity area are allocated first to non-surface water regions
		if(nonsw_area>power_area):
			reliant_source_nonsw=power_area/nonsw_area
			reliant_source_sw=0
		else:#nonsurface water area <= power area 
			reliant_source_nonsw=1
			reliant_source_sw=(power_area-nonsw_area)/(sw_area)
		#if data unavailable, don't assume difference between ground and surface water

	def estimate_scheme_reliance(scheme_total,total_irrigated_area,localized_area,
	#for now, assume total irrigated area is zero if not listed
	#catch issues with incomplete or nonsense data
	#(ignore aquastat surface and ground water area data, if data is not complete or is erroneous (if nan))

	if(
		abs(scheme_total)-1 
		> abs(total_irrigated_area_zeroed) 
		or 
		abs(scheme_total) + 1 
		< abs(total_irrigated_area_zeroed)
		):		

		# in this case we don't have good direct estimate regarding the fraction of the scheme that is reliant. We'll guess all remaining area is electrified if spate or lowland are listed explicitly,
		# as long as neither sprinkler or localized are listed explicitly as zero
		if(localized_area_zeroed+sprinkler_area_zeroed==0):

			if(localized_area==0 or sprinkler_area==0):
				reliant_scheme=np.nan
				reliant_scheme_assumed=0	
				reliant_scheme_nonsw=reliant_scheme_assumed
				reliant_scheme_sw=reliant_scheme_assumed

			elif(#both localized_area and sprinkler area must have been nan
				spate_area_zeroed+lowland_area_zeroed+surface_area_zeroed>max_area/2
				):
				reliant_scheme =\
					(max_area-(spate_area_zeroed+lowland_area_zeroed+surface_area_zeroed))/max_area
				reliant_scheme_assumed=reliant_scheme
				reliant_scheme_area=max_area-(spate_area_zeroed+lowland_area_zeroed+surface_area_zeroed)
				[reliant_scheme_sw,reliant_scheme_nonsw]=estimate_reliant_scheme_sw(reliant_scheme_assumed,reliant_scheme_area,surface_water_area,max_area,spate_area,lowland_area,surface_area,localized_area,sprinkler_area)
			#we don't really know anything about it.
			else:
				reliant_scheme=np.nan
				reliant_scheme_assumed=0
				reliant_scheme_nonsw=reliant_scheme_assumed
				reliant_scheme_sw=reliant_scheme_assumed				
		else:
			reliant_scheme=(localized_area_zeroed+sprinkler_area_zeroed)/max_area
			reliant_scheme_assumed=reliant_scheme
			reliant_scheme_area=localized_area_zeroed+sprinkler_area_zeroed
			[reliant_scheme_sw,reliant_scheme_nonsw]=estimate_reliant_scheme_sw(
	else:
		#good data with nonzero values, complete irrigation data, surface water greater than spate plus lowland irrigation 
		reliant_scheme=(localized_area_zeroed+sprinkler_area_zeroed)/max_area
		reliant_scheme_assumed=reliant_scheme
		reliant_scheme_area=localized_area_zeroed+sprinkler_area_zeroed



#assign total irrigated area to the maximum of total area, scheme area, or power area
areas=np.array([scheme_total,total_irrigated_area,power_area])
areas=areas[~np.isnan(areas)]
#not enough data to estimate value.
if(np.sum(areas)==0):
	max_area=np.nan
	reliant_source = np.nan
	reliant_source_assumed = np.nan
	reliant_scheme = np.nan
	reliant_scheme_assumed = np.nan
	reliant_source_sw=reliant_source_assumed
	reliant_source_nonsw=reliant_source_assumed
	reliant_scheme_sw=reliant_scheme_assumed
	reliant_scheme_nonsw=reliant_scheme_assumed
else: #at least one of original areas array is not nan and not zero
	max_area=max(areas)

	[reliant_source,reliant_source_assumed,reliant_source_sw,reliant_source_nonsw] = \
		estimate_source_reliance(power_area,total_irrigated_area,max_area,surface_water_area)

	[reliant_scheme,reliant_scheme_assumed,reliant_scheme_sw,reliant_scheme_nonsw]= \
		estimate_scheme_reliance(scheme_total,total_irrigated_area,localized_area,sprinkler_area,spate_area,lowland_area,surface_area,max_area,surface_water_area)

gmiav5_all_areas.append(highRes['area'].sum())
if(np.isnan(reliant_scheme) and np.isnan(reliant_source)):
	reliant = np.nan
else:
	reliant=1-(1-reliant_scheme_assumed)*(1-reliant_source_assumed)
	reliant_sw=1-(1-reliant_scheme_sw)*(1-reliant_source_sw)
	reliant_nonsw=1-(1-reliant_scheme_nonsw)*(1-reliant_source_nonsw)
